"""Konu destelerini Anki'nin metin içe aktarma biçimine (tab ayraçlı, HTML) çevirir ve
sitedeki flashcard sayfasının verisini üretir.

Kullanım:  python3 -I anki/src/build.py
           python3 tex/html_gen/build_html.py   (ana sayfadaki deste listesi ve sürüm ekleri için)
Çıktı:     anki/01_*.txt ... anki/08_*.txt  (Anki > Dosya > İçe Aktar)
           html/assets/kartlar-data.js      (html/kartlar.html bunu okur)
Kart metnini değiştirmek o kartın sitedeki tekrar planını sıfırlar (kimlik ön yüzden türer).
"""
import hashlib
import importlib.util
import json
import pathlib
import sys

SRC = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(SRC))  # deste dosyaları ortak.py'yi içe aktarır
OUT = SRC.parent
SITE_DATA = OUT.parent / "html" / "assets" / "kartlar-data.js"
ANA_DESTE = "OOP Vize"

# (modül, Anki dosyası, sitedeki renk ve ilgili konu sayfası; renkler konu kartlarıyla aynı)
DESTELER = [
    ("d01", "01_Kapsam_ve_Etik", "#60A5FA", "konu-01-kapsam"),
    ("d02", "02_Yasam_Dongusu_Stable_Forms", "#C084FC", "konu-02-yasam-dongusu"),
    ("d03", "03_Unified_Process_SPMP", "#F472B6", "konu-03-unified-process"),
    ("d04", "04_Cohesion_Coupling", "#2DD4BF", "konu-04-moduller"),
    ("d05", "05_ISO_25010", "#FBBF24", "konu-05-iso25010"),
    ("d06", "06_Gereksinimler_Use_Case", "#22D3EE", "konu-06-gereksinimler"),
    ("d07", "07_OO_Analiz", "#FB923C", "konu-07-oo-analiz"),
    ("d08", "08_UML", "#818CF8", "konu-08-uml"),
]


def kart_id(deste, on):
    """Ön yüzden türeyen kalıcı kimlik: sitede kartın tekrar planı bununla saklanır."""
    return hashlib.sha1(f"{deste}\n{on}".encode("utf-8")).hexdigest()[:10]


def satir(metin):
    """Kart metnini tek satırlık HTML'e çevirir (yeni satır -> <br>)."""
    metin = metin.strip("\n")
    if "\t" in metin:
        raise ValueError("Kart metninde tab olamaz: " + metin[:60])
    # Çift tırnakla başlayan alanı Anki tırnaklı CSV alanı sanar; HTML öznitelikleri tek tırnak kullanır.
    return metin.replace('"', "&quot;").replace("\n", "<br>")


def yukle(ad):
    spec = importlib.util.spec_from_file_location(ad, SRC / f"{ad}.py")
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    return modul


def main():
    toplam = 0
    site = []
    for modul_adi, dosya_adi, renk, konu in DESTELER:
        modul = yukle(modul_adi)
        deste = f"{ANA_DESTE}::{modul.DESTE}"
        on_yuzler = set()
        site_kartlar = []
        satirlar = [
            "#separator:tab",
            "#html:true",
            "#notetype:Basic",
            f"#deck:{deste}",
            "#tags column:3",
        ]
        for on, arka, etiketler in modul.KARTLAR:
            on, arka = satir(on), satir(arka)
            if on in on_yuzler:
                raise ValueError(f"{modul_adi}: aynı ön yüz iki kez: {on[:60]}")
            on_yuzler.add(on)
            satirlar.append(f"{on}\t{arka}\t{etiketler}")
            site_kartlar.append(dict(id=kart_id(modul_adi, on), f=on, b=arka, t=etiketler.split()))
        (OUT / f"{dosya_adi}.txt").write_text("\n".join(satirlar) + "\n", encoding="utf-8")
        print(f"{dosya_adi}.txt  {len(modul.KARTLAR):3d} kart  ->  {deste}")
        toplam += len(modul.KARTLAR)
        site.append(dict(id=modul_adi, no=modul_adi[1:].lstrip("0"), ad=modul.DESTE.split(" ", 1)[1],
                         renk=renk, konu=konu, kartlar=site_kartlar))
    print(f"Toplam {toplam} kart")
    SITE_DATA.write_text("window.FC_DESTELER=" + json.dumps(site, ensure_ascii=False, separators=(",", ":")) + ";\n",
                         encoding="utf-8")
    print(f"{SITE_DATA.relative_to(OUT.parent)}  ({SITE_DATA.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
