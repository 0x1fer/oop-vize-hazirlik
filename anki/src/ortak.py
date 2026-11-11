"""Kart yazarken kullanılan küçük HTML yardımcıları."""
import html


def kod(metin):
    """Kod bloğu: HTML kaçışlı, satır sonları <br> ile."""
    satirlar = html.escape(metin.strip("\n")).split("\n")
    return ("<pre style='text-align:left;font-size:0.85em'>"
            + "<br>".join(satirlar) + "</pre>")


def ol(*maddeler):
    return "<ol style='text-align:left'>" + "".join(f"<li>{m}</li>" for m in maddeler) + "</ol>"


def ul(*maddeler):
    return "<ul style='text-align:left'>" + "".join(f"<li>{m}</li>" for m in maddeler) + "</ul>"


def en(metin):
    """Sınava İngilizce yazılabilecek cevap kalıbı."""
    return f"<div style='text-align:left'><i>EN:</i> <i>{metin}</i></div>"


def ipucu(metin):
    return f"<div style='color:#888;font-size:0.85em'>💡 {metin}</div>"
