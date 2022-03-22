import requests
from bs4 import BeautifulSoup
from typing import List
import sys
import csv

try:
    url = sys.argv[1]
    soubor = sys.argv[2]

    if not url.startswith("https"):
        print("First must be URL adress")
        sys.exit(1)

    if not soubor.endswith(".csv"):
        print("File must be *.csv")
        sys.exit(1)

except IndexError:
        print("You did not specify a file")
        sys.exit(1)


def vytahni_udaje(url):
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

def ziskej_pravou_adr(soup):
    h = vytahni_udaje(url)
    seznam = h.find_all("td", class_="cislo")
    adr = []
    for i in seznam:
        prehled = i.find('a')['href']
        adr.append(prehled)
    return adr

def prava_adresa(adr):
    adresa = []
    for index in ziskej_pravou_adr(adr):
        adresa.append(f"https://volby.cz/pls/ps2017nss/{index}")
    return adresa

def strany_platne_hlasy(adresa):
    soubor_obce = []
    for k in adresa:
        polevka = vytahni_udaje(k)
        cislo_obec = (([a['href'] for a in polevka.find_all('a', href=True)][6]).split("&")[2]).strip("XOBEC=")
        obec = ((polevka.find_all("h3")[2].get_text()).strip()).split(" ")
        PH = polevka.findAll("td")[3].text
        VO = polevka.findAll("td")[4].text
        PLH = polevka.findAll("td")[7].text
        ODS = polevka.findAll("td")[11].text
        RN = polevka.findAll("td")[16].text
        COS = polevka.findAll("td")[21].text
        CSSD = polevka.findAll("td")[26].text
        RC = polevka.findAll("td")[31].text
        SAN = polevka.findAll("td")[36].text
        KSCM = polevka.findAll("td")[41].text
        SZ = polevka.findAll("td")[46].text
        REU = polevka.findAll("td")[51].text
        SSO = polevka.findAll("td")[56].text
        BPI = polevka.findAll("td")[61].text
        ODA = polevka.findAll("td")[66].text
        CPS = polevka.findAll("td")[71].text
        RoEU = polevka.findAll("td")[76].text
        TOP09 = polevka.findAll("td")[81].text
        ANO2011 = polevka.findAll("td")[86].text
        DV2016 = polevka.findAll("td")[91].text
        SPR = polevka.findAll("td")[96].text
        KDU= polevka.findAll("td")[101].text
        CSNS = polevka.findAll("td")[106].text
        REAL = polevka.findAll("td")[111].text
        SPORT = polevka.findAll("td")[116].text
        DSSS = polevka.findAll("td")[121].text
        OKAMURA = polevka.findAll("td")[126].text
        SPO = polevka.findAll("td")[131].text
        mezikus = {"Číslo obce": cislo_obec, "Obec": obec[1], "Voliči v seznamu": PH, "Vydané obálky": VO, "Platné hlasy": PLH,
                "Občanská demokratická strana": ODS, "Řád národa - Vlastenecká unie": RN,
                "CESTA ODPOVĚDNÉ SPOLEČNOST": COS, "Česká str.sociálně demokrat": CSSD,
                "Radostné Česko":RC, "STAROSTOVÉ A NEZÁVISLÍ": SAN, "Komunistická str.Čech a Moravy": KSCM,
                "Strana zelených": SZ,  "ROZUMNÍ-stop migraci,diktát.EU": REU, "Strana svobodných občanů": SSO,
                "Blok proti islam.-Obran.domova":BPI, "Občanská demokratická aliance": ODA, "Česká pirátská strana": CPS,
                "Referendum o Evropské unii": RoEU, "TOP 09": TOP09, "ANO 2011": ANO2011,"Dobrá volba 2016": DV2016,
                "SPR-Republ.str.Čsl. M.Sládka":SPR, "Křesť.demokr.unie-Čs.str.lid.": KDU,
                "Česká strana národně sociální":CSNS, "REALISTÉ":REAL, "SPORTOVCI": SPORT,
                "Dělnic.str.sociální spravedl.": DSSS, "Svob.a př.dem.-T.Okamura (SPD)": OKAMURA,
                "Strana Práv Občanů": SPO
                }
        soubor_obce.append(mezikus)
    return soubor_obce


def uloz_csv(data: List[dict]):
    with open(soubor, "a", newline="", encoding="utf-8") as csv_soubor:
        zahlavi = ["Cislo", "Obec", "Volici", "Obalky", "Platne_hlasy", "Občanská demokratická strana",
                   "Řád národa - Vlastenecká unie", "CESTA ODPOVĚDNÉ SPOLEČNOST", "Česká str.sociálně demokrat",
                   "Radostné Česko", "STAROSTOVÉ A NEZÁVISLÍ", "Komunistická str.Čech a Moravy",
                   "Strana zelených", "ROZUMNÍ-stop migraci,diktát.EU","Strana svobodných občanů",
                   "Blok proti islam.-Obran.domova", "Občanská demokratická aliance", "Česká pirátská strana",
                   "Referendum o Evropské unii", "TOP 09", "ANO 2011","Dobrá volba 2016", "SPR-Republ.str.Čsl. M.Sládka",
                   "Křesť.demokr.unie-Čs.str.lid.", "Česká strana národně sociální", "REALISTÉ", "SPORTOVCI",
                   "Dělnic.str.sociální spravedl.", "Svob.a př.dem.-T.Okamura (SPD)","Strana Práv Občanů"]

        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()

        for index,_ in enumerate(data):
            writer.writerow(
                {
                    "Cislo": data[index]["Číslo obce"],
                    "Obec": data[index]["Obec"],
                    "Volici": data[index]["Voliči v seznamu"],
                    "Obalky": data[index]["Vydané obálky"],
                    "Platne_hlasy": data[index]["Platné hlasy"],
                    "Občanská demokratická strana": data[index]["Občanská demokratická strana"],
                    "Řád národa - Vlastenecká unie": data[index]["Řád národa - Vlastenecká unie"],
                    "CESTA ODPOVĚDNÉ SPOLEČNOST": data[index]["CESTA ODPOVĚDNÉ SPOLEČNOST"],
                    "Česká str.sociálně demokrat": data[index]["Česká str.sociálně demokrat"],
                    "Radostné Česko": data[index]["Radostné Česko"],
                    "STAROSTOVÉ A NEZÁVISLÍ": data[index]["STAROSTOVÉ A NEZÁVISLÍ"],
                    "Komunistická str.Čech a Moravy": data[index]["Komunistická str.Čech a Moravy"],
                    "Strana zelených": data[index]["Strana zelených"],
                    "ROZUMNÍ-stop migraci,diktát.EU": data[index]["ROZUMNÍ-stop migraci,diktát.EU"],
                    "Strana svobodných občanů": data[index]["Strana svobodných občanů"],
                    "Blok proti islam.-Obran.domova": data[index]["Blok proti islam.-Obran.domova"],
                    "Občanská demokratická aliance": data[index]["Občanská demokratická aliance"],
                    "Česká pirátská strana": data[index]["Česká pirátská strana"],
                    "Referendum o Evropské unii": data[index]["Referendum o Evropské unii"],
                    "TOP 09": data[index]["TOP 09"],
                    "ANO 2011": data[index]["ANO 2011"],
                    "Dobrá volba 2016": data[index]["Dobrá volba 2016"],
                    "SPR-Republ.str.Čsl. M.Sládka": data[index]["SPR-Republ.str.Čsl. M.Sládka"],
                    "Křesť.demokr.unie-Čs.str.lid.": data[index]["Křesť.demokr.unie-Čs.str.lid."],
                    "Česká strana národně sociální": data[index]["Česká strana národně sociální"],
                    "REALISTÉ": data[index]["REALISTÉ"],
                    "SPORTOVCI": data[index]["SPORTOVCI"],
                    "Dělnic.str.sociální spravedl.": data[index]["Dělnic.str.sociální spravedl."],
                    "Svob.a př.dem.-T.Okamura (SPD)": data[index]["Svob.a př.dem.-T.Okamura (SPD)"],
                    "Strana Práv Občanů": data[index]["Strana Práv Občanů"]
                }
            )

