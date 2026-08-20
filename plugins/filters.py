def yesno(msg: str = ""):
    text = (msg or "").strip().lower()
    for accented, plain in (("í", "i"), ("á", "a"), ("é", "e"), ("ó", "o"), ("ú", "u")):
        text = text.replace(accented, plain)
    return text.startswith("s")


def to_number(msg: str = ""):
    text = (msg or "").strip()
    digits = "".join(ch for ch in text if ch.isdigit() or ch == "-")
    if not digits or digits == "-":
        return 0
    return int(digits)


def value(x=None):
    return x
