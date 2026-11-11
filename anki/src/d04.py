"""Konu 4: Modüllerden nesnelere — cohesion, coupling, ADT, information hiding (Chapter 7)."""
from ortak import en, ipucu, kod, ol, ul

DESTE = "04 Cohesion ve Coupling"

KARTLAR = [
    # --- Modül ---
    ("<b>Module</b> tanımı nedir? (3 öğe)",
     "<i>A lexically contiguous sequence of program statements, bounded by boundary elements, with an aggregate identifier.</i>\n"
     + ul("<b>Lexically contiguous:</b> kodda bitişik satırlar", "<b>Boundary elements:</b> { … } / begin … end",
          "<b>Aggregate identifier:</b> modülün tamamına verilen isim"),
     "tanim cikmis"),
    ("<code>if (k) { s1; s2; } else { s3; s4; }</code> bloğu bir modül müdür?",
     "<b>Hayır.</b> Bitişik ve sınır öğeleriyle çevrili ama <b>adı (aggregate identifier) yok</b>, ismiyle çağrılamaz. Metoda konup isim verilirse modül olur.",
     "kavram"),
    ("Bir modülün üç özelliği: <b>function, logic, context</b>. \"Newton algoritmasıyla double sayıların karekökünü hesaplayan modül\" için?",
     "<b>Function</b> (ne yapar): karekök hesaplar.\n<b>Logic</b> (nasıl): Newton algoritmasıyla.\n<b>Context</b> (ne üzerinde): double precision sayılar.",
     "kavram cikmis"),
    ("Bilgisayar tasarımı örneği: kapı türüne göre çiplere bölmek (Tasarım 2) neden kötü?",
     "İşlevsel olarak eşdeğer ama: anlaşılması zor, hatanın yerini bulmak zor, genişletmesi zor, başka üründe yeniden kullanılamaz.\n"
     "Ders: <b>maximal relationships within modules, minimal relationships between modules</b>.",
     "kavram"),

    # --- Cohesion / coupling genel ---
    ("<b>Cohesion</b> nedir?",
     "Bir modülün <b>içindeki</b> etkileşimin derecesi. <b>Yüksek</b> olmalı."
     + en("Cohesion is the degree of interaction within a module."),
     "tanim cikmis hoca_sorar"),
    ("<b>Coupling</b> nedir?",
     "<b>İki modül arasındaki</b> etkileşimin derecesi. <b>Düşük</b> olmalı."
     + en("Coupling is the degree of interaction between two modules."),
     "tanim cikmis hoca_sorar"),
    ("Which one yields a <b>robust architecture</b>?\na) Loose coupling / high cohesion b) High coupling / high cohesion c) Low coupling / low cohesion d) Tight coupling e) Loose coupling / low cohesion",
     "<b>a) Loose (low) coupling / high cohesion</b>.",
     "cikmis test"),
    ("Cohesion'ın <b>7 seviyesi</b> (en kötüden en iyiye)?",
     ol("Coincidental", "Logical", "Temporal", "Procedural", "Communicational", "Functional", "Informational")
     + ipucu("\"Can Leyla Tatilde Pazar Cuma Fransa'ya İner\" — C-L-T-P-C-F-I. Ölçek doğrusal değil."),
     "liste cikmis hoca_sorar ezber"),
    ("Coupling'in <b>5 seviyesi</b> (en kötüden en iyiye)?",
     ol("Content", "Common", "Control", "Stamp", "Data")
     + ipucu("\"Cem Can Cuma Sabah Dans etti\" — C-C-C-S-D (Content, Common, Control, Stamp, Data)."),
     "liste cikmis hoca_sorar ezber"),
    ("En kötü ve en iyi cohesion? En kötü ve en iyi coupling?",
     "Cohesion: en kötü <b>coincidental</b>, en iyi <b>informational</b> (sonra functional).\nCoupling: en kötü <b>content</b>, en iyi <b>data</b>.",
     "ezber"),

    # --- Cohesion seviyeleri ---
    ("<b>Coincidental cohesion</b>: tanım, neden oluşur, neden kötü, düzeltme?",
     "Modül <b>birbiriyle tamamen ilgisiz</b> birden çok eylem yapar.\nNasıl oluşur: \"her modül 35–50 satır olsun\" gibi kurallar.\n"
     "Kötü: bakımı zor, <b>yeniden kullanılamaz</b>.\nDüzeltme: her biri tek iş yapan modüllere böl (Single Responsibility)."
     + en("The module performs multiple, completely unrelated actions."),
     "tanim cohesion"),
    ("<b>Logical cohesion</b>: tanım?",
     "Modül <b>birbiriyle ilgili</b> bir dizi eylem yapar; <b>hangisinin çalışacağını çağıran modül seçer</b> (opCode / flag / switch)."
     + en("The module performs a series of related actions, one of which is selected by the calling module."),
     "tanim cohesion cikmis"),
    ("Logical cohesion neden kötü? (3 sebep + OCP)",
     ol("<b>Arayüz anlaşılması zor</b> (hangi opCode'da hangi parametre?)", "Eylemlerin kodu <b>iç içe geçebilir</b> (intertwined)",
        "Yeniden kullanmak zor")
     + "Hoca: yeni yazıcı için <code>if (opCode == 38)</code> eklemek → <b>Open-Closed</b> ihlali.",
     "cohesion"),
    ("Logical cohesion nasıl düzeltilir?",
     "Her eylemi kendi metoduna ayır (<b>functional</b>); çağıran doğrudan ilgili metodu çağırsın. OO çözüm: ortak arayüz (ör. <code>IRapor</code>) + her durum için ayrı sınıf (<b>polymorphism</b>); yeni durum eklemek mevcut kodu değiştirmez.",
     "cohesion duzeltme"),
    ("<b>Temporal cohesion</b>: tanım, örnek, neden kötü?",
     "Modül <b>zaman açısından ilişkili</b> eylemler yapar; sadece aynı anda/art arda yapıldıkları için bir aradalar (başlatma, kapanış).\n"
     "Örnek: <i>perform_initialization</i> (dosyaları aç, tabloyu sıfırla, ilk kaydı oku).\n"
     "Kötü: eylemler birbirleriyle <b>zayıf</b>, başka modüllerdeki eylemlerle <b>güçlü</b> ilişkili; yeniden kullanılamaz."
     + en("The module performs a series of actions related in time."),
     "tanim cohesion"),
    ("Temporal cohesion nasıl düzeltilir?",
     "Her başlatma/kapanış işini ilgili sınıfa taşı (tablo başlatma → tablo sınıfının constructor'ı, dosya açma → dosya sınıfı).",
     "cohesion duzeltme"),
    ("<b>Procedural cohesion</b>: tanım ve örnek?",
     "Modül <b>ürünün izlediği prosedürle (iş akışındaki sırayla)</b> ilişkili eylemler yapar; eylemler <b>farklı veriler</b> üzerinde.\n"
     "Örnek: <i>read_part_number_and_update_repair_record_on_master_file</i>."
     + en("The module performs a series of actions related by the procedure to be followed by the product."),
     "tanim cohesion"),
    ("<b>Communicational cohesion</b>: tanım ve örnek?",
     "Procedural + <b>bütün eylemler aynı veri üzerinde</b> çalışır.\nÖrnek: <i>update_record_in_database_and_write_it_to_audit_trail</i>, "
     "<i>calculate_new_coordinates_and_send_them_to_terminal</i>."
     + en("The actions are related by the procedure of the product and all of them are performed on the same data."),
     "tanim cohesion"),
    ("Procedural ile communicational cohesion arasındaki <b>tek fark</b>?",
     "İkisinde de eylemler ürünün prosedürüne göre art arda. <b>Communicational</b>'da hepsi <b>aynı veri</b> üzerinde; procedural'da farklı veriler.",
     "karsilastirma cohesion"),
    ("Communicational cohesion neden hâlâ kötü? Hocanın Lego benzetmesi?",
     "Hâlâ birden fazla iş yapar, yeniden kullanılabilirlik düşük.\nLego: 5 birimlik Lego'yu sadece 5 birime ihtiyaç olunca kullanırsın; 1 birimlik Lego her yerde kullanılır. Modül tek iş yaptıkça yeniden kullanılabilir.",
     "cohesion"),
    ("<b>Functional cohesion</b>: tanım, örnek, avantajlar?",
     "Modül <b>tam olarak tek bir eylem</b> yapar.\nÖrnek: <i>get_temperature_of_furnace</i>, <i>calculate_sales_commission</i>.\n"
     "Avantajlar: <b>yeniden kullanılabilir</b>, hata izolasyonu (corrective bakım kolay, az regression fault), genişletmesi kolay."
     + en("The module performs exactly one action."),
     "tanim cohesion"),
    ("<b>Informational cohesion</b>: tanım?",
     "Modül bir dizi eylem yapar; <b>her eylemin kendi giriş noktası (entry point)</b> ve <b>bağımsız kodu</b> vardır ve <b>hepsi aynı veri yapısı</b> üzerinde çalışır. "
     "Özünde bir <b>abstract data type</b>; <b>sınıflar</b> informational cohesion örneğidir."
     + en("The module performs a number of actions, each with its own entry point and independent code, all performed on the same data structure."),
     "tanim cohesion"),
    ("Cohesion türünü bulma algoritması (sınavda koddan tür bulma)?",
     ol("Tek eylem mi? → <b>Functional</b>", "Ayrı giriş noktalı eylemler, aynı gizli veri (sınıf/ADT)? → <b>Informational</b>",
        "Eylemler tamamen ilgisiz mi? → <b>Coincidental</b>", "Dışarıdan gelen kod/bayrakla biri mi seçiliyor? → <b>Logical</b>",
        "Sadece aynı zamanda yapıldıkları için mi bir arada? → <b>Temporal</b>",
        "İş akışında art arda adımlar mı? Aynı veri → <b>Communicational</b>; farklı veri → <b>Procedural</b>"),
     "algoritma kod"),
    ("Cohesion/coupling sorusunda cevapta mutlaka hangi 4 şey yazılmalı?",
     ol("<b>Tür adı</b>", "<b>Gerekçe</b> (neden o tür, tanıma dayanarak)", "<b>Düzeltilmiş kod</b>", "<b>Yeni seviye</b> (\"after refactoring each method has functional cohesion\")"),
     "cikmis sinav_taktigi"),

    # --- Coupling seviyeleri ---
    ("<b>Content coupling</b>: tanım ve örnekler?",
     "Bir modül <b>diğerinin içeriğine doğrudan başvurur</b>: p, q'nun bir komutunu değiştirir; q'nun yerel verisine displacement ile erişir; "
     "q'daki bir yerel etikete dallanır (<code>goto</code>).\nKötü: q'daki neredeyse her değişiklik (yeni derleyici bile) p'yi de değiştirir."
     + en("One module directly references the contents of the other."),
     "tanim coupling"),
    ("<b>Common coupling</b>: tanım ve örnekler?",
     "İki modül <b>aynı global veriye</b> (yazma) erişimine sahip: aynı global değişken, aynı DB kaydı, FORTRAN <code>common</code>, C# <code>public static</code> alan."
     + en("Both modules have write access to the same global data."),
     "tanim coupling"),
    ("Common coupling neden kötü?",
     ul("Kod okunamaz; <b>yan etkiler</b>: modülü anlamak için global değişkeni değiştiren bütün modülleri okumak gerekir",
        "Global bildirimi değişince diğer modüller de değişmeli", "Yeniden kullanmak zor",
        "<b>Clandestine</b> common coupling: p'yi hiç değiştirmeden p ile ürün arasındaki bağ değişebilir",
        "Modül gereğinden fazla veriye maruz kalır → <b>bilgisayar suçu</b> riski"),
     "coupling"),
    ("Common coupling nasıl düzeltilir?",
     "Global değişkeni kaldır; veriyi <b>parametreyle</b> gönder (data coupling) ya da veriyi ve onu değiştiren işlemleri bir <b>sınıfa kapsülle</b> (information hiding).",
     "coupling duzeltme"),
    ("<b>Control coupling</b>: tanım?",
     "Bir modül diğerine bir <b>kontrol öğesi</b> (flag, opCode, switch) gönderir: <b>çağrılanın ne yapacağını çağıran belirler</b>. "
     "Genellikle <b>logical cohesion</b>'lı bir modüle opCode göndermekle birlikte görülür."
     + en("One module passes an element of control to the other; it explicitly controls the logic of the other."),
     "tanim coupling"),
    ("Kitaptaki ayrım: q, p'ye \"başaramadım\" derse bu veri mi kontrol mü? \"başaramadım, ABC123 hata mesajını yaz\" derse?",
     "\"Başaramadım\" → <b>veri</b>.\n\"Başaramadım, ABC123 mesajını yaz\" → <b>kontrol</b> (q, p'nin ne yapacağını belirliyor).",
     "coupling"),
    ("Control coupling neden kötü, nasıl düzeltilir?",
     "Modüller bağımsız değil: çağıran, çağrılanın iç mantığını bilmek zorunda; reuse azalır.\nDüzeltme: her görevi ayrı metot yap, çağıran doğrudan <code>Gorev3()</code>'ü çağırsın.",
     "coupling duzeltme"),
    ("<b>Stamp coupling</b>: tanım?",
     "Parametre olarak bir <b>veri yapısı</b> gönderilir ama çağrılan modül yapının <b>yalnızca bazı</b> bileşenlerini kullanır. Örnek: <i>calculate_withholding(employee_record)</i>.\n"
     "Hoca: sadece struct değil, <b>dizi</b> gönderilip bazı elemanları kullanılıyorsa da stamp."
     + en("A data structure is passed as an argument, but the called module operates on only some of the individual components."),
     "tanim coupling cikmis"),
    ("Stamp coupling neden kötü? Hocanın şifre örneği?",
     "Hangi alanların kullanıldığı modül okunmadan anlaşılmaz; reuse zor; <b>gereğinden fazla veri</b> geçer → kontrolsüz erişim, <b>bilgisayar suçu</b>.\n"
     "Hoca: \"kullanmadığı hâlde şifreyi gönderiyorsunuz, o modüle şifre yetkisi veriyorsunuz.\"",
     "coupling"),
    ("Veri yapısı göndermek her zaman stamp coupling midir?",
     "Hayır. Yapının <b>bütün</b> bileşenleri kullanılıyorsa <b>data coupling</b>'dir: <i>invert_matrix(original, inverted)</i>, <i>print_inventory_record(warehouse_record)</i>.",
     "coupling"),
    ("<b>Data coupling</b>: tanım ve örnek?",
     "Bütün parametreler <b>homojen veri öğeleri</b>: basit parametreler ya da <b>bütün elemanları kullanılan</b> veri yapıları.\n"
     "Örnek: <i>display_time_of_arrival(flight_number)</i>, <i>compute_product(a, b)</i>. Bakımı en kolay."
     + en("Every argument is either a simple argument or a data structure in which all elements are used by the called module."),
     "tanim coupling"),
    ("Coupling türünü bulma algoritması?",
     ol("Diğerinin kodunu/etiketini/yerel verisini değiştiriyor ya da içine dallanıyor mu? → <b>Content</b>",
        "Aynı global veriyi (static alan, global değişken, aynı DB kaydı) yazıp okuyorlar mı? → <b>Common</b>",
        "Gönderilen parametre ne yapılacağını belirleyen bayrak/kod mu? → <b>Control</b>",
        "Struct/kayıt/dizi gönderiliyor ama bir kısmı mı kullanılıyor? → <b>Stamp</b>",
        "Hepsi basit veri ya da tamamen kullanılan yapı mı? → <b>Data</b>"),
     "algoritma kod"),

    # --- Koddan tür bulma (sınav tipi) ---
    ("Cohesion türü?" + kod("""
void metot2(int opCode)
{
    if (opCode == 3)      PrintLocalSalesReport();
    else if (opCode == 4) PrintRegionalSalesReport();
    else if (opCode == 5) PrintNationalSalesReport();
    else                  PrintInternationalSalesReport();
}"""),
     "<b>Logical cohesion</b> — ilgili eylemlerden biri çağıranın gönderdiği <code>opCode</code> ile seçiliyor. Çağıranla arasında <b>control coupling</b>.",
     "kod cikmis test"),
    ("metot1 ile metot2 arasındaki coupling türü?" + kod("""
void metot1()
{
    int[] a = new int[10];
    for (int i = 0; i < 10; i++) a[i] = i * i;
    Console.WriteLine(metot2(a));
}
int metot2(int[] dizi) { return dizi[0] + dizi[9]; }"""),
     "<b>Stamp coupling</b> — dizi gönderiliyor ama sadece <code>dizi[0]</code> ve <code>dizi[9]</code> kullanılıyor.\nDüzeltme: <code>int metot2(int ilk, int son)</code> → data coupling.",
     "kod cikmis test"),
    ("Cohesion türü ve düzeltme? (2025–26 vizesi)" + kod("""
class Siparis
{
    public double toplamTutar;
    public void kdvekle_indirimuygula(int indirimOrani)
    {
        toplamTutar = toplamTutar - toplamTutar * indirimOrani / 100.0;
        toplamTutar = toplamTutar + toplamTutar * 0.20;
    }
}"""),
     "<b>Communicational cohesion</b>: iki eylem (indirim, KDV), prosedüre göre art arda ve <b>ikisi de aynı veri</b> (<code>toplamTutar</code>) üzerinde.\n"
     "Düzeltme: <code>private</code> alan + <code>IndirimUygula(int)</code> ve <code>KdvEkle(double)</code> ayrı metotlar → metotlar <b>functional</b>, sınıf <b>informational</b>, parametreler <b>data coupling</b>."
     + en("It has communicational cohesion because it performs two actions related by the procedure of the product and both operate on the same data."),
     "kod cikmis"),
    ("Cohesion türü? (2025–26 vizesindeki ikinci metot)" + kod("""
public void Islemler(Musteri m, double faizOrani)
{
    double faiz = faizOrani / 100;
    Console.WriteLine("Hos geldiniz " + m.Ad);
    m.Bakiye = m.Bakiye + m.Bakiye * faiz;
    LogDosyasiniAc();
}"""),
     "<b>Coincidental cohesion</b> — faiz hesabı, karşılama mesajı ve log açma birbiriyle ilgisiz (oturum başında art arda yapılıyorsa <i>temporal</i> da savunulabilir).\n"
     "Ayrıca bütün <code>Musteri</code> gönderilip sadece Ad ve Bakiye kullanıldığı için çağıranla <b>stamp coupling</b>.",
     "kod cikmis"),
    ("<code>public static double toplamTutar;</code> alanını birden çok metot okuyup yazıyorsa aralarında hangi coupling?",
     "<b>Common coupling</b> (aynı global veriye yazma erişimi).",
     "kod cikmis"),
    ("Cohesion türü?" + kod("""
void SistemKapat()
{
    log.Kapat();
    ekran.Temizle();
    yedek.Al();
}"""),
     "<b>Temporal cohesion</b> — işler birbirinden bağımsız, sadece kapanış anında art arda yapıldıkları için bir arada.",
     "kod alistirma"),
    ("Cohesion ve coupling türü?" + kod("""
void Hesapla(char islem, double a, double b)
{
    if (islem == '+') Console.WriteLine(a + b);
    else if (islem == '-') Console.WriteLine(a - b);
    else if (islem == '*') Console.WriteLine(a * b);
}"""),
     "<b>Logical cohesion</b>; çağıranla <b>control coupling</b> (<code>islem</code> kontrol öğesi). OCP ihlali.\nDüzeltme: <code>Topla(a,b)</code>, <code>Cikar</code>, <code>Carp</code> ayrı metotlar (functional + data coupling) ya da <code>IIslem</code> arayüzü.",
     "kod alistirma"),
    ("Cohesion ve coupling?" + kod("""
class Ogrenci { public string No, Ad, Soyad, Sifre; public double Ortalama; }
bool BursAlirMi(Ogrenci o) { return o.Ortalama >= 3.0; }"""),
     "<code>BursAlirMi</code> <b>functional</b>; çağıranla <b>stamp coupling</b> (bütün kayıt, şifre dahil, gidiyor; sadece Ortalama kullanılıyor).\nDüzeltme: <code>bool BursAlirMi(double ortalama)</code> → data coupling.",
     "kod alistirma"),
    ("Coupling türü?" + kod("""
static class Durum { public static bool indirimVar; }
void KampanyaBaslat() { Durum.indirimVar = true; }
double FiyatHesapla(double f) { return Durum.indirimVar ? f * 0.9 : f; }"""),
     "<b>Common coupling</b> — iki metot aynı global veriyi yazıp okuyor.\nDüzeltme: <code>FiyatHesapla(double f, double indirimOrani)</code> (data coupling) ya da bir <code>Kampanya</code> sınıfında kapsülle.",
     "kod alistirma"),
    ("Cohesion türü?" + kod("""
void NotGirVeOrtalamaGuncelle(Ogrenci o, int not)
{
    o.Notlar.Add(not);
    o.Ortalama = o.Notlar.Average();
}"""),
     "<b>Communicational cohesion</b> — iki iş, prosedürle ilişkili ve aynı veri (<code>o</code>) üzerinde.\nDaha iyisi: Ogrenci sınıfına <code>NotEkle(int)</code> ve <code>Ortalama()</code>.",
     "kod alistirma"),
    ("Cohesion türü?" + kod("""
class Kuyruk
{
    private int[] d = new int[100]; private int bas, son;
    public void Ekle(int x) { d[son++] = x; }
    public int Cikar() { return d[bas++]; }
    public bool BosMu() { return bas == son; }
}"""),
     "<b>Informational cohesion</b> — her işlemin kendi giriş noktası ve bağımsız kodu var, hepsi aynı gizli veri yapısı üzerinde (ADT). Düzeltme gerekmez.",
     "kod alistirma"),
    ("Cohesion türü?" + kod("""
void ParcaNoOkuVeTamirKaydiGuncelle()
{
    int parcaNo = int.Parse(Console.ReadLine());
    TamirKaydi k = anaDosya.Bul(parcaNo);
    k.TamirSayisi++;
    anaDosya.Guncelle(k);
}"""),
     "<b>Procedural cohesion</b> — iş akışında art arda gelen adımlar ama <b>farklı veriler</b> (parça numarası, tamir kaydı).\nDüzeltme: <code>ParcaNoOku()</code> ve <code>TamirKaydiGuncelle(int)</code>.",
     "kod alistirma"),
    ("Hocanın 2025 dersindeki kod: türler?" + kod("""
if (isDoc) UsePrinter("network");
else       UsePdfWriter(new int[] {1, 2, 3, 4, 5});

void UsePrinter(string b)  { Console.WriteLine(b); }
void UsePdfWriter(int[] a) { Console.WriteLine(a[0] + a[a.Length-1]); }
void WriteTimePrint()      { Console.WriteLine(DateTime.Now); Print(true); }"""),
     ul("<code>UsePrinter</code>, <code>UsePdfWriter</code>: <b>functional</b>",
        "<code>WriteTimePrint</code>: <b>coincidental ya da temporal</b> (hoca ikisini de kabul etti)",
        "Bayrağa göre seçen kısım: <b>logical</b>; bayrağı gönderenle <b>control coupling</b>",
        "<code>UsePdfWriter</code>'a bütün dizi, sadece ilk/son kullanılıyor → <b>stamp coupling</b>",
        "<code>UsePrinter(\"network\")</code> → <b>data coupling</b>"),
     "kod cikmis"),
    ("Hafta 5 sıcaklık örnekleri: \"edit site, time, <b>or</b> temperature field\" modülünün cohesion'ı? \"initialize sums and open files\"?",
     "edit … or … → <b>Logical</b> (birden çok işlemden biri seçiliyor).\ninitialize sums and open files → <b>Coincidental</b> (zamana bağlı görülürse temporal).",
     "cikmis ornek"),
    ("Kod: modül M1 içinde <code>goto BB;</code>, BB etiketi M2'nin içinde. Coupling?",
     "<b>Content coupling</b> — M1, M2'nin içindeki yerel etikete dallanıyor.",
     "kod"),

    # --- ADT, encapsulation, info hiding ---
    ("<b>Data encapsulation</b> nedir? İş kuyruğu örneğinde iki tasarım?",
     "Bir veri yapısı + o veri yapısı üzerinde yapılan işlemler bir arada.\nTasarım 1: kuyruk işlemleri her yere dağılmış → düşük cohesion. "
     "Tasarım 2: <code>job_queue</code> + initialize/add/delete bir modülde → <b>informational cohesion</b>.",
     "tanim"),
    ("Data encapsulation'ın geliştirme ve bakım açısından avantajı?",
     "<b>Geliştirme:</b> <b>abstraction</b> örneği — önce üst düzey kavramlarla tasarla, gerçekleştirmeyi önemseme; sonra alt düzeyi.\n"
     "<b>Bakım:</b> değişmesi muhtemel yerleri gizle; kuyruk bağlı listeye çevrilse bile kullanan modüller değişmez, sadece yeniden derlenir.",
     "kavram"),
    ("<b>Abstraction</b> nedir? (hocanın tanımı)",
     "Gereksiz ayrıntıyı gizleyip ilgili ayrıntıyı vurgulayarak problemi üst düzeyde düşünmek (stepwise refinement aracı).",
     "tanim cikmis"),
    ("<b>Abstract data type (ADT)</b> nedir?",
     "Bir <b>veri tipi</b> + o tipin örnekleri üzerinde yapılan <b>işlemler</b>. Informational cohesion'a sahip veri tipidir; <b>sınıflar ADT örneğidir</b>.",
     "tanim cikmis"),
    ("<b>Data abstraction</b> ile <b>procedural abstraction</b> farkı?",
     "<b>Data abstraction:</b> tasarımcı ADT düzeyinde düşünür.\n<b>Procedural abstraction:</b> bir prosedür tanımlamak = dili genişletmek.\nİkisi de <b>information hiding</b>'in örneğidir.",
     "karsilastirma"),
    ("<b>Information hiding</b> nedir? C#'ta nasıl sağlanır?",
     "Modülleri, <b>değişmesi muhtemel öğeler gizlenecek</b> şekilde tasarlamak; gelecekteki değişiklik yerelleşir. "
     "C#: <code>private</code> alanlar, <code>public</code> metot/property (en az yetki). Public alanlar bunu bozar."
     + en("Designing modules so that items likely to change are hidden; future change is localized."),
     "tanim cikmis"),
    ("<b>Class</b> nedir? (ADT ile ilişkisi)",
     "<b>Kalıtımı destekleyen</b> abstract data type.",
     "tanim"),
    ("<b>Polymorphism</b> ve <b>dynamic binding</b> nedir? <code>myFile.open()</code> örneği?",
     "Klasikte <i>open_disk_file</i>, <i>open_tape_file</i>… açıkça seçilir. OO'da <code>myFile.open()</code> yazılır; hangi <code>open</code>'ın çalışacağı "
     "<b>çalışma zamanında</b> nesnenin sınıfına göre belirlenir (<b>dynamic binding</b>); aynı metot farklı sınıfların nesnelerine uygulanır (<b>polymorphism</b>).",
     "tanim cikmis"),
    ("Polymorphism ve dynamic binding neden zayıf yan da olabilir?",
     "Bir metodun birden çok olası sürümü varsa kodu anlamak zorlaşır, bakım olumsuz etkilenebilir.",
     "kavram"),
    ("<b>Fragile base class problem</b> nedir?",
     "Taban sınıftaki bir değişikliğin <b>bütün alt sınıflara dalga gibi yayılması</b>. Sınıflar baştan dikkatle tasarlanmalı.",
     "tanim"),
    ("OO paradigmanın zayıf yanları?",
     ul("Geliştirme eforu/boyut büyük olabilir (özellikle GUI)", "<b>Fragile base class</b>",
        "Alt sınıflar her şeyi miras alır, şişer → \"Use inheritance where appropriate\"",
        "Polymorphism/dynamic binding sorun çıkarabilir", "Kötü OO kod yazmak çok kolay"),
     "liste"),

    # --- SOLID ---
    ("SOLID harfleri?",
     ol("<b>S</b>ingle Responsibility", "<b>O</b>pen-Closed", "<b>L</b>iskov Substitution", "<b>I</b>nterface Segregation", "<b>D</b>ependency Inversion"),
     "liste solid"),
    ("Hangi SOLID ilkesi coincidental / procedural / communicational modülleri bölmeyi söyler?",
     "<b>Single Responsibility</b>: bir modülün değişmek için tek nedeni olmalı (tek iş) → functional cohesion.",
     "solid"),
    ("Logical cohesion'da yeni durum için <code>if</code> eklemek hangi SOLID ilkesini ihlal eder?",
     "<b>Open-Closed</b>: genişletmeye açık, değişikliğe kapalı olmalı. Çözüm: arayüz + polymorphism.",
     "solid"),
    ("Interface Segregation hangi coupling türüne benzer?",
     "<b>Stamp coupling</b>'e: sınıf, kullanmadığı şeylere (büyük arayüz) bağımlı olmamalı.",
     "solid"),
]
