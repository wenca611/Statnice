# Statnice
* název práce: Testovátor 3000
* autor: Pastušek Václav
* škola: VUT FEKT
* rok: 2021/22
* testeři: Pastušek Václav

## Upozornění:
* Lze použít i na naučení slovíček do ajiny.
* Toto neslouží jako úplné nahrazení přípravy na testy!!!
* Není vhodné pro otázky s vícero obrázky/grafy/odpovědí atd.

## Požadovaná cesta:
* ROOT - adresář se vším
* | statnine.py - jediný hlavní python skript
* | data
* | | statnice.txt - databáze
* | | OKO - soubory s obrázky, libovolná cesta se zadává do dat
* | | | jones
* | | | | 1.jpg - obrázek
* | | | | ...
* | | | ...
* | | ...

## Funguje:
* Nastavitelný multiple choice otázky s nastavitelným počtem kol.
### data:
* ignorují se prázdné řádky, 1 lexém a komenty začínající #
* pro test jsou určeny 2 a 4 lexémy
* automaticky se převede Q:A => Q:A:0:0
* jiné počty lexémů jsou chybné !!
* bere obrázky typu jpg od data\ a nakonci nedávát .jpg
* př.: imgpath = OKO\1 => data\\OKO\\1.jpg
* \[imgpath\]:\[imgpath2\]:0:0
### jiné:
* pro ukončení obrázků stiskněte v obrázku libovolnou klávesu
* feature: 
* * každý start se random někde ubere 100 bodů, může být na více místech v závislosti na logaritmu dat o základě 2
* * váhováné generování všechny body se zvednou nad 0 a transformují podle 1/(x+1)+1

## TODO list:
* jde kombinovat otázka (obrázek) a odpověď (text) nebo opačně, ale ne oboje v jedné části !!!
* možnost sdílení státnicových otázek mezi sebou a jiných testů dle předmětu
* v průběhu testování je otevřen soubor, který při terminaci programu nebo nástání chyby, kterou nechytím smaže data v statnice.txt !!!
* * řešení: překopat program a vícekrát otvírat program bez přepisu a až nakonec s přepisem (moc práce)

## otázky, doporučení, diskuze a jiné: 
* https://docs.google.com/document/d/1pS1C7GzmWBDG4wQL8p9XjimN5QFL6Xd9b8NFtWrB_Wo/edit?usp=sharing
