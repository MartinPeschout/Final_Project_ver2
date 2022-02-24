import requests
from bs4 import BeautifulSoup
import csv
import sys


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


def ziskej_pocty():
    vytahni_udaje(url)
    volici = vytahni_udaje(url).findAll('td', {"class": "cislo"})
    return volici


def pocet_volicu():
    vytahni_udaje(url)
    pocet_volicu = ziskej_pocty()[3].get_text()
    return (pocet_volicu)


def vydane_obalky():
    vytahni_udaje(url)
    vydane_obalky = ziskej_pocty()[4].get_text()
    return vydane_obalky


def platne_hlasy():
    vytahni_udaje(url)
    platne_hlasy = ziskej_pocty()[7].get_text()
    return platne_hlasy


def ziskej_kandidujici_strany():
    strany = []
    kandidujici_strany = vytahni_udaje(url).findAll('td', {"class": "overflow_name"})
    for i in range(len(kandidujici_strany)):
        strany.append(kandidujici_strany[i].get_text())
    return strany


def ziskej_obec():
    vytahni_udaje(url)
    obec = vytahni_udaje(url).findAll('h3')
    nazev_obce = obec[2].get_text().strip('\nObec: ')
    return nazev_obce


def ziskej_kod_obce():
    vytahni_udaje(url)
    a = url
    b = a.split('/')
    c = b[5].split("=")
    kod_obce = c[3].strip('&xvyber')
    return kod_obce

def uloz_csv():
    with open(soubor, "w", newline="", encoding='utf-8') as csv_soubor:
        zahlavi = ["kod_obce", "nazev_obce", "pocet_volicu", "pocet_obalek", "pocet_platnych_hlasu", "kandidujici_strany"]
        writer = csv.DictWriter(csv_soubor, fieldnames=zahlavi)
        writer.writeheader()
        writer.writerow(
            {
                "kod_obce": ziskej_kod_obce(),
                "nazev_obce": ziskej_obec(),
                "pocet_volicu": pocet_volicu(),
                "pocet_obalek": vydane_obalky(),
                "pocet_platnych_hlasu": platne_hlasy(),
                "kandidujici_strany": ziskej_kandidujici_strany()
            }
        )