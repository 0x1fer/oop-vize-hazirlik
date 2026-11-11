"""Konu 3: Unified Process (Chapter 3), IEEE SPMP, süreç iyileştirme."""
from ortak import en, ipucu, ol, ul

DESTE = "03 Unified Process ve SPMP"

KARTLAR = [
    # --- UP nedir ---
    ("<b>What is the Unified Process?</b>",
     "Booch, Jacobson, Rumbaugh'un (1999) <b>nesne yönelimli yazılım geliştirme metodolojisi</b>. "
     "Bir dizi adım değildir; ürüne göre değiştirilen <b>uyarlanabilir</b> bir metodolojidir. UML kullanan bir <b>modelleme tekniğidir</b>. "
     "<b>Yinelemeli, artırımlı ve iki boyutludur</b>: 5 iş akışı (teknik bağlam) + 4 faz (iş bağlamı)."
     + en("The Unified Process is an object-oriented software development methodology. It is not a series of steps; it is an "
          "adaptable methodology that has to be modified for the specific product. It is a modeling technique (UML), iterative and "
          "incremental, and two-dimensional: five core workflows (technical context) and four phases (business context)."),
     "tanim cikmis hoca_sorar"),
    ("Unified Process hangi üç yöntemin birleşimidir?",
     "Booch'un yöntemi, Jacobson'un <b>Objectory</b>'si, Rumbaugh'un <b>OMT</b>'si. Önce RUP, sonra USDP, bugün Unified Process.",
     "tanim"),
    ("Unified Process neden \"herkese uyan tek\" bir adımlar dizisi değildir?",
     "Çok farklı türde yazılımlar vardır; tek metodoloji hepsine uymaz. UP <b>adaptable</b>'dır, ürüne göre değiştirilmelidir.",
     "kavram"),
    ("UP'nin <b>5 çekirdek iş akışı</b>?",
     ol("Requirements", "Analysis", "Design", "Implementation", "Test"),
     "liste cikmis hoca_sorar ezber"),
    ("UP'nin <b>4 fazı</b>? (sırayla)",
     ol("Inception", "Elaboration", "Construction", "Transition")
     + ipucu("Hoca: \"Fazlarını ve iş akışlarını sınavda soruyorum.\""),
     "liste cikmis hoca_sorar ezber"),
    ("Which one is NOT a phase of Unified Process?\na) Elaboration b) Construction c) Testing d) Transition e) Inception",
     "<b>c) Testing</b> — test bir <b>iş akışıdır (workflow)</b>, faz değildir.",
     "cikmis test"),
    ("<b>Workflow</b> ile <b>phase</b> farkı nedir?",
     "<b>Workflow</b> = adımın <b>teknik bağlamı</b> (technical context).\n<b>Phase</b> = adımın <b>iş/ekonomik bağlamı</b> (business context).\n"
     "UP'deki her adım hem bir iş akışına hem bir faza düşer.",
     "tanim karsilastirma"),
    ("Why do we need a <b>two-dimensional</b> model?",
     "Gerçek projeler tek seferde bitirilemeyecek kadar büyüktür; <b>Miller yasası</b> gereği iş artırımlara (fazlara) bölünür ve her artırımda "
     "iş akışları yinelenir. İki boyutlu model hem iş akışlarını hem fazları gösterir; <b>moving target</b> ve kaçınılmaz hatalarla daha iyi başa çıkar."
     + en("Real projects are too large to be completed in one pass. Because of Miller's law the task is divided into increments "
          "(phases) and within each increment the workflows are iterated. A two-dimensional model handles the moving target problem "
          "and inevitable mistakes better."),
     "cikmis kavram"),
    ("Tek boyutlu ve iki boyutlu yaşam döngüsü modellerine örnek?",
     "Tek boyutlu: <b>waterfall</b> (sadece faz ekseni).\nİki boyutlu: <b>Unified Process</b>, <b>evolution-tree</b>.",
     "karsilastirma"),
    ("UP moving target problemini ortadan kaldırır mı?",
     "Hayır. Kaçınılmaz değişiklikleri <b>ortadan kaldırmaz, etkilerini azaltır</b>. Bugüne kadarki en iyi çözümdür; gelecekte daha iyisiyle yer değiştirecektir.",
     "kavram"),

    # --- Workflows ---
    ("<b>Requirements workflow</b>'un amacı ve adımları?",
     "Amaç: müşterinin <b>ihtiyaçlarını</b> (needs) belirlemek, <i>istediklerini</i> (wants) değil.\n"
     + ol("Uygulama alanını (application domain) anla", "İş modelini (business model) kur", "Müşterinin kısıtlarını (constraints) belirle"),
     "workflow"),
    ("Requirements workflow'da belirlenen müşteri <b>kısıtları</b> (constraints)?",
     ul("Deadline (mission critical)", "Parallel running", "Portability", "Reliability", "Rapid response time",
        "Cost (müşteri bütçeyi nadiren söyler → teklif/ihale)"),
     "liste workflow"),
    ("<b>Analysis workflow</b>'un amacı? Neden requirements'tan ayrı?",
     "Gereksinimleri <b>analiz etmek ve inceltmek</b>.\nRequirements artifact'ları müşterinin anlayacağı <b>doğal dilde</b> olmalı, doğal diller belirsizdir; "
     "analysis artifact'ları tasarımcılar için <b>kesin ve tam</b> olmalıdır.",
     "workflow"),
    ("Doğal dilin belirsizliğine kitaptaki örnek? (\"A harfinin ardından Q\")",
     "\"Parça kaydı ve fabrika kaydı okunur. <i>Eğer</i> A'nın hemen ardından Q <i>içeriyorsa</i> taşıma maliyetini hesapla.\" — "
     "\"içeriyorsa\"nın öznesi belirsiz: parça kaydı mı, fabrika kaydı mı, veritabanı mı?",
     "workflow"),
    ("<b>Specification document</b> nedir? Neler içermemelidir?",
     "Müşteri ile geliştirici arasında bir <b>sözleşmedir (contract)</b>. \"Optimal\", \"%98 tamam\" gibi belirsiz ifadeler içermemeli; "
     "<b>çelişki (contradictions), eksiklik (omissions), tamamlanmamışlık (incompleteness)</b> olmamalıdır. Test ve bakım için şarttır.",
     "tanim cikmis"),
    ("SPMP (software project management plan) ne zaman hazırlanır? İçeriği (5 öğe)?",
     "Müşteri spesifikasyonu <b>imzaladıktan sonra</b> (mümkün olan en erken zaman).\n"
     + ul("Cost estimate", "Duration estimate", "Deliverables", "Milestones", "Budget"),
     "liste"),
    ("<b>Design workflow</b>'un amacı? Klasik ve OO karşılığı?",
     "Analizi programcıların gerçekleştirebileceği forma gelene kadar inceltmek. Birçok <b>nonfunctional requirement</b> burada kesinleşir (dil, reuse, portability).\n"
     "Klasik: architectural + detailed design. OO: sınıflar analizde çıkarılır, tasarımda tasarlanır.",
     "workflow"),
    ("Tasarım kararları neden saklanmalı?",
     "Çıkmaz sokağa girilince geri dönebilmek ve bakım ekibinin \"tekerleği yeniden icat etmemesi\" için.",
     "workflow"),
    ("<b>Implementation workflow</b>'un amacı?",
     "Hedef ürünü seçilen programlama dilinde gerçekleştirmek; büyük ürün alt sistemlere, onlar da bileşenlere / kod artifact'larına bölünür.",
     "workflow"),
    ("<b>Test workflow</b>: kimin sorumluluğu? Başarılı testin önemli gereksinimi?",
     "Her geliştiricinin, bakımcının ve <b>SQA grubunun</b> sorumluluğu.\nGereksinim: <b>traceability</b> — her artifact'taki her öğe bir önceki artifact'taki bir öğeye izlenebilmeli.",
     "workflow"),
    ("<b>Traceability</b> nedir?",
     "Bir artifact'taki her öğenin bir önceki artifact'taki bir öğeye izlenebilmesi (analysis → requirements, design → analysis …).",
     "tanim"),
    ("Implementation artifact'ları için 4 test türü?",
     ol("<b>Unit testing:</b> her bileşen gerçekleştirildiği anda", "<b>Integration testing:</b> her yinelemenin sonunda bileşenler birlikte",
        "<b>Product testing:</b> ürün tamamlanmış görününce bütün olarak", "<b>Acceptance testing:</b> müşterinin bilgisayarında <b>müşteri</b> tarafından"),
     "liste"),
    ("<b>Alpha release</b> ve <b>beta release</b> nedir?",
     "<b>Alpha:</b> COTS'ta geliştirme testleri sürerken olası müşterilere test için verilen sürüm.\n"
     "<b>Beta:</b> neredeyse tamamlanmış, <b>ilk işletme kalitesindeki</b> sürüm (construction fazının çıktısı).\n"
     "Alfa/beta sitesi olmanın avantajı: ürünü erken görmek; dezavantajı: hatalı yazılımla uğraşmak.",
     "tanim cikmis"),
    ("Requirements/analysis ve design artifact'ları nasıl test edilir? Fark?",
     "<b>Review</b> ile. Requirements/analysis review'unda <b>müşteri temsilcisi</b> bulunur; design review'unda genellikle bulunmaz.",
     "workflow"),
    ("Postdelivery maintenance'ta iki tür test nedir? Neden önceki testler saklanır?",
     "Yapılan değişikliğin testi + <b>regression testing</b>. Regression testing için önceki bütün test durumları ve beklenen sonuçları saklanmalıdır.",
     "kavram"),
    ("<b>Gerçek retirement</b> ne zaman olur?",
     "Müşteri kurumun, ürünün sağladığı işleve <b>artık hiç ihtiyacı kalmadığında</b>. (Yeniden yazmak aslında bakımdır; gerçek retirement nadirdir.)",
     "tanim"),

    # --- Phases ---
    ("<b>Inception phase</b>'in amacı?",
     "Önerilen ürünün <b>ekonomik olarak uygulanabilir (economically viable)</b> olup olmadığını belirlemek. Asıl çıktı: <b>ilk business case</b>.",
     "faz cikmis"),
    ("Inception fazının <b>4 adımı</b>?",
     ol("Understand the domain", "Build the business model", "Delimit the scope of the project",
        "Begin to make the initial business case"),
     "faz liste cikmis"),
    ("<b>Business case</b>'te cevaplanan sorular?",
     ul("Ürün maliyet-etkin mi?", "Yatırımın geri dönüşü ne kadar sürer?", "Geliştirmezsek maliyeti ne olur?",
        "Pazarlanacaksa pazar araştırması yapıldı mı?", "Zamanında teslim edilebilir mi? Geç kalırsa etkisi?"),
     "faz"),
    ("<b>Üç ana risk kategorisi</b>?",
     ol("<b>Technical risks</b> (ekip deneyimi, donanım zamanında gelir mi, CASE araçları)",
        "<b>The risk of not getting the requirements right</b>", "<b>The risk of not getting the architecture right</b>")
     + "Riskler sıralanır, kritik olanlar önce azaltılır.",
     "liste cikmis"),
    ("Inception fazında kodlama yapılır mı? Plan ne kadar yapılır?",
     "Genellikle kodlama yok, bazen <b>proof-of-concept prototype</b>. Tüm proje için bilgi yetmediğinden <b>yalnızca elaboration fazının planı</b> yapılır.",
     "faz"),
    ("Inception fazının çıktıları (deliverables)?",
     ul("Domain model, business model, requirements artifact'larının ilk sürümü", "Analysis artifact'ları ve mimarinin ön sürümü",
        "<b>İlk risk listesi</b>", "Use case'lerin ilk sıralaması", "Elaboration fazının planı", "<b>Business case'in ilk sürümü</b>"),
     "faz liste"),
    ("<b>Elaboration phase</b>'in amacı ve en önemli çıktısı?",
     "İlk gereksinimleri ve mimariyi <b>inceltmek</b>, riskleri izlemek, business case'i inceltmek ve <b>project management plan (SPMP)</b>'ı hazırlamak.\n"
     "Requirements neredeyse tamamlanır, analizin neredeyse tamamı yapılır, mimari tasarıma başlanır.",
     "faz cikmis"),
    ("<b>Construction phase</b>'in amacı?",
     "Ürünün <b>ilk işletme kalitesindeki (first operational-quality) sürümünü</b> = <b>beta release</b>'i üretmek. "
     "Vurgu implementation ve test'te (unit, integration, product). Çıktı: ilk kullanıcı kılavuzları.",
     "faz cikmis"),
    ("<b>Transition phase</b>'in amacı?",
     "Müşterinin gereksinimlerinin <b>gerçekten karşılandığından emin olmak</b>: hatalar düzeltilir, kılavuzlar tamamlanır, fark edilmemiş riskler aranır. "
     "Beta sitelerinden gelen <b>geri bildirimle</b> yürür.",
     "faz cikmis"),
    ("Hangi fazda hangi iş akışı ağırlıklı?",
     "Inception → Requirements\nElaboration → Requirements + Analysis\nConstruction → Implementation + Test\nTransition → Test (geri bildirim)",
     "faz karsilastirma"),
    ("Hangi fazın sonunda <b>beta release</b> çıkar? Hangi fazda SPMP hazırlanır?",
     "Beta → <b>Construction</b> sonu.\nSPMP (project management plan) → <b>Elaboration</b>.",
     "faz"),

    # --- SPMP ---
    ("IEEE SPMP'nin <b>8 ana başlığı</b>? (sırayla)",
     ol("Overview", "Reference materials", "Definitions and acronyms", "Project organization",
        "Managerial process plans", "Technical process plans", "Supporting process plans", "Additional plans")
     + ipucu("O-R-D-O-M-T-S-A. Hoca: \"genelde sınavlarda soruyorum, 1–8 ana başlıkları\"."),
     "liste cikmis hoca_sorar ezber spmp"),
    ("SPMP 1. <b>Overview</b> neyi içerir?",
     "Project summary (purpose, scope and objectives; assumptions and constraints; deliverables; schedule and budget summary) + evolution of the plan.",
     "spmp"),
    ("SPMP 4. <b>Project organization</b> neyi içerir?",
     "External interfaces, internal structure, roles and responsibilities.",
     "spmp"),
    ("SPMP 5. <b>Managerial process plans</b> neyi içerir?",
     "Start-up plan (estimation, staffing, resource acquisition, training), work plan, control plan, <b>risk management plan</b>, project close-out plan.",
     "spmp"),
    ("SPMP 6. <b>Technical process plans</b> neyi içerir?",
     "Process model; methods, tools and techniques; infrastructure plan; product acceptance plan.",
     "spmp"),
    ("SPMP 7. <b>Supporting process plans</b> neyi içerir?",
     "Configuration management, testing, documentation, quality assurance, reviews and audits, problem resolution, subcontractor management, process improvement.",
     "spmp"),
    ("SPMP'de 5. başlık nedir? 7. başlık?",
     "5 → <b>Managerial process plans</b>\n7 → <b>Supporting process plans</b>",
     "spmp ezber"),
    ("SPMP'de 3. başlık nedir? 6. başlık?",
     "3 → <b>Definitions and acronyms</b>\n6 → <b>Technical process plans</b>",
     "spmp ezber"),
    ("IEEE SPMP çerçevesi neden Unified Process için idealdir?",
     "Her tür ürün için tasarlanmıştır, belirli bir yaşam döngüsü modeli dayatmaz; <b>requirements control</b> ve <b>risk management</b> bölümleri vardır.",
     "spmp"),

    # --- Süreç iyileştirme ---
    ("SEI'ye göre yazılımdaki temel sorun nedir? Hocanın vurgusu?",
     "Sorun <b>sürecin kötü yönetilmesidir</b>. Süreç kaliteliyse ürün de kaliteli olur; belge yoksa ilerleme izlenemez, izlenemezse ölçülemez, ölçülemezse iyileştirilemez.",
     "kavram"),
    ("<b>CMM</b>'in 5 olgunluk seviyesi?",
     ol("<b>Initial</b> (ad hoc, kriz yönetimi)", "<b>Repeatable</b> (temel proje yönetimi)", "<b>Defined</b> (süreç tamamen belgelenmiş)",
        "<b>Managed</b> (nicel hedefler, ölçüm)", "<b>Optimizing</b> (sürekli süreç iyileştirme)")
     + ipucu("Hoca: okuyun ama ISO 25000 daha önemli."),
     "liste"),
    ("ISO 9000 ve ISO/IEC 15504 (SPICE) nedir?",
     "<b>ISO 9000:</b> kalite sistemleri standardı (yazılım için 9000-3).\n<b>ISO/IEC 15504 (SPICE):</b> süreç değerlendirme standardı.",
     "tanim"),
]
