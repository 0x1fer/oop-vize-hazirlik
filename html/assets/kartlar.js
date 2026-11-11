/* OOP Vize Hazırlık: flashcard'lar. Anki'deki gibi aralıklı tekrar (SM-2 tabanlı, öğrenme adımları 1 dk ve 10 dk).
   Veri: assets/kartlar-data.js (anki/src/build.py üretir). İlerleme bu tarayıcıda localStorage'da (oop:fc:*). */
(function () {
  'use strict';
  var DESTELER = window.FC_DESTELER || [];
  var S = window.BZStore;
  var root = document.getElementById('fc');
  var body = document.body;
  var crumb = document.querySelector('.fc-crumb');

  var DK = 60000, GUN_MS = 864e5;
  var OGRENME = [1, 10];        // yeni kart adımları (dakika)
  var YENIDEN = [10];           // unutulan kartın adımı (dakika)
  var MEZUN = 1, KOLAY = 4;     // öğrenmeden çıkınca ilk aralık (gün)
  var ONDEN = 20 * DK;          // başka kart kalmayınca 20 dk içindeki öğrenme kartları öne alınır
  var YENI = 0, OGREN = 1, TEKRAR = 2, YENIDEN_OGREN = 3;

  var KART = {}, DESTE = {};
  DESTELER.forEach(function (d) {
    DESTE[d.id] = d;
    d.kartlar.forEach(function (k) { k.d = d.id; KART[k.id] = k; });
  });
  var TUMU = { id: 'tumu', no: '∑', ad: 'Tüm desteler', renk: '#A78BFA', kartlar: [] };
  DESTELER.forEach(function (d) { TUMU.kartlar = TUMU.kartlar.concat(d.kartlar); });
  function deste(id) { return id === 'tumu' ? TUMU : DESTE[id]; }

  var ETIKET = {
    cikmis: 'Çıkmış soru', hoca_sorar: 'Hoca sorar', kod: 'Kod', senaryo: 'Senaryo', senaryo_cozum: 'Senaryo çözümü',
    tanim: 'Tanım', liste: 'Liste', ezber: 'Ezber', test: 'Test', karsilastirma: 'Karşılaştırma', sinav_taktigi: 'Sınav taktiği',
    kavram: 'Kavram', sif: 'Stable forms', vaka: 'Vaka', yorum: 'Diyagram yorumu', iliski: 'İlişki', notasyon: 'Notasyon',
    alistirma: 'Alıştırma', etik: 'Etik', spmp: 'SPMP', faz: 'Faz', workflow: 'Workflow', solid: 'SOLID', anlam: 'Anlam',
    sayi: 'Sayı', duzeltme: 'Düzeltme', cohesion: 'Cohesion', coupling: 'Coupling', model: 'Model', diyagram: 'Diyagram',
    ornek: 'Örnek', algoritma: 'Algoritma', karakteristik: 'Karakteristik', 'karakteristik->alt': 'Karakteristik → alt',
    'alt->karakteristik': 'Alt → karakteristik'
  };
  var ONCELIK = ['cikmis', 'hoca_sorar', 'kod', 'senaryo', 'tanim'];
  function etiketAdi(t) { return ETIKET[t] || (t.charAt(0).toLocaleUpperCase('tr') + t.slice(1).replace(/_/g, ' ')); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ---------------------------------------------------------------- kayıt */
  var durum = S.get('fc:s', {});          // kart id -> {q, st, iv, e, due, r, l}
  function kaydet() { S.set('fc:s', durum); ozetKaydet(); }
  function bugun() { return Math.floor((Date.now() - 4 * 3600e3 - new Date().getTimezoneOffset() * DK) / GUN_MS); } // gün sabah 4'te döner
  function gunluk() {
    var g = S.get('fc:gun', null);
    if (!g || g.gun !== bugun()) g = { gun: bugun(), yeni: {}, cevap: 0, dogru: 0 };
    return g;
  }
  function limit() { return S.get('fc:limit', 20); }
  function st(id) { return durum[id] || { q: YENI }; }

  /* ---------------------------------------------------------------- zamanlama */
  function cevapla(s0, puan, simdi) {
    var s = { q: s0.q, st: s0.st || 0, iv: s0.iv || 0, e: s0.e || 2.5, due: s0.due, r: (s0.r || 0) + 1, l: s0.l || 0 };
    var gun = bugun();
    function adim(dk) { s.due = simdi + dk * DK; }
    function mezun(iv) { s.q = TEKRAR; s.iv = iv; s.st = 0; s.due = gun + iv; }
    if (s.q === YENI || s.q === OGREN) {
      if (s.q === YENI) s.st = 0;
      s.q = OGREN;
      if (puan === 1) { s.st = 0; adim(OGRENME[0]); }
      else if (puan === 2) adim(s.st === 0 && OGRENME.length > 1 ? (OGRENME[0] + OGRENME[1]) / 2 : OGRENME[s.st]);
      else if (puan === 3) { if (s.st + 1 >= OGRENME.length) mezun(MEZUN); else { s.st++; adim(OGRENME[s.st]); } }
      else mezun(KOLAY);
    } else if (s.q === TEKRAR) {
      if (puan === 1) { s.l++; s.e = Math.max(1.3, s.e - 0.2); s.iv = 1; s.q = YENIDEN_OGREN; s.st = 0; adim(YENIDEN[0]); }
      else {
        if (puan === 2) { s.e = Math.max(1.3, s.e - 0.15); s.iv = Math.max(s.iv + 1, Math.round(s.iv * 1.2)); }
        else if (puan === 3) s.iv = Math.max(s.iv + 1, Math.round(s.iv * s.e));
        else { s.iv = Math.max(s.iv + 1, Math.round(s.iv * s.e * 1.3)); s.e += 0.15; }
        s.due = gun + s.iv;
      }
    } else {                      // yeniden öğrenme
      if (puan === 1) { s.st = 0; adim(YENIDEN[0]); }
      else if (puan === 2) adim(YENIDEN[0] * 1.5);
      else mezun(puan === 4 ? s.iv + 1 : s.iv);
    }
    return s;
  }
  function sureYaz(s, simdi) {
    if (s.q === OGREN || s.q === YENIDEN_OGREN) {
      var dk = Math.round((s.due - simdi) / DK);
      return dk < 1 ? '<1 dk' : dk < 60 ? dk + ' dk' : Math.round(dk / 60) + ' sa';
    }
    var g = s.iv;
    return g < 30 ? g + ' gün' : g < 365 ? (g / 30).toFixed(g < 90 ? 1 : 0).replace('.', ',').replace(',0', '') + ' ay' : (g / 365).toFixed(1).replace('.', ',') + ' yıl';
  }

  /* ---------------------------------------------------------------- sayımlar ve sıra */
  function sayim(d) {
    var gun = bugun(), simdi = Date.now(), g = gunluk();
    var c = { yeni: 0, ogren: 0, tekrar: 0, yeniToplam: 0, ogrenilen: 0, olgun: 0, toplam: d.kartlar.length };
    var yeniKalan = {};
    (d.id === 'tumu' ? DESTELER : [d]).forEach(function (x) { yeniKalan[x.id] = Math.max(0, limit() - (g.yeni[x.id] || 0)); });
    d.kartlar.forEach(function (k) {
      var s = st(k.id);
      if (s.q === YENI) { c.yeniToplam++; if (yeniKalan[k.d] > 0) { yeniKalan[k.d]--; c.yeni++; } }
      else if (s.q === TEKRAR) { if (s.due <= gun) c.tekrar++; if (s.iv >= 21) c.olgun++; else c.ogrenilen++; }
      else { c.ogrenilen++; if (s.due < simdi + GUN_MS / 2) c.ogren++; }
    });
    return c;
  }
  // sıradaki kart: önce zamanı gelen öğrenme kartı, sonra tekrar ve yeni kartlar karışık, en son öne alınabilen öğrenme kartı
  function siradaki(d, haric) {
    var gun = bugun(), simdi = Date.now(), g = gunluk();
    var ogren = [], tekrar = [], yeni = [], yeniKalan = {};
    (d.id === 'tumu' ? DESTELER : [d]).forEach(function (x) { yeniKalan[x.id] = Math.max(0, limit() - (g.yeni[x.id] || 0)); });
    d.kartlar.forEach(function (k) {
      if (k.id === haric) return;
      var s = st(k.id);
      if (s.q === YENI) { if (yeniKalan[k.d] > 0) { yeniKalan[k.d]--; yeni.push(k); } }
      else if (s.q === TEKRAR) { if (s.due <= gun) tekrar.push(k); }
      else ogren.push(k);
    });
    ogren.sort(function (a, b) { return st(a.id).due - st(b.id).due; });
    if (ogren.length && st(ogren[0].id).due <= simdi) return ogren[0];
    if (tekrar.length || yeni.length) {
      tekrar.sort(function (a, b) { return st(a.id).due - st(b.id).due; });
      var oran = tekrar.length / (tekrar.length + yeni.length);
      if (!yeni.length || (tekrar.length && Math.random() < oran)) return tekrar[0];
      return yeni[0];
    }
    if (ogren.length && st(ogren[0].id).due <= simdi + ONDEN) return ogren[0];
    if (haric && KART[haric] && (KART[haric].d === d.id || d.id === 'tumu')) {
      var h = st(haric);
      if ((h.q === OGREN || h.q === YENIDEN_OGREN) && h.due <= simdi + ONDEN) return KART[haric];
    }
    return null;
  }
  function sonrakiOgrenme(d) {
    var en = null;
    d.kartlar.forEach(function (k) { var s = st(k.id); if ((s.q === OGREN || s.q === YENIDEN_OGREN) && (en === null || s.due < en)) en = s.due; });
    return en;
  }
  function ozetKaydet() {
    var c = sayim(TUMU);
    S.set('fc:ozet', { gun: bugun(), yeni: c.yeni, ogren: c.ogren, tekrar: c.tekrar, goruldu: c.toplam - c.yeniToplam, toplam: c.toplam });
  }

  /* ---------------------------------------------------------------- görünümler */
  var aktif = null;                 // çalışma oturumu
  function vurgu(renk) { body.style.setProperty('--accent', renk || '#A78BFA'); }
  function sayilar(c, aktifTur) {
    return '<span class="n n-yeni' + (aktifTur === 'yeni' ? ' on' : '') + '" title="Yeni">' + c.yeni + '</span>' +
      '<span class="n n-ogren' + (aktifTur === 'ogren' ? ' on' : '') + '" title="Öğreniliyor">' + c.ogren + '</span>' +
      '<span class="n n-tekrar' + (aktifTur === 'tekrar' ? ' on' : '') + '" title="Tekrar zamanı gelen">' + c.tekrar + '</span>';
  }
  function cubuk(c) {
    var t = c.toplam || 1;
    return '<div class="fc-bar" title="Olgun: ' + c.olgun + ' · Öğrenilen: ' + c.ogrenilen + ' · Hiç görülmemiş: ' + c.yeniToplam + '">' +
      '<i class="b-olgun" style="width:' + (c.olgun / t * 100) + '%"></i><i class="b-ogren" style="width:' + (c.ogrenilen / t * 100) + '%"></i></div>';
  }

  function listeGoster() {
    vurgu(); crumb.textContent = "Flashcard'lar"; document.title = "Flashcard'lar | OOP Vize";
    var hepsi = sayim(TUMU), bugunIs = hepsi.yeni + hepsi.ogren + hepsi.tekrar, g = gunluk();
    var satir = DESTELER.map(function (d) {
      var c = sayim(d);
      return '<a class="fc-deck" href="#' + d.id + '" style="--hue:' + d.renk + '">' +
        '<span class="badge">' + esc(d.no) + '</span>' +
        '<span class="fc-deck-t"><b>' + esc(d.ad) + '</b><small>' + c.toplam + ' kart · ' + (c.toplam - c.yeniToplam) + ' görüldü</small>' + cubuk(c) + '</span>' +
        '<span class="fc-counts">' + sayilar(c) + '</span><span class="go" aria-hidden="true">›</span></a>';
    }).join('');
    root.innerHTML =
      '<section class="fc-hero">' +
        '<div><p class="kicker">Aralıklı tekrar</p><h1>Flashcard\'lar</h1>' +
        '<p class="lead">Anki\'deki gibi çalış: soruyu gör, cevabı aklından söyle, sonra kendini puanla. Bilemediğin kartlar birkaç dakika sonra, bildiklerin günler sonra tekrar gelir. ' +
        'Her konunun destesi ayrı; ilerlemen bu tarayıcıda saklanır.</p></div>' +
        '<div class="fc-today">' +
          '<div class="fc-today-n"><b>' + bugunIs + '</b><span>kart bugün seni bekliyor</span></div>' +
          '<div class="fc-counts big">' + sayilar(hepsi) + '</div>' +
          '<div class="fc-legend"><span><i class="n-yeni"></i>Yeni</span><span><i class="n-ogren"></i>Öğreniliyor</span><span><i class="n-tekrar"></i>Tekrar</span></div>' +
          (g.cevap ? '<p class="fc-muted">Bugün ' + g.cevap + ' cevap, %' + Math.round(g.dogru / g.cevap * 100) + ' doğru.</p>' : '') +
          '<a class="fc-btn primary" href="#tumu/calis">' + (bugunIs ? 'Bütün destelerden çalış' : 'Bugünlük bitti 🎉') + '</a>' +
          '<a class="fc-btn" href="#tumu/serbest/cikmis">Sadece çıkmış sorular (serbest)</a>' +
        '</div>' +
      '</section>' +
      '<div class="sec-h"><h2>Desteler</h2><p>konu sırasıyla, ' + TUMU.kartlar.length + ' kart</p></div>' +
      '<section class="fc-decks">' + satir + '</section>' +
      '<section class="fc-help"><h2>Nasıl çalışır?</h2><ol>' +
        '<li><b>Tekrar</b>: bilemedin, kart 1 dakika sonra yine gelir.</li>' +
        '<li><b>Zor</b>: zorlanarak bildin, aralık kısa tutulur.</li>' +
        '<li><b>İyi</b>: bildin, kart bir sonraki adıma geçer (10 dk → 1 gün → 2–3 gün → …).</li>' +
        '<li><b>Kolay</b>: çok kolaydı, kart 4 gün sonraya atlar.</li>' +
      '</ol><p class="fc-muted">Kısayollar: <kbd>Boşluk</kbd> cevabı göster / İyi, <kbd>1</kbd>–<kbd>4</kbd> puan, <kbd>Z</kbd> geri al, <kbd>Esc</kbd> desteye dön. ' +
      'Sınava az kaldıysa <b>serbest tekrar</b> ile planı bozmadan bütün kartları ya da sadece çıkmışları hızlıca dönebilirsin.</p></section>';
  }

  function etiketler(d) {
    var say = {};
    d.kartlar.forEach(function (k) { k.t.forEach(function (t) { say[t] = (say[t] || 0) + 1; }); });
    return Object.keys(say).filter(function (t) { return say[t] >= 3 || ONCELIK.indexOf(t) >= 0; })
      .sort(function (a, b) {
        var pa = ONCELIK.indexOf(a), pb = ONCELIK.indexOf(b);
        if (pa >= 0 || pb >= 0) return (pa < 0 ? 99 : pa) - (pb < 0 ? 99 : pb);
        return say[b] - say[a];
      }).map(function (t) { return [t, say[t]]; });
  }

  function desteGoster(d) {
    vurgu(d.renk); crumb.textContent = d.ad; document.title = d.ad + " | Flashcard'lar";
    var c = sayim(d), bugunIs = c.yeni + c.ogren + c.tekrar, son = sonrakiOgrenme(d);
    var chips = '<a class="fc-chip" href="#' + d.id + '/serbest">Tümü <small>' + d.kartlar.length + '</small></a>' +
      etiketler(d).map(function (e) { return '<a class="fc-chip" href="#' + d.id + '/serbest/' + encodeURIComponent(e[0]) + '">' + esc(etiketAdi(e[0])) + ' <small>' + e[1] + '</small></a>'; }).join('');
    var bekleyen = !bugunIs && son ? '<p class="fc-muted">Öğrenme adımındaki kartlar ' + new Date(son).toLocaleTimeString('tr', { hour: '2-digit', minute: '2-digit' }) + ' civarında tekrar gelecek.</p>' : '';
    root.innerHTML =
      '<a class="fc-back" href="#">‹ Desteler</a>' +
      '<section class="fc-over" style="--hue:' + d.renk + '">' +
        '<div class="fc-over-h"><span class="badge">' + esc(d.no) + '</span><div><p class="kicker">' + (d.id === 'tumu' ? 'Bütün konular' : 'Konu ' + esc(d.no)) + '</p><h1>' + esc(d.ad) + '</h1></div></div>' +
        '<div class="fc-over-grid">' +
          '<div class="fc-stat"><span class="n-yeni">' + c.yeni + '</span><small>Yeni</small></div>' +
          '<div class="fc-stat"><span class="n-ogren">' + c.ogren + '</span><small>Öğreniliyor</small></div>' +
          '<div class="fc-stat"><span class="n-tekrar">' + c.tekrar + '</span><small>Tekrar</small></div>' +
        '</div>' + cubuk(c) +
        '<p class="fc-muted">' + c.toplam + ' kart: ' + c.yeniToplam + ' hiç görülmedi, ' + c.ogrenilen + ' öğreniliyor, ' + c.olgun + ' olgun (21+ gün aralık).</p>' +
        (bugunIs ? '<a class="fc-btn primary big" href="#' + d.id + '/calis">Çalışmaya başla</a>' :
          '<div class="fc-done-note">Bu desteyi bugünlük bitirdin. ' + (c.yeniToplam ? 'Daha fazla yeni kart için günlük limiti artırabilir ya da serbest tekrar yapabilirsin.' : '') + '</div>') + bekleyen +
      '</section>' +
      '<section class="fc-panel"><h2>Serbest tekrar</h2><p class="fc-muted">Planı etkilemez: seçtiğin kartları karışık sırayla döner, bilemediklerin tura geri eklenir. Sınavdan önceki gece için ideal.</p>' +
        '<div class="fc-chips">' + chips + '</div></section>' +
      '<section class="fc-panel fc-row">' +
        '<a class="fc-btn" href="#' + d.id + '/liste">Kartlara göz at</a>' +
        (d.konu ? '<a class="fc-btn" href="' + d.konu + '.html">Konu anlatımını aç</a>' : '') +
        '<label class="fc-limit">Günlük yeni kart <input type="number" id="fcLimit" min="0" max="500" step="5" value="' + limit() + '"></label>' +
        '<button class="fc-btn ghost danger" type="button" id="fcReset">Bu destenin ilerlemesini sıfırla</button>' +
      '</section>';
    document.getElementById('fcLimit').addEventListener('change', function () {
      var v = Math.max(0, Math.min(500, parseInt(this.value, 10) || 0));
      S.set('fc:limit', v); ozetKaydet(); desteGoster(d);
    });
    document.getElementById('fcReset').addEventListener('click', function () {
      if (!confirm('"' + d.ad + '" destesindeki ' + d.kartlar.length + ' kartın tekrar planı silinsin mi? Bu geri alınamaz.')) return;
      d.kartlar.forEach(function (k) { delete durum[k.id]; });
      var g = gunluk();
      if (d.id === 'tumu') g.yeni = {}; else delete g.yeni[d.id];
      S.set('fc:gun', g); kaydet(); desteGoster(d);
    });
  }

  /* ---------------------------------------------------------------- çalışma ekranı */
  function calisGoster(d, serbest, etiket) {
    vurgu(d.renk); crumb.textContent = d.ad; document.title = d.ad + " | Flashcard'lar";
    aktif = { d: d, serbest: serbest, acik: false, kart: null, geri: [], adet: 0, dogru: 0 };
    if (serbest) {
      var liste = d.kartlar.filter(function (k) { return !etiket || k.t.indexOf(etiket) >= 0; }).slice();
      for (var i = liste.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), x = liste[i]; liste[i] = liste[j]; liste[j] = x; }
      aktif.sira = liste; aktif.toplam = liste.length; aktif.etiket = etiket;
    }
    iskelet();
    ilerle();
  }

  function iskelet() {
    var d = aktif.d;
    root.innerHTML =
      '<section class="fc-study" style="--hue:' + d.renk + '">' +
        '<div class="fc-study-top"><a class="fc-back" href="#' + d.id + '">‹ ' + esc(d.ad) + '</a>' +
          '<span class="fc-counts" id="fcCounts"></span>' +
          '<button class="fc-icon" type="button" id="fcUndo" title="Geri al (Z)" aria-label="Geri al" disabled>↶<span class="lbl"> Geri al</span></button></div>' +
        '<div class="fc-meter"><i id="fcMeter"></i></div>' +
        '<article class="fc-card" id="fcCard" tabindex="-1"></article>' +
        '<div class="fc-actions" id="fcActions"></div>' +
      '</section>';
    document.getElementById('fcUndo').addEventListener('click', geriAl);
    document.getElementById('fcCard').addEventListener('click', function (e) {
      if (!aktif.acik && aktif.kart && !e.target.closest('a')) goster();
    });
  }

  function ilerle(haric) {
    var a = aktif;
    a.acik = false;
    if (a.serbest) a.kart = a.sira[0] || null;
    else a.kart = siradaki(a.d, haric);
    if (!a.kart) return bitti();
    ciz();
  }

  function tur(k) {
    var s = st(k.id);
    return s.q === YENI ? 'yeni' : s.q === TEKRAR ? 'tekrar' : 'ogren';
  }

  function ciz() {
    var a = aktif, k = a.kart, kartEl = document.getElementById('fcCard');
    var cnt = document.getElementById('fcCounts'), meter = document.getElementById('fcMeter');
    if (a.serbest) {
      cnt.innerHTML = '<span class="n">' + a.sira.length + ' kaldı</span>' + (a.etiket ? '<span class="fc-tag">' + esc(etiketAdi(a.etiket)) + '</span>' : '');
      meter.style.width = ((a.toplam - a.sira.length) / Math.max(1, a.toplam) * 100) + '%';
    } else {
      var c = sayim(a.d);
      cnt.innerHTML = sayilar(c, tur(k));
      var kalan = c.yeni + c.ogren + c.tekrar;
      meter.style.width = (a.adet / Math.max(1, a.adet + kalan) * 100) + '%';
    }
    var kaynak = a.d.id === 'tumu' ? '<span class="fc-src" style="--hue:' + DESTE[k.d].renk + '">' + esc(DESTE[k.d].ad) + '</span>' : '';
    var etiketHtml = k.t.filter(function (t) { return ONCELIK.indexOf(t) >= 0 && t !== 'tanim'; })
      .map(function (t) { return '<span class="fc-tag t-' + t + '">' + esc(etiketAdi(t)) + '</span>'; }).join('');
    kartEl.innerHTML =
      '<div class="fc-meta">' + kaynak + etiketHtml + '</div>' +
      '<div class="fc-q">' + k.f + '</div>' +
      (a.acik ? '<div class="fc-sep"><span>Cevap</span></div><div class="fc-a">' + k.b + '</div>' : '<p class="fc-tap">Cevabı aklından söyle, sonra göster.</p>');
    kartEl.classList.toggle('acik', a.acik);
    var act = document.getElementById('fcActions');
    if (!a.acik) {
      act.innerHTML = '<button class="fc-btn primary big" type="button" data-g="1">Cevabı göster <kbd>Boşluk</kbd></button>';
    } else if (a.serbest) {
      act.innerHTML = '<div class="fc-rate two">' +
        '<button type="button" class="r1" data-p="1"><b>Bilemedim</b><small>tura geri ekle</small><kbd>1</kbd></button>' +
        '<button type="button" class="r3" data-p="3"><b>Bildim</b><small>turdan çıkar</small><kbd>Boşluk</kbd></button></div>';
    } else {
      var s0 = st(k.id), simdi = Date.now();
      var adlar = ['Tekrar', 'Zor', 'İyi', 'Kolay'];
      act.innerHTML = '<div class="fc-rate">' + [1, 2, 3, 4].map(function (p) {
        return '<button type="button" class="r' + p + '" data-p="' + p + '"><small>' + sureYaz(cevapla(s0, p, simdi), simdi) + '</small><b>' + adlar[p - 1] + '</b><kbd>' + p + '</kbd></button>';
      }).join('') + '</div>';
    }
    act.onclick = function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      if (b.dataset.g) goster(); else puanla(+b.dataset.p);
    };
    document.getElementById('fcUndo').disabled = !a.geri.length;
    if (a.acik) {
      var ilk = act.querySelector('[data-p="3"]');
      if (ilk && matchMedia('(hover: hover)').matches) ilk.focus({ preventScroll: true });
    }
    if (!a.acik) window.scrollTo({ top: 0 });
  }

  function goster() { if (aktif && aktif.kart && !aktif.acik) { aktif.acik = true; ciz(); } }

  function puanla(p) {
    var a = aktif;
    if (!a || !a.acik || !a.kart) return;
    var k = a.kart, g = gunluk();
    if (a.serbest) {
      a.geri.push({ serbest: true, sira: a.sira.slice(), adet: a.adet, dogru: a.dogru });
      a.sira.shift();
      if (p === 1) a.sira.splice(Math.min(3, a.sira.length), 0, k); else a.dogru++;
      a.adet++;
      return ilerle();
    }
    var once = durum[k.id] ? JSON.parse(JSON.stringify(durum[k.id])) : null;
    a.geri.push({ id: k.id, once: once, gun: JSON.parse(JSON.stringify(g)), adet: a.adet, dogru: a.dogru });
    if (a.geri.length > 30) a.geri.shift();
    var s0 = st(k.id);
    if (s0.q === YENI) g.yeni[k.d] = (g.yeni[k.d] || 0) + 1;
    g.cevap++; if (p > 1) g.dogru++;
    S.set('fc:gun', g);
    durum[k.id] = cevapla(s0, p, Date.now());
    kaydet();
    a.adet++; if (p > 1) a.dogru++;
    ilerle(k.id);
  }

  function geriAl() {
    var a = aktif;
    if (!a || !a.geri.length) return;
    var u = a.geri.pop();
    a.adet = u.adet; a.dogru = u.dogru;
    if (u.serbest) { a.sira = u.sira; a.kart = a.sira[0]; }
    else {
      if (u.once) durum[u.id] = u.once; else delete durum[u.id];
      S.set('fc:gun', u.gun); kaydet();
      a.kart = KART[u.id];
    }
    if (!document.getElementById('fcCard')) iskelet();   // bitiş ekranından geri dönülüyor
    a.acik = true; ciz();
  }

  function bitti() {
    var a = aktif, d = a.d;
    var oran = a.adet ? Math.round(a.dogru / a.adet * 100) : 0;
    var son = !a.serbest && sonrakiOgrenme(d);
    var c = sayim(d);
    document.querySelector('.fc-study').innerHTML =
      '<div class="fc-finish">' +
        '<div class="fc-finish-ic" aria-hidden="true">' + (a.adet ? '🎉' : '✅') + '</div>' +
        '<h1>' + (a.serbest ? 'Tur bitti!' : a.adet ? 'Bu desteyi bugünlük bitirdin!' : 'Şu an çalışılacak kart yok') + '</h1>' +
        (a.adet ? '<p class="fc-finish-s"><b>' + a.adet + '</b> cevap · <b>%' + oran + '</b> ' + (a.serbest ? 'ilk seferde bildin' : 'doğru') + '</p>' : '') +
        (son ? '<p class="fc-muted">Öğrenme adımındaki kartlar ' + new Date(son).toLocaleTimeString('tr', { hour: '2-digit', minute: '2-digit' }) + ' civarında yeniden gelecek; o zaman bu sayfaya dön.</p>' : '') +
        '<div class="fc-row center">' +
          (son ? '<button class="fc-btn primary" type="button" id="fcAhead">Bekleyenleri şimdi çalış</button>' : '') +
          (!a.serbest && c.yeniToplam ? '<button class="fc-btn" type="button" id="fcMore">+10 yeni kart</button>' : '') +
          '<a class="fc-btn" href="#' + d.id + '/serbest">Serbest tekrar</a>' +
          '<a class="fc-btn" href="#' + d.id + '">Desteye dön</a>' +
          '<a class="fc-btn" href="#">Bütün desteler</a>' +
        '</div>' +
        (a.geri.length ? '<button class="fc-icon" type="button" id="fcUndo2">↶ Son cevabı geri al</button>' : '') +
      '</div>';
    var ahead = document.getElementById('fcAhead');
    if (ahead) ahead.addEventListener('click', function () {
      d.kartlar.forEach(function (k) { var s = durum[k.id]; if (s && (s.q === OGREN || s.q === YENIDEN_OGREN) && s.due > Date.now()) s.due = Date.now(); });
      kaydet(); calisGoster(d, false);
    });
    var more = document.getElementById('fcMore');
    if (more) more.addEventListener('click', function () {
      var g = gunluk();
      (d.id === 'tumu' ? DESTELER : [d]).forEach(function (x) { g.yeni[x.id] = (g.yeni[x.id] || 0) - 10; });
      S.set('fc:gun', g); calisGoster(d, false);
    });
    var u2 = document.getElementById('fcUndo2');
    if (u2) u2.addEventListener('click', geriAl);
  }

  /* ---------------------------------------------------------------- göz at */
  function listeKartGoster(d) {
    vurgu(d.renk); crumb.textContent = d.ad; document.title = d.ad + ' (liste) | Flashcard\'lar';
    var gun = bugun();
    function durumYaz(k) {
      var s = st(k.id);
      if (s.q === YENI) return '<span class="fc-st yeni">Yeni</span>';
      if (s.q === TEKRAR) { var f = s.due - gun; return '<span class="fc-st tekrar">' + (f <= 0 ? 'Bugün' : f + ' gün sonra') + '</span>'; }
      return '<span class="fc-st ogren">Öğreniliyor</span>';
    }
    root.innerHTML =
      '<a class="fc-back" href="#' + d.id + '">‹ ' + esc(d.ad) + '</a>' +
      '<div class="fc-list-h"><h1>' + esc(d.ad) + ' <small>' + d.kartlar.length + ' kart</small></h1>' +
      '<input type="search" id="fcFind" placeholder="Kartlarda ara" autocomplete="off"></div>' +
      '<ol class="fc-list" id="fcList">' + d.kartlar.map(function (k, i) {
        return '<li data-i="' + i + '"><details><summary><span class="fc-list-q">' + k.f + '</span>' + durumYaz(k) + '</summary><div class="fc-a">' + k.b + '</div></details></li>';
      }).join('') + '</ol>';
    var metin = d.kartlar.map(function (k) { return (k.f + ' ' + k.b).replace(/<[^>]+>/g, ' ').toLocaleLowerCase('tr'); });
    var lis = document.querySelectorAll('#fcList > li');
    document.getElementById('fcFind').addEventListener('input', function () {
      var q = this.value.trim().toLocaleLowerCase('tr');
      lis.forEach(function (li, i) { li.hidden = q && metin[i].indexOf(q) < 0; });
    });
  }

  /* ---------------------------------------------------------------- yönlendirme ve klavye */
  function yonlen() {
    var h = decodeURIComponent(location.hash.replace(/^#\/?/, '')).split('/');
    var d = deste(h[0]);
    aktif = null;
    if (!d) listeGoster();
    else if (h[1] === 'calis') calisGoster(d, false);
    else if (h[1] === 'serbest') calisGoster(d, true, h[2] || null);
    else if (h[1] === 'liste') listeKartGoster(d);
    else desteGoster(d);
    if (!aktif) window.scrollTo({ top: 0 });
    ozetKaydet();
  }
  window.addEventListener('hashchange', yonlen);
  crumb.addEventListener('click', function (e) {
    var d = aktif && aktif.d;
    if (d) { e.preventDefault(); location.hash = d.id; }
  });

  document.addEventListener('keydown', function (e) {
    if (!aktif || !document.getElementById('fcCard') || e.defaultPrevented) return;
    if (document.documentElement.classList.contains('dua-open')) return;
    var sBox = document.getElementById('search');
    if (sBox && !sBox.hidden) return;
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA')) return;
    var k = e.key;
    if (k === ' ' || k === 'Enter') {
      if (t && t.tagName === 'BUTTON' && k === 'Enter') return;   // odaktaki düğmeye Enter kendi işini yapsın
      e.preventDefault();
      if (!aktif.acik) goster(); else puanla(3);
    } else if (/^[1-4]$/.test(k) && aktif.acik) {
      e.preventDefault();
      var p = +k;
      if (aktif.serbest) p = p === 1 ? 1 : 3;
      puanla(p);
    } else if (k === 'z' || k === 'Z') { e.preventDefault(); geriAl(); }
    else if (k === 'Escape') location.hash = aktif.d.id;
  }, true);   // yakalama evresi: app.js aramayı kapatmadan önce aramanın açık olduğunu görelim

  if (!DESTELER.length) { root.innerHTML = '<p class="fc-empty">Kart verisi yüklenemedi.</p>'; return; }
  yonlen();
})();
