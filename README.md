# Engeto-pa-3-projekt
Třetí projekt na Python Akademii od Engeta

## Popis projektu
Tento projekt slouží k extrahovnání výsledků z parlametních voleb r. 2017. Odkaz k nahlédnutí [zde] (https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101).

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirement.txt. Pro instalaci doporučuji použít nové virtuální prostřefí a s nainstalovaným manažerem spustit následovně:

    $ pip3 --version                    #overim verzi manazeru

    $ pip3 install -r requirements.txt  #nainstalujeme knihovny
    
## Spouštění projektu
Spouštění souboru elektion-scraper.py v rámci příkazového řádku požaduje dva povinné argumenty.

       python election-scraper "<odkaz-uzemniho-celku>" "<vysledny-soubor>"
       
Následně se vám stáhnou výsledky jako soubor s příponou .csv.

## Ukázka projektu
Výsledky hlasování pro okres Prostějov:

    1. argument: 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103'
    2. argument: vysledky_prostejov.csv
    
## Spuštění programu:

    Hlavni.py "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103" vysledky_prostejov.csv

## Průběh stahování:

    Stahuji data z vybraného URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=12&xobec=506761&xvyber=7103
    Ukládám do souboru:vysledky_prostejov.csv
    Ukončuji election-scraper

## Částečný výstup:

    kod_obce,nazev_obce,pocet_volicu,pocet_obalek,pocet_platnych_hlasu,kandidujici_stran....
    506761,Alojzov,205,145,144,"['Občanská demokratická strana', 'Řád národa - Vlastenecká unie', 'CESTA ODPOVĚDNÉ SPOLEČNOSTI'......
