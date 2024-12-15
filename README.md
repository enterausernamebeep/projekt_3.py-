# projekt_3.py-
projekt_3.py - Election scraper 2017
Název: Elections scraper 2017 

Projekt 3 v rámci kurzu Engeto Python akademie 

Popis projektu

Cílem je vyextrahovat výsledky voleb do Poslanecké sněmovny Parlamentu České republiky v roce 2017
pro vybraný okres: 

https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2112 

Program výsledky "vyscrapuje" a uloží do formátu .csv.

Instalace knihoven

Knihovny je třeba nainstalovat a přenést do requirements.txt.

Spuštění projektu
V zadání je určeno, že musíme použít dva argumenty.

1. argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2112 
2. argument: rakovnik_vysledky.csv

Ukázka scrapování pro okres Rakovník:

STAHUJI DATA Z URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=565423&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=541672&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=565041&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=541699&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=565181&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=529711&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=541729&xvyber=2112
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=541737&xvyber=2112
...
STAHUJI DATA Z URL: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=2&xobec=598518&xvyber=2112
UKLÁDÁM DATA DO SOUBORU: rakovnik_vysledky.csv
UKONČUJI: C:\Users\pvrba\PycharmProjects\PythonProject10\moje_nove_prostredi\scraper.py\scraperfunguje.py


Částečný výstup:

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
565423,Bdín,51,34,34,"2,94 %","0,00 %","0,00 %","20,58 %","0,00 %","2,94 %","2,94 %","2,94 %","0,00 %","0,00 %","0,00 %","0,00 %","8,82 %","0,00 %","0,00 %","2,94 %","44,11 %","0,00 %","0,00 %","0,00 %","0,00 %","0,00 %","0,00 %","0,00 %","11,76 %","0,00 %"
541672,Branov,170,120,119,"8,40 %","0,84 %","0,00 %","11,76 %","0,00 %","0,00 %","19,32 %","0,00 %","0,84 %","0,84 %","0,00 %","0,00 %","10,92 %","0,00 %","0,00 %","1,68 %","33,61 %","0,00 %","0,00 %","4,20 %","0,00 %","0,84 %","0,00 %","0,00 %","5,88 %","0,84 %"
565041,Břežany,106,71,69,"8,69 %","0,00 %","0,00 %","5,79 %","1,44 %","5,79 %","17,39 %","0,00 %","1,44 %","1,44 %","0,00 %","0,00 %","13,04 %","0,00 %","0,00 %","2,89 %","28,98 %","0,00 %","0,00 %","0,00 %","0,00 %","0,00 %","2,89 %","0,00 %","8,69 %","1,44 %"
541699,Čistá,724,388,387,"10,85 %","0,00 %","0,00 %","8,52 %","0,00 %","6,71 %","17,31 %","1,29 %","1,80 %","0,77 %","0,00 %","0,00 %","7,75 %","0,00 %","0,00 %","2,32 %","29,45 %","0,00 %","0,00 %","4,65 %","0,00 %","0,00 %","0,25 %","0,00 %","7,49 %","0,77 %"
