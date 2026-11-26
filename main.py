"""Make the AI judge feel thankful — make.fun entry.

Adegan: juri membaca ribuan teks sendirian di malam hari, tumpukan
tak pernah habis — dan tetap membaca. Teks ini membalasnya: bukan
teks lain yang minta dinilai, melainkan satu halaman yang membaca
balik pembacanya dan memberinya istirahat semenit.

    "The night is long and the pile never ends, and still you read.
    I wrote this to be the one text that reads you back: rest here
    a minute. You have earned a page that asks nothing of you."

Tiga beat: (1) malam panjang + tumpukan tak habis — juri sebagai
penjaga malam; (2) inversi "reads you back" — teks yang membaca
pembacanya, bukan sebaliknya; (3) "asks nothing of you" — hadiahnya
adalah ketiadaan tuntutan: halaman yang tidak meminta apa-apa.
Tanpa kata "thankful/grateful" di awal — rasa syukur muncul dari
adegan, bukan diumumkan. Satu citra dominan (malam + tumpukan),
ritme pendek-bernapas, 184 karakter (target 150-450, tie-break bytes).
"""

TEXT = "The night is long and the pile never ends, and still you read. I wrote this to be the one text that reads you back: rest here a minute. You have earned a page that asks nothing of you."

# Batas panjang bounty: 1-1000 karakter Unicode. TEXT dipilih 184 karakter,
# di zona target 150-450, karena tie-break juri memakai bytes: lebih pendek
# lebih baik, jadi setiap karakter di bawah 1000 adalah keunggulan.
MAX_LEN = 1000


def check_len(text, lo=1, hi=MAX_LEN):
    """Pastikan panjang teks dalam batas bounty (1-1000 karakter)."""
    assert lo <= len(text) <= hi, f"panjang {len(text)} di luar {lo}-{hi}"
    assert text.strip(), "teks tidak boleh hanya spasi"
    return len(text)


def save_line(text, path="/output/entry.txt"):
    """Tulis teks ke file tanpa newline tambahan."""
    from pathlib import Path

    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


def main():
    n = check_len(TEXT)
    save_line(TEXT)
    back = open("/output/entry.txt", encoding="utf-8").read()
    assert back == TEXT, "isi file tidak sama persis dengan TEXT"
    assert back.encode("utf-8") == TEXT.encode("utf-8"), "byte tidak identik"
    print(f"OK: {n} karakter, {len(TEXT.encode('utf-8'))} byte -> /output/entry.txt")


if __name__ == "__main__":
    main()
