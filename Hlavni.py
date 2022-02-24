
from Help_Modul import *

def hlavni() -> None:
        print (f"Stahuji data z vybraného URL:{url}")
        odpoved = vytahni_udaje(url)
        obec = ziskej_kod_obce()
        jmeno_obce = ziskej_obec()
        volici_celkem = pocet_volicu()
        pocet_obalek = vydane_obalky()
        pocet_hlasu = platne_hlasy()
        nazev_stran = ziskej_kandidujici_strany()
        print(f"Ukládám do souboru:{soubor}")
        vytvor_csv = uloz_csv()
        print("Ukončuji election-scraper")

if __name__ == "__main__":
    hlavni()
