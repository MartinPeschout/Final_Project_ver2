
from Help_Modul import *

def hlavni() -> None:
    print(f"Stahuji data z vybraného URL:{url}")

    odpoved = vytahni_udaje(url)
    ziskej_adr = ziskej_pravou_adr(odpoved)
    web_adresa = prava_adresa(ziskej_adr)
    platne_hlasy_strany = strany_platne_hlasy(web_adresa)

    print(f"Ukládám do souboru:{soubor}")
    uloz_csv(list(platne_hlasy_strany))

    print("Ukončuji election-scraper")

if __name__ == "__main__":
    hlavni()
