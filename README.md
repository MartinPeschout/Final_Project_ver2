# Engeto-pa-3-projekt
Třetí projekt na Python Akademii od Engeta

## Popis projektu
Tento projekt slouží k extrahovnání výsledků z parlametních voleb r. 2017. Odkaz k nahlédnutí [zde](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101).

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

    1. argument: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
    2. argument: vysledky_prostejov.csv
    
## Spuštění programu:

    Hlavni.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" vysledky_prostejov.csv

## Průběh stahování:

    Stahuji data z vybraného URL:https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103
    Ukládám do souboru:vysledky_prostejov.csv
    Ukončuji election-scraper

## Částečný výstup:

    Cislo,Obec,Volici,Obalky,Platne_hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOST,Česká str.sociálně demokrat,Radostné 
    506761,Alojzov,205,145,144,29,0,0,9,0,5,17,4,1,1,0,0,18,0,5,32,0,0,6,0,0,1,1,15,0
    589268,Bedihošť,834,527,524,51,0,0,28,1,13,123,2,2,14,1,0,34,0,6,140,0,0,26,0,0,0,0,82,1
    589276,Bílovice-Lutotín,431,279,275,13,0,0,32,0,8,40,1,0,4,0,0,30,0,3,83,0,0,22,0,0,0,1,38,0
