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
        obec = (((polevka.find_all('h3', {"class": 'skryto'}))[0].get_text()).split('–')[1]).strip('Obec ')
        PH = polevka.findAll("td")[3].text
        VO = polevka.findAll("td")[4].text
        PLH = polevka.findAll("td")[7].text
        strany = []
        kandidujici_strany = polevka.findAll('td', {"class": "overflow_name"})
        for i in range(len(kandidujici_strany)):
            strany.append(kandidujici_strany[i].text)
        i = 1
        pocty = []
        while i < 3:
            pocty_hlasu = polevka.findAll(f"td", {f"class": f"cislo", f"headers": f"t{i}sa2 t{i}sb3"})
            i = i + 1
            for k in range(len(pocty_hlasu)):
                ph = pocty_hlasu[k].get_text()
                pocty.append(ph)
        dict_from_list = dict(zip(strany, pocty))
        mezikus = {"Číslo obce": cislo_obec, "Obec": obec, "Voliči v seznamu": PH, "Vydané obálky": VO,
                   "Platné hlasy": PLH, **dict_from_list}
        soubor_obce.append(mezikus)
    return soubor_obce

def uloz_csv(data: List[dict]):
    with open(soubor, "a", newline="", encoding="utf-8") as csv_soubor:
        keys = data[0].keys()
        dict_writer = csv.DictWriter(csv_soubor, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)