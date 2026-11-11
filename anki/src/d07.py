"""Konu 7: Nesne yönelimli analiz (Chapter 13)."""
from ortak import en, ipucu, ol, ul

DESTE = "07 Nesne Yönelimli Analiz"

KARTLAR = [
    ("<b>Object-oriented analysis (OOA)</b> nedir? Analiz iş akışının iki amacı?",
     "OO paradigmanın <b>yarı biçimsel (semiformal)</b> analiz tekniği; bu iş akışında <b>sınıflar çıkarılır</b>.\n"
     "Amaçlar: gereksinimleri <b>daha derin anlamak</b> ve onları <b>bakımı kolay</b> bir tasarım ve gerçekleştirmeye götürecek şekilde tanımlamak.",
     "tanim"),
    ("Analiz iş akışındaki <b>üç sınıf türü</b>?",
     ol("<b>Entity class</b>", "<b>Boundary class</b>", "<b>Control class</b>") + "Üçü de UML'in <b>stereotype</b> genişletmesidir.",
     "liste cikmis"),
    ("<b>Entity class</b> neyi modeller? Örnek?",
     "<b>Uzun ömürlü (long-lived) bilgiyi</b>; gerçek sistemdeki varlıkları.\nÖrnek: Account, Investment, Mortgage, Kişi, Araç."
     + en("An entity class models information that is long lived."),
     "tanim cikmis"),
    ("<b>Boundary class</b> neyi modeller? Örnek?",
     "Ürün ile <b>çevresi (aktörler) arasındaki etkileşimi</b>; genellikle <b>giriş/çıkış</b>. Her giriş ekranı, çıkış ekranı ve basılı rapor bir boundary sınıfıdır.\n"
     "Örnek: User Interface Class, Investments Report Class."
     + en("A boundary class models the interaction between the product and the environment; it is generally associated with input or output."),
     "tanim cikmis"),
    ("<b>Control class</b> neyi modeller? Örnek?",
     "<b>Karmaşık hesaplamaları ve algoritmaları</b>; use case akışını yönetir. Her önemsiz olmayan hesaplama bir control sınıfıdır.\n"
     "Örnek: Estimate Funds for Week Class, Elevator Controller."
     + en("A control class models complex computations and algorithms."),
     "tanim cikmis"),
    ("Entity / boundary / control sınıflarının simgeleri (hocanın tahtası)?",
     "Entity: <b>altı çizili daire</b>.\nBoundary: <b>solunda dikey çizgi olan daire</b>.\nControl: <b>üstünde ok olan daire</b>.\nStereotipler: «entity», «boundary», «control».",
     "notasyon"),
    ("Sınıf türünü söyle: (a) KiralamaEkrani (b) Musteri (c) UcretHesaplayici (d) FaturaRaporu",
     "(a) <b>Boundary</b> (b) <b>Entity</b> (c) <b>Control</b> (d) <b>Boundary</b> (rapor = çıktı)",
     "senaryo"),

    # --- Üç adım ---
    ("Entity sınıflarını çıkarmanın <b>üç adımı</b>?",
     ol("<b>Functional modeling:</b> bütün use case'lerin senaryolarını sun",
        "<b>Entity class modeling:</b> entity sınıfları, nitelikleri, ilişkileri → <b>class diagram</b>",
        "<b>Dynamic modeling:</b> her sınıfa/sınıfın yaptığı işlemler → <b>statechart</b>")
     + "Bu adımlar artırımlı ve yinelemeli yapılır.",
     "liste cikmis"),
    ("<b>Scenario</b> nedir?",
     "Bir use case'in <b>bir örneği</b> (instance). Hedef ürünü kavramak için <b>yeterli sayıda</b> senaryo incelenir (ne çok fazla ne çok az)."
     + en("A scenario is an instance of a use case."),
     "tanim"),
    ("Normal ve exceptional senaryo farkı? (asansör örneği)",
     "<b>Normal:</b> beklenen akış (User A 3. katta yukarı düğmesine basar, 7. kata gider…).\n"
     "<b>Exceptional:</b> beklenmeyen durum (yukarıya bastı ama aşağı gitmek istediğini fark etti, yanlış asansöre bindi).",
     "kavram"),

    # --- Asansör ---
    ("Asansör probleminin iki use case'i?",
     "<b>Press an Elevator Button</b> ve <b>Press a Floor Button</b> (aktör: User).",
     "vaka"),
    ("<b>Noun extraction</b> nasıl yapılır? (2 aşama)",
     ol("Ürünü <b>tek paragrafta</b> tanımla (kısa problem tanımı)",
        "<b>İsimleri</b> belirle; problem sınırının <b>dışındakileri</b> ve <b>soyut isimleri</b> ele; kalanlar aday sınıflar")
     + ipucu("Soyut isimler sınıf değil ama nitelik olabilir."),
     "tanim cikmis"),
    ("Asansör paragrafındaki isimler hangileri? Hangileri neden elendi?",
     "İsimler: button, elevator, floor, movement, building, illumination, request, door.\n"
     "<b>floor, building, door</b> → problem sınırının dışında. <b>movement, illumination, request</b> → soyut isimler.\n"
     "Kalan: <b>Elevator</b> ve <b>Button</b> (alt sınıflar: Elevator Button, Floor Button).",
     "vaka"),
    ("Asansörde neden <b>Elevator Controller Class</b> eklendi?",
     "Düğmeler asansörlerle doğrudan iletişim kurmaz; bir kontrolcü gerekir. Böylece bütün ilişkiler <b>1-to-n</b> olur, tasarım ve gerçekleştirme kolaylaşır.",
     "vaka"),
    ("Asansör sınıf diyagramındaki çokluklar (m kat, n asansör)?",
     "Elevator Button (<b>m·n</b>) — 1 Elevator Controller\nFloor Button (<b>2m−2</b>) — 1 Elevator Controller\nElevator Controller 1 — <b>n</b> Elevator",
     "vaka"),

    # --- CRC ---
    ("<b>CRC kartı</b> nedir? Alanları?",
     "<b>Class–Responsibility–Collaboration</b> kartı (1989'dan beri).\n"
     + ul("<b>Class:</b> sınıfın adı", "<b>Responsibility:</b> sınıfın işlevleri (ne yapar, neyi bilir)",
          "<b>Collaboration:</b> çağırdığı / birlikte çalıştığı sınıflar"),
     "tanim cikmis"),
    ("CRC kartlarının güçlü ve zayıf yanı?",
     "<b>Güçlü:</b> ekip kartları canlandırınca (act out) <b>eksik veya hatalı öğeleri</b> ortaya çıkarır → iyi bir <b>test</b> tekniği.\n"
     "<b>Zayıf:</b> entity sınıflarını bulmak için kullanılırsa <b>alan uzmanlığı</b> gerekir.",
     "cikmis"),
    ("Elevator Controller CRC kartındaki \"1. Turn on elevator button\" sorumluluğunun hatası? Doğrusu?",
     "<b>Responsibility-driven design</b> ve <b>information hiding</b> ihlali — kontrolcü düğmenin işini kendisi yapıyor.\n"
     "Doğrusu: <i>\"Send message to Elevator Button Class to turn itself on.\"</i>",
     "vaka"),
    ("CRC ile asansörde hangi unutulmuş sınıf bulundu?",
     "<b>Elevator Doors Class</b> — kapıların çalışma sırasında değişen bir durumu var (güvenlik açısından da önemli).",
     "vaka"),
    ("<b>God class</b> nedir? Çözümü?",
     "<b>Çok fazla bilgiye maruz kalan ve çok fazla kontrole sahip</b> sınıf; bilinen bir <b>antipattern</b>.\n"
     "Çözüm: <b>kontrolü dağıtmak</b> (distributed decentralized architecture)."
     + en("A god class is exposed to too much information and has too much control."),
     "tanim cikmis"),
    ("Asansörde kontrol nasıl dağıtıldı (distribute the control)?",
     "Her asansöre bir <b>Elevator Subcontroller</b>, her kata bir <b>Floor Subcontroller</b>; m+n alt kontrolcü istekleri işleyen bir <b>Scheduler</b> ile konuşur; "
     "katlardaki <b>Sensor</b>'lar asansör yaklaşınca/uzaklaşınca alt kontrolcüyü bilgilendirir.",
     "vaka cikmis"),

    # --- Statechart ---
    ("Statechart notasyonu: başlangıç, bitiş, durum, geçiş?",
     "Başlangıç: <b>dolu siyah daire</b>.\nBitiş: <b>içinde küçük siyah daire olan daire</b>.\nDurum: <b>köşeleri yuvarlatılmış dikdörtgen</b>.\nGeçiş: <b>ok</b> (üzerinde tetikleyen olay).",
     "notasyon"),
    ("MSG dinamik modelinde (statechart) bir menü seçimi neye karşılık gelir?",
     "Bir <b>olaya (event)</b>; durum geçişine yol açar. İşlem bitince sistem <i>MSG Foundation Information System Loop</i> durumuna döner; \"quit\" bitişe götürür.",
     "vaka"),

    # --- MSG ---
    ("MSG noun extraction sonucu aday entity sınıfları? Neden ortak üst sınıf eklendi?",
     "<b>Mortgage Class</b> ve <b>Investment Class</b> (report/list uzun ömürlü değil, money soyut).\n"
     "İkisine yapılan işlemler çok benzer (ekle, sil, değiştir, yazdır) → üst sınıf <b>Asset Class</b>; use case'ler <i>Manage an Asset</i>'te birleşti.",
     "vaka"),
    ("MSG'de neden <b>MSG Application Class</b> eklendi?",
     "Yıllık işletme giderlerinin (ve haftalık hesap sonucunun) saklanacağı bir sınıf yoktu.",
     "vaka"),
    ("MSG'nin boundary ve control sınıfları?",
     "Boundary: <b>User Interface Class</b> (tek ekran) + üç rapor: <b>Estimated Funds Report, Mortgages Report, Investments Report</b>.\n"
     "Control: tek hesaplama → <b>Estimate Funds for Week Class</b>.",
     "vaka"),

    # --- Use-case realization ---
    ("<b>Use-case realization</b> nedir?",
     "Use case'leri <b>genişletip inceltme</b> süreci. Bir senaryonun gerçekleştirilmesi bir <b>interaction diagram</b> (sequence ya da collaboration) ile gösterilir.",
     "tanim"),
    ("Interaction diagram'ın iki türü?",
     "<b>Sequence diagram</b> ve <b>collaboration (communication) diagram</b> — tamamen eşdeğerdir, birbirine dönüştürülebilir.",
     "tanim"),
    ("Use-case realization artifact zinciri (7 öğe)?",
     ol("Use case (diyagram)", "Use case açıklaması", "Class diagram", "Scenario", "Collaboration diagram",
        "Flow of events (collaboration'ın yazılı anlatımı)", "Sequence diagram"),
     "liste"),
    ("Çalışan bir sistem sınıfları mı nesneleri mi kullanır? Diyagramda nasıl gösterilir?",
     "<b>Nesneleri.</b> Belirli bir ipotek <code>: Mortgage Class</code> şeklinde gösterilir.",
     "notasyon"),
    ("<b>Collaboration diagram</b> nedir?",
     "Nesneleri, aralarındaki <b>bağlantıları (links)</b> ve bağlantılar üzerinde <b>gönderilme sırasına göre numaralanmış</b> mesajları gösterir. Dikey zaman ekseni yoktur."
     + en("A collaboration diagram shows the objects, the links between them and the messages numbered in the order in which they are sent."),
     "tanim cikmis"),
    ("<b>Sequence diagram</b> nedir?",
     "Nesneleri ve aralarındaki mesajları <b>zaman sırasıyla</b> (yukarıdan aşağıya) gösterir; çağrılar düz, dönüşler kesikli oktur.",
     "tanim"),
    ("Sequence mı collaboration mı? Hangisi ne zaman daha iyi?",
     "<b>Sequence:</b> mesajların akışı ve <b>sırası</b> açık; odak bilgi aktarımı ise üstün.\n<b>Collaboration:</b> sınıf diyagramına benzer; geliştiriciler <b>sınıflara</b> odaklanıyorsa kullanışlı.",
     "karsilastirma"),
    ("Analiz aşamasındaki sequence oklarına ne yazılır, sınavda ne yazmalısın?",
     "Analizde metotlar belli olmadığından açıklama (\"Request estimated return…\"). Tasarımda/sınavda <b>metot adları</b>: her ok <b>okun ucundaki sınıfın metodu</b> olmalı (parametreli).",
     "sinav_taktigi cikmis"),
    ("Estimate Funds for Week senaryosuna giren 6 sınıf ve türleri?",
     "User Interface (<b>boundary</b>), Estimate Funds for Week (<b>control</b>), Investment, Mortgage, MSG Application (<b>entity</b>), Estimated Funds Report (<b>boundary</b>).",
     "vaka"),
    ("Estimate Funds collaboration'ında 9 numaralı mesaj nedir? Özelliği?",
     "\"Compute estimated amount available for week\" — Estimate Funds for Week nesnesinin <b>kendine</b> gönderdiği mesaj (<b>self call</b>).",
     "vaka"),

    # --- Adres defteri (hocanın çözümü) ---
    ("Adres defteri: sınıflar ve türleri (hocanın kâğıdı)?",
     "<b>Kisi</b> → entity (uzun ömürlü bilgi)\n<b>Menu</b> → boundary (menü, bilgi alma)\n<b>AdresDefteri</b> → control (ekle, ara, sırala, düzenle)\n<b>Program</b> diğerlerini kullanır («uses» = dependency).",
     "cikmis senaryo_cozum"),
    ("Adres defteri: AdresDefteri ile Kisi arasındaki ilişki? Aggregation mı composition mı?",
     "Hocanın kâğıdında <b>aggregation</b> (AdresDefteri ◇— Kisi, 1–n, elmas AdresDefteri tarafında). Tahtadaki yeni sürümde <b>composition</b>.\n"
     "İkisi de geçerli; <b>gerekçeyle</b> yaz: kişiler defterle silinir → composition; bağımsız yaşar → aggregation.",
     "cikmis senaryo_cozum"),
    ("Adres defteri CRC: <b>AdresDefteri</b> kartı?",
     "<b>Responsibility:</b> kişi ekler, siler, düzenler; arama ve sıralama yapar.\n<b>Collaboration:</b> Kisi, Program.",
     "senaryo_cozum"),
    ("Adres defteri CRC: <b>Menu</b> kartı?",
     "<b>Responsibility:</b> ana menüyü gösterir; kişi ekleme bilgilerini alır; arama bilgisini alır.\n<b>Collaboration:</b> Kisi, AdresDefteri, Program.",
     "senaryo_cozum"),
    ("Kişi Ekle sequence diyagramının mesaj sırası?",
     ol("Kullanıcı → Menu: <code>eklemeIstegi()</code>", "Menu → Menu: <code>KisiBilgileriniAl()</code> (self)",
        "Menu → Kisi: «create» <code>Kisi(ad, soyad, tel, adres)</code>", "Menu → AdresDefteri: <code>Ekle(kisi)</code>",
        "AdresDefteri → AdresDefteri: <code>kaydet()</code> (boyut kontrolü)", "AdresDefteri ⇢ Menu: işlem tamam", "Menu ⇢ Kullanıcı: işlem tamam"),
     "senaryo_cozum"),
    ("2014 vizesi senaryo sorusunun dört alt sorusu (proje takip sistemi, 40 p)?",
     ol("Use case'leri oluştur", "Class yapısını oluştur, türlerini (entity/boundary/control) belirt",
        "Class'ların tasarımını oluştur", "Collaboration veya sequence diyagramı"),
     "cikmis"),
    ("Proje takip sisteminde sınıf türleri?",
     "Entity: Proje, Gorev, Calisan (ProjeYoneticisi, TakimLideri, Yazilimci).\nBoundary: ProjeEkrani, GorevEkrani, IlerlemeRaporu.\nControl: GorevAtamaKontrol, IlerlemeHesaplayici.",
     "cikmis senaryo_cozum"),

    # --- Diğer ---
    ("Unified Process neden \"use-case driven\"dır? Spesifikasyon belgesinin yerini ne alır?",
     "Use case'ler ve onlardan türeyen artifact'lar geleneksel metin spesifikasyonunun yerini alır ve aynı <b>sözleşme</b> rolünü oynar.",
     "kavram"),
    ("UP'de aktör (rol) için kullanılan terim nedir?",
     "<b>Worker</b> (ör. Applicants ve Borrowers iki ayrı worker).",
     "tanim"),
    ("OOA'nın zorlukları?",
     "OO tasarımın sınırını geçme (analizde tasarım yapma); sınıflara <b>henüz metot atama</b> (stepwise refinement sırasında yeniden dağıtmak boşa emek).",
     "kavram"),
    ("OOA'da boyut (size) metriği nedir?",
     "<b>UML diyagramlarının sayfa sayısı</b>.",
     "tanim"),
]
