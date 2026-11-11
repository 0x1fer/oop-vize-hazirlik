"""Konu 5: ISO/IEC 25010 (2023) yazılım ürün kalitesi modeli.

İlk iki bölüm, klasördeki ISO25010_anki.txt ile aynı ön yüzleri üretir; daha önce içe
aktarıldıysa Anki bu notları yinelemez, günceller.
"""
from ortak import ipucu, ol, ul

DESTE = "05 ISO 25010"

TABLO = [
    ("Functional Suitability", ["Functional completeness", "Functional correctness", "Functional appropriateness"]),
    ("Performance Efficiency", ["Time behaviour", "Resource utilization", "Capacity"]),
    ("Compatibility", ["Co-existence", "Interoperability"]),
    ("Interaction Capability", ["Appropriateness recognizability", "Learnability", "Operability", "User error protection",
                                "User engagement", "Inclusivity", "User assistance", "Self-descriptiveness"]),
    ("Reliability", ["Faultlessness", "Availability", "Fault tolerance", "Recoverability"]),
    ("Security", ["Confidentiality", "Integrity", "Non-repudiation", "Accountability", "Authenticity", "Resistance"]),
    ("Maintainability", ["Modularity", "Reusability", "Analysability", "Modifiability", "Testability"]),
    ("Flexibility", ["Adaptability", "Scalability", "Installability", "Replaceability"]),
    ("Safety", ["Operational constraint", "Risk identification", "Fail safe", "Hazard warning", "Safe integration"]),
]

ANLAM = {
    "Functional completeness": "İşlevler belirtilen bütün görevleri ve kullanıcı hedeflerini kapsıyor mu?",
    "Functional correctness": "Doğru sonuçları gereken hassasiyetle üretiyor mu?",
    "Functional appropriateness": "İşlevler görevlerin yerine getirilmesini kolaylaştırıyor mu?",
    "Time behaviour": "Yanıt ve işlem süreleri, verim (throughput) gereksinimleri karşılıyor mu?",
    "Resource utilization": "Kullanılan kaynak (bellek, CPU) miktarı ve türü.",
    "Capacity": "Bir parametrenin üst sınırları (eşzamanlı kullanıcı, kayıt sayısı).",
    "Co-existence": "Ortak ortam ve kaynakları başka ürünlerle zarar vermeden paylaşabilme.",
    "Interoperability": "İki veya daha fazla sistemin bilgi alışverişi yapıp bu bilgiyi kullanabilmesi (hoca: e-Devlet ile kimlik doğrulama).",
    "Appropriateness recognizability": "Kullanıcı ürünün ihtiyacına uygun olup olmadığını anlayabiliyor mu?",
    "Learnability": "Kullanmayı öğrenme kolaylığı.",
    "Operability": "Kullanma ve kontrol etme kolaylığı.",
    "User error protection": "Kullanıcıyı hata yapmaktan koruma (hoca: numara kutusuna harf yazdırmamak; ilk düğmeye basılmadan ikinciyi pasif tutmak).",
    "User engagement": "Hoş, ilgi çekici, motive edici etkileşim (2011'de UI aesthetics).",
    "Inclusivity": "Farklı özellik ve yeteneklerdeki insanların kullanabilmesi (2011'de Accessibility).",
    "User assistance": "Kullanıcıya yardım ve destek (yardım menüsü, ipuçları).",
    "Self-descriptiveness": "Ürünün kendini açıklaması; ekranın ne yapılacağını kendiliğinden göstermesi.",
    "Faultlessness": "Normal çalışmada hatasız işleme (2011'de Maturity).",
    "Availability": "Gerektiğinde çalışır ve erişilebilir olma.",
    "Fault tolerance": "Donanım/yazılım hatalarına rağmen amaçlandığı gibi çalışma.",
    "Recoverability": "Kesinti/arıza sonrası veriyi kurtarıp istenen duruma dönebilme.",
    "Confidentiality": "Veriye yalnızca yetkililerin erişmesi.",
    "Integrity": "Program veya verinin yetkisiz erişim/değişikliğe karşı korunması.",
    "Non-repudiation": "Eylem/olayların gerçekleştiğinin kanıtlanabilmesi, sonradan inkâr edilememesi.",
    "Accountability": "Bir varlığın eylemlerinin tekil olarak o varlığa izlenebilmesi.",
    "Authenticity": "Bir özne veya kaynağın kimliğinin iddia edildiği gibi olduğunun kanıtlanması.",
    "Resistance": "Saldırılara karşı direnç (2023'te eklendi).",
    "Modularity": "Bir bileşendeki değişikliğin diğerlerini en az etkileyecek şekilde ayrık bileşenlerden oluşma.",
    "Reusability": "Bir varlığın birden fazla sistemde kullanılabilmesi.",
    "Analysability": "Değişikliğin etkisini değerlendirme, hata nedenini bulma, değişecek parçayı belirleme kolaylığı.",
    "Modifiability": "Hata eklemeden, kaliteyi düşürmeden değiştirilebilme.",
    "Testability": "Test kriterleri konup testlerin yapılabilmesi.",
    "Adaptability": "Farklı veya gelişen donanım, yazılım, ortama uyarlanabilme.",
    "Scalability": "Artan/azalan iş yüküne göre ölçeklenebilme (2023'te eklendi).",
    "Installability": "Belirli ortamda başarıyla kurulabilme / kaldırılabilme.",
    "Replaceability": "Aynı ortamda aynı amaçla başka bir ürünün yerine geçebilme.",
    "Operational constraint": "Güvenli çalışma sınırları içinde kalma.",
    "Risk identification": "Riskleri belirleyebilme.",
    "Fail safe": "Arıza anında kendini güvenli moda alma.",
    "Hazard warning": "Tehlike durumunda uyarı verme.",
    "Safe integration": "Başka bileşenlerle güvenli bütünleşme.",
}

KARAKTERISTIK_ANLAM = {
    "Functional Suitability": "Ürün belirtilmiş ve örtük ihtiyaçları karşılayan işlevleri sağlıyor mu?",
    "Performance Efficiency": "Kullanılan kaynağa göre performans.",
    "Compatibility": "Başka ürünlerle bilgi alışverişi yapabilme / aynı ortamı paylaşabilme.",
    "Interaction Capability": "Belirli kullanıcıların ürünle etkileşebilme derecesi (2011'de Usability).",
    "Reliability": "Belirtilen koşullarda, belirtilen süre boyunca belirtilen işlevleri yerine getirme.",
    "Security": "Bilgi ve veriyi yetki düzeyine uygun şekilde koruma.",
    "Maintainability": "İyileştirmek, düzeltmek, uyarlamak için etkin biçimde değiştirilebilme.",
    "Flexibility": "Gereksinim, kullanım bağlamı ya da ortam değişikliklerine uyum (2011'de Portability).",
    "Safety": "İnsan hayatı, sağlık, mülk ve çevre için tehlike yaratmama (2023'te yeni).",
}

KARTLAR = []

# 1) Karakteristik -> alt karakteristikler (ISO25010_anki.txt ile aynı)
for i, (k, altlar) in enumerate(TABLO, 1):
    KARTLAR.append((f"<b>{k}</b>\nAlt karakteristikleri nelerdir? ({len(altlar)})",
                    "\n".join(f"{j}. {a}" for j, a in enumerate(altlar, 1)),
                    "karakteristik->alt"))

# 2) Alt karakteristik -> karakteristik (ISO25010_anki.txt ile aynı)
for i, (k, altlar) in enumerate(TABLO, 1):
    for a in altlar:
        KARTLAR.append((f"<b>{a}</b>\nHangi karakteristiğe aittir?", f"{i}. {k}", "alt->karakteristik"))

# 3) Alt karakteristiğin anlamı
for i, (k, altlar) in enumerate(TABLO, 1):
    for a in altlar:
        KARTLAR.append((f"ISO 25010: <b>{a}</b> ne anlama gelir?",
                        f"{ANLAM[a]}\n<span style='color:#888'>({k})</span>", "anlam"))

# 4) Karakteristiğin anlamı
for k, anlam in KARAKTERISTIK_ANLAM.items():
    KARTLAR.append((f"ISO 25010 karakteristiği <b>{k}</b> neyi ölçer?", anlam, "anlam karakteristik"))

KARTLAR += [
    ("ISO/IEC 25010 (2023) <b>9 ana karakteristiğini</b> sırayla yaz.",
     ol(*[k for k, _ in TABLO])
     + ipucu("FP-CIR-SMFS: \"Fonksiyonel Performans, Cihazlar İletişimde Rahat; Sistem Mutlaka Fazla Sağlam\". Toplam 40 alt karakteristik."),
     "liste cikmis hoca_sorar ezber"),
    ("2025–26 vizesinde ISO sorusu nasıl puanlandı? Kaç alt başlık yazmalısın?",
     "18 puan: <b>ana başlık 1'er</b>, <b>alt başlık 0,5'er</b>. 9×1 + 18×0,5 = 18 → her ana başlıktan <b>en az 2</b> alt başlık. "
     "2024–25'te tablonun tamamı istendi. Güvenli olan: hepsini yaz. Açıklama istenmiyor, maddeler yeterli.",
     "cikmis sinav_taktigi"),
    ("Which one is NOT an ISO/IEC 25010 quality characteristic?\na) Reliability b) Portability c) Compatibility d) Comprehensibility e) Security",
     "<b>d) Comprehensibility</b>. (Portability 2011 sürümünde vardı; 2023'te Flexibility oldu.)",
     "cikmis test"),
    ("ISO 25000 serisinin adı (SQuaRE açılımı)? ISO 25010 neyi tanımlar?",
     "<b>SQuaRE</b>: Systems and software Quality Requirements and Evaluation.\n25010 → <b>kalite modelini</b>: ürün değerlendirilirken hangi kalite karakteristiklerinin dikkate alınacağını.",
     "tanim"),
    ("Bir sistemin <b>kalitesi</b> nedir? (ISO 25010)",
     "Sistemin, paydaşlarının <b>belirtilmiş ve örtük ihtiyaçlarını</b> karşılama derecesi.",
     "tanim"),
    ("Hocanın vurgusu: ISO 25010 karakteristikleri bir yazılımın ne yaptığını mı söyler?",
     "Hayır; <b>dokümanlarda nelerin tanımlanması gerektiğini</b> söyler. Ör. yanıt süresinin düşük/yüksek olması değil, <b>belgelerde tanımlanmış olması</b> önemlidir — "
     "tanımlıysa izlenebilir, ölçülebilir, iyileştirilebilir.",
     "kavram"),
    ("2011 sürümünde kaç karakteristik / alt karakteristik vardı? 2023'te?",
     "2011: <b>8</b> karakteristik, <b>31</b> alt.\n2023: <b>9</b> karakteristik, <b>40</b> alt.",
     "sayi karsilastirma"),
    ("2011 → 2023 <b>isim değişiklikleri</b> (karakteristik düzeyinde)?",
     ul("<b>Usability → Interaction Capability</b>", "<b>Portability → Flexibility</b>", "Yeni karakteristik: <b>Safety</b>"),
     "karsilastirma"),
    ("2011 → 2023 <b>alt karakteristik</b> değişiklikleri?",
     ul("UI aesthetics → <b>User engagement</b>", "Accessibility → <b>Inclusivity</b>",
        "Yeni: <b>User assistance</b>, <b>Self-descriptiveness</b>", "Maturity → <b>Faultlessness</b>",
        "Security'ye yeni: <b>Resistance</b>", "Flexibility'ye yeni: <b>Scalability</b>"),
     "karsilastirma"),
    ("ISO 25010'da en çok alt karakteristiği olan karakteristik hangisi? En az olan?",
     "En çok: <b>Interaction Capability (8)</b>.\nEn az: <b>Compatibility (2)</b>.",
     "sayi ezber"),
    ("Alt karakteristik sayılarını sırayla söyle (FS, PE, C, IC, R, Sec, M, F, Saf).",
     "3 – 3 – 2 – 8 – 4 – 6 – 5 – 4 – 5 = <b>40</b>",
     "sayi ezber"),
    ("Hem 2011 hem 2023'te aynı kalan, sınavda \"güvenli\" alt başlıklara örnek?",
     "Time behaviour, Co-existence, Interoperability, Learnability, Operability, Availability, Fault tolerance, Confidentiality, Integrity, Modularity, Testability, Installability, Adaptability…",
     "sinav_taktigi"),
    ("Security'nin alt başlıklarını hatırlama ipucu?",
     "Confidentiality, Integrity (CIA'ya benzer) + Non-repudiation, Accountability, Authenticity, Resistance — "
     "\"inkâr edemezsin, hesabını verirsin, kim olduğunu kanıtlarsın, saldırıya dayanırsın\".",
     "ezber"),
    ("Reliability'nin alt başlıklarını hatırlama ipucu?",
     "Hata olmasın (<b>faultlessness</b>), erişilebilsin (<b>availability</b>), hataya rağmen çalışsın (<b>fault tolerance</b>), sonra toparlansın (<b>recoverability</b>).",
     "ezber"),
    ("Senaryo: Sistem, sunuculardan biri çökse bile çalışmaya devam ediyor. Hangi alt karakteristik?",
     "<b>Fault tolerance</b> (Reliability).",
     "senaryo"),
    ("Senaryo: Kullanıcı, kendisinin yaptığı para transferini inkâr edemiyor çünkü işlem kaydı ve imza var. Hangi alt karakteristik?",
     "<b>Non-repudiation</b> (Security).",
     "senaryo"),
    ("Senaryo: Uygulama, e-Devlet ile kimlik bilgisi alışverişi yapıp kullanabiliyor. Hangi alt karakteristik?",
     "<b>Interoperability</b> (Compatibility).",
     "senaryo"),
    ("Senaryo: Kampanya günü kullanıcı sayısı 10 katına çıkınca sistem ek sunucularla yükü karşılıyor. Hangi alt karakteristik?",
     "<b>Scalability</b> (Flexibility).",
     "senaryo"),
    ("Senaryo: Form, telefon alanına harf girilmesine izin vermiyor. Hangi alt karakteristik?",
     "<b>User error protection</b> (Interaction Capability).",
     "senaryo"),
    ("Senaryo: Görme engelli kullanıcılar ekran okuyucuyla uygulamayı kullanabiliyor. Hangi alt karakteristik?",
     "<b>Inclusivity</b> (Interaction Capability; 2011'de Accessibility).",
     "senaryo"),
    ("Senaryo: Bir modülde değişiklik yapınca diğer modüller etkilenmiyor. Hangi alt karakteristik?",
     "<b>Modularity</b> (Maintainability).",
     "senaryo"),
    ("Senaryo: Elektrik kesintisinden sonra sistem 2 dakikada verileriyle birlikte eski durumuna dönüyor. Hangi alt karakteristik?",
     "<b>Recoverability</b> (Reliability).",
     "senaryo"),
    ("Senaryo: Tıbbi cihaz yazılımı arıza algılayınca dozu kesip güvenli moda geçiyor. Hangi alt karakteristik?",
     "<b>Fail safe</b> (Safety).",
     "senaryo"),
    ("Senaryo: Hasta kayıtlarını yalnızca yetkili doktorlar görebiliyor. Hangi alt karakteristik?",
     "<b>Confidentiality</b> (Security).",
     "senaryo"),
]
