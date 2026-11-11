"""Konu 2: Yaşam döngüsü modelleri (Chapter 2) ve Stable Intermediate Forms."""
from ortak import en, ipucu, ol, ul

DESTE = "02 Yaşam Döngüsü ve Stable Intermediate Forms"

KARTLAR = [
    # --- Stable Intermediate Forms (her iki vizede çıktı) ---
    ("<b>Stable Intermediate Forms</b> — ana fikir nedir?",
     "Karmaşık bir sistem her adımda <b>kararlı (çalışan, tutarlı) ara formlardan</b> geçerek gelişirse çok daha hızlı ve güvenli gelişir. "
     "Bir değişiklik ters giderse baştan başlanmaz, <b>son kararlı forma geri dönülür</b>. Moving target problemi ve kaçınılmaz hataların etkisini azaltır."
     + en("Complex systems evolve much faster and more safely if they pass through stable intermediate forms. If a change fails "
          "we return to the last stable form instead of starting again."),
     "cikmis hoca_sorar sif"),
    ("Stable Intermediate Forms'un <b>üç yöntemi</b> nedir?",
     ol("<b>Three points of contact</b>", "<b>Copy before release</b>",
        "<b>Iterative and incremental software development</b> (stepwise refinement, snowball effect)")
     + ipucu("2024–25 ve 2025–26 vizelerinin ikisinde de çıktı (15 p). Hoca AÇIKLAMALARINI istiyor; \"terms\" değil \"forms\"."),
     "liste cikmis hoca_sorar sif ezber"),
    ("SIF 1: <b>Three points of contact</b> — açıkla.",
     "Kaya tırmanıcısı benzetmesi: dört uzvundan <b>üçü sabit</b>, yalnızca <b>biri</b> hareket eder; tutamak kayarsa sabit üç noktaya döner.\n"
     "Yazılımda: <b>aynı anda yalnızca tek bir şey değiştirilir</b>, diğer her şey sabit tutulur. Değişiklik test edilip kararlı olunca sıradakine geçilir. "
     "Olumsuz sonuçta geri dönmek kolay, hatanın kaynağı belli."
     + en("Like a climber who keeps three limbs fixed and moves only one, we change only one thing at a time and keep everything "
          "else stable. If the change fails, we can easily go back to the last stable form and we know which change caused the problem."),
     "cikmis hoca_sorar sif"),
    ("SIF 2: <b>Copy before release</b> — açıkla.",
     "Yeni sürüm yayımlanmadan / değişiklik canlıya alınmadan önce <b>mevcut kararlı sürümün kopyası (yedeği)</b> alınır. "
     "Yeni sürümde sorun çıkarsa kararlı kopyaya dönülür (rollback). Sürüm kontrolü ve <b>baseline</b> bunun uygulamasıdır."
     + en("Before releasing a new version, a copy (backup) of the current stable version is taken. If the new release causes "
          "problems, we can roll back to the stable copy. Each copy is a stable intermediate form (baseline)."),
     "cikmis hoca_sorar sif"),
    ("SIF 3: <b>Iterative and incremental software development</b> — açıkla.",
     "Ürün artırımlara (mini projeler) bölünür; her artırımda iş akışları hedefe ulaşana kadar yinelenir. "
     "Her artırımın sonunda <b>çalışan ama eksik</b> bir ürün = kararlı ara form. "
     "Önce en önemli çekirdek (<b>stepwise refinement</b>, Miller), sonra ürün kartopu gibi büyür (<b>snowball effect</b>)."
     + en("The product is divided into increments. In each increment the workflows are iterated, so at the end of every increment "
          "we have a working but incomplete product, i.e. a stable intermediate form. We start with the most important core "
          "(stepwise refinement) and grow the product like a snowball."),
     "cikmis hoca_sorar sif"),
    ("Hoca \"Stable Intermediate Forms\"u hangi slayt açıkken ve hangi problemle ilişkilendirerek anlattı?",
     "<b>Moving Target Problem</b> slaytı (Slide 2.43). SIF, moving target ve kaçınılmaz hataların etkisini azaltmanın yoludur.",
     "sif"),
    ("Snowball effect (kartopu etkisi) nedir?",
     "Önce çekirdek (en öncelikli) kısım yapılır, sonra her artırımda yeni özellikler eklenerek ürün kartopu gibi büyür.",
     "tanim sif"),

    # --- Teori vs pratik ---
    ("Gerçek dünyada yazılım neden doğrusal (linear) ve sıfırdan geliştirilemez? İki sebep.",
     ol("İnsanlar <b>hata yapar</b> (we make mistakes)", "Geliştirme sırasında <b>müşterinin gereksinimleri değişir</b> (moving target)"),
     "kavram"),

    # --- Winburg ---
    ("Winburg mini vaka çalışması: sistem ve iki gereksinim nedir?",
     "Belediye otobüslerinde yalnızca 1$ banknot kabul eden <b>ücret makinesi</b>; görüntü tanıma algoritmasıyla banknotun geçerliliğine karar verir.\n"
     "Gereksinimler: ortalama yanıt süresi <b>&lt; 1 saniye</b>, doğruluk <b>≥ %98</b>.",
     "vaka"),
    ("Winburg Episode 2: ne oldu, hata türü ne?",
     "Yanıt süresi 10 s çıktı; sebep her yerde <i>double precision</i>. Single precision yeterliydi.\n→ <b>Implementation fault</b> (corrective).",
     "vaka"),
    ("Winburg Episode 3: ne oldu, hata türü ne?",
     "Düzeltme bitse bile süre 4,5 s olacaktı; sorun karmaşık algoritma. Yeni hızlı algoritmayla <b>yeniden tasarlandı</b>.\n→ <b>Design fault</b> (corrective).",
     "vaka"),
    ("Winburg Episode 4: ne oldu, değişiklik türü ne?",
     "Belediye başkanı ürünü satmak için doğruluğun artırılmasını istedi → %99,5.\n→ <b>Gereksinim değişikliği</b> (perfective).",
     "vaka"),
    ("Winburg Epilogue: ne oldu, bakım türü ne?",
     "Birkaç yıl sonra sensörler/donanım değişti, yazılım yeniden yazıldı → <b>adaptive</b>.",
     "vaka"),
    ("<b>Evolution-tree modeli</b> waterfall'a göre neyi gösterebilir?",
     "Waterfall geri besleme oklarıyla Winburg'u gösterir ama <b>olayların sırasını gösteremez</b>. "
     "Evolution-tree her bölümde hangi artifact'ın hangi sürümünün üretildiğini ve <b>sırasını</b> gösterir. İki boyutludur.",
     "kavram"),
    ("<b>Baseline</b> nedir? Winburg Episode 3 sonundaki baseline?",
     "Belirli bir andaki artifact'ların <b>tam kümesi</b>.\nEpisode 3 sonu: Requirements₁, Analysis₁, Design₃, Implementation₃.",
     "tanim"),
    ("Winburg'un dersi nedir?",
     "<b>Değişiklik her zaman gerekir</b>: yazılım sürekli değişen gerçek dünyanın modelidir ve yazılımcılar insandır, hata yapar.",
     "kavram"),

    # --- Moving target ---
    ("<b>Moving target problem</b> nedir? Çözümü var mı?",
     "Yazılım ürünü geliştirilirken <b>gereksinimlerin değişmesi</b>. Sebep iyi olsa bile modüller arasında bağımlılıklar oluşur, "
     "regression fault'lara yol açar; çok değişiklikte ürün yeniden tasarlanır.\n<b>Çözümü yoktur</b>, sadece etkisi azaltılabilir."
     + en("A change in the requirements while the software product is being developed. There is no solution; its effects can only be minimized."),
     "tanim cikmis"),
    ("Teal Tractors vakasında moving target'a yol açan değişiklik neydi?",
     "Şirket <b>Kanada'ya genişledi</b>: yeni satış bölgeleri, Kanada vergileri ve iş kuralları, iki para birimi (USD ve CAD).",
     "vaka"),
    ("<b>Regression fault</b> nedir?",
     "Başka bir yerde yapılan değişiklik yüzünden yazılımın <b>görünüşte ilgisiz</b> bir bölümünde ortaya çıkan hata."
     + en("A fault in an apparently unrelated part of the software caused by a change made elsewhere."),
     "tanim cikmis"),
    ("Değişikliği isteyen kişinin yeterli gücü (clout) varsa moving target için ne yapılabilir?",
     "Hiçbir şey; büyüyen şirketler hep değişir. Ancak etkisi iterative-incremental model ve robust mimariyle azaltılır.",
     "kavram"),

    # --- Miller, iteration, increment ---
    ("<b>Miller's Law</b> nedir?",
     "İnsan aynı anda yaklaşık <b>yedi parça (chunk)</b> bilgiye odaklanabilir."
     + en("At any one time we can concentrate on only about seven chunks of information."),
     "tanim cikmis"),
    ("<b>Stepwise refinement</b> nedir? (3 adım)",
     ol("O an <b>en önemli</b> konulara odaklan", "Daha az kritik olanları <b>ertele</b>", "Sonunda her konu ele alınır, ama <b>önem sırasına göre</b>")
     + "Bu artırımlı (incremental) bir süreçtir.",
     "tanim liste"),
    ("<b>Iteration</b> nedir?",
     "Temel süreç yinelemelidir: <b>her ardışık sürüm hedefe bir öncekinden daha yakındır</b>. Bir artırım içinde hedefe ulaşılana kadar aynı iş akışları tekrarlanır."
     + en("Each successive version is closer to the target than its predecessor."),
     "tanim cikmis"),
    ("<b>Incrementation</b> nedir?",
     "Ürün parçalara (artırımlara) bölünür; her artırımda ürüne <b>yeni işlevler eklenir</b> (adım adım büyütme).",
     "tanim cikmis"),
    ("Iteration ve incrementation birlikte nasıl kullanılır?",
     "Tek bir \"requirements phase\" ya da \"design phase\" yoktur; her iş akışının birden çok örneği vardır. "
     "Artırım sayısı 4, yineleme sayısı 3 olmak zorunda değildir.",
     "kavram"),
    ("Beş çekirdek iş akışı (core workflows) nedir?",
     ol("Requirements", "Analysis", "Design", "Implementation", "Test")
     + "Bütün yaşam döngüsü boyunca yürütülür; başta requirements, sonda implementation ve test baskındır.",
     "liste"),
    ("İterative-incremental modelde \"her yineleme\" neye benzetilir? Yönetimi neden disiplinlidir?",
     "Her yineleme <b>küçük ama tam bir waterfall modelidir</b>; model art arda uygulanan waterfall olduğu için waterfall kadar disiplinlidir.",
     "kavram"),
    ("Iterative-incremental modelin <b>5 güçlü yanı</b>?",
     ol("Doğruluğu kontrol için <b>birçok fırsat</b>; hatalar erken bulunur",
        "Mimarinin <b>robustness</b>'ı yaşam döngüsünün başında belirlenir",
        "<b>Riskler erken azaltılır</b> (mitigate)",
        "Baştan itibaren <b>çalışan bir sürüm</b> vardır; müşteri geri bildirimi erken",
        "<b>Deneysel kanıt</b>: Standish CHAOS raporlarında başarı oranı arttı"),
     "liste cikmis"),
    ("<b>Architecture</b> ve <b>robustness</b> tanımları?",
     "<b>Architecture:</b> bileşen modüller ve birbirine nasıl oturdukları.\n"
     "<b>Robustness:</b> dağılmadan genişlemeyi ve değişikliği kaldırabilme özelliği.",
     "tanim"),
    ("Winburg, iterative-incremental modelin üstüne oturtulunca bölümler neye karşılık gelir?",
     "Her bölüm (episode) bir <b>artırıma</b>; her artırım her iş akışını içermek zorunda değil. Episode 2–3 corrective, Episode 4 perfective bakım.",
     "vaka"),

    # --- Diğer modeller ---
    ("<b>Code-and-fix</b> modeli nedir?",
     "Tasarım/spesifikasyon olmadan kodla, sonra düzelt. Küçük programlar dışında kötüdür.",
     "model"),
    ("<b>Rapid prototyping</b> modeli nedir?",
     "Müşteriye hızlıca bir prototip gösterip gereksinimleri netleştirme; prototip sonra atılır.",
     "model"),
    ("<b>Spiral</b> modelin odağı nedir?",
     "Her döngüde <b>risk analizi</b>; odak risklerdir.",
     "model"),
    ("<b>Synchronize-and-stabilize</b> modeli kimin modelidir, özelliği?",
     "<b>Microsoft</b> modeli; her gün bileşenler birleştirilip test edilir (daily build).",
     "model"),
    ("<b>Agile processes</b> özü?",
     "Kısa iterasyonlar, sürekli müşteri teması.",
     "model"),
]
