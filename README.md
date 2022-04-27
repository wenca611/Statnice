# Testovač 3000
* název práce: Testovač 3000
* autor: Pastušek Václav
* škola: VUT FEKT
* rok: 2021/22
* testeři: Pastušek Václav

## Potřeba nainstalovat:
* Python verze 3.8+
* https://www.python.org/downloads/
* nebo Spyder z Anacondy (pozor při instalaci Spyder bez Anacondy, bylo zaznamenáno nestandardní chování IPython terminálu)
* https://www.anaconda.com/products/distribution

## BAT spuštění (Windows):
* Potřeba nainstalovat opencv-python pro novou verzi, pro starou ne (skip na bod 3):
  1) otevřít příkazový řádek (do vyhledávače napsat: cmd)
  2) napsat zde: py -m pip install opencv-python
  3) spustit run.bat

## SH spuštění (Linux):
  1) spustit run.sh

## Upozornění:
* Lze použít i na naučení slovíček do ajiny.
* Toto neslouží jako úplné nahrazení přípravy na testy!!!
* Není vhodné pro otázky s vícero obrázky/grafy/odpovědí atd.

## Požadovaná cesta:
* ROOT - adresář se vším
* | new_main.py - nový hlavní python skript
* | old_main.py - starý hlavní python skript
* | run_new.sh - otevření programu pro Linux
* | run_new.bat - otevření programu pro Windows
* | run_old.sh - viz výše, ale pro starší verzi
* | run_old.bat - viz výše, ale pro starší verzi
* | data
* | | statnice.txt - databáze i s odkazy na obrázky
* | | voc.txt - anglická slovíčka
* | | OKO - soubory s obrázky, libovolná cesta se zadává do dat
* | | | jones
* | | | | 1.jpg - obrázek
* | | | | ...
* | | | ...
* | | ...
* | .gtignore - ignorování python zbytků při nahrávání na git
* | spuštění.txt - kdyby jste furt nevědeli, jak skript spustit XD
* | REDME.md - teď se na něj díváte
* | LICENSE - licence

## Funguje:
* Nastavitelný multiple choice otázky s nastavitelným počtem kol, s váhováním i eventuálně s obrázky.
### data v statnice.txt:
* ignorují se prázdné řádky, 1 lexém a komenty začínající #
* pro testování jsou určeny 2 nebo 4 lexémy
* automaticky se převede Q:A => Q:A:0:0
* jiné počty lexémů jsou chybné !! (3,5,6,...)
* bere obrázky typu jpg od data\ a nakonci nedávát .jpg
* př.: imgpath = OKO\1 => data\\OKO\\1.jpg
* vzor: \[imgpath\]:\[imgpath2\]:0:0
### jiné:
* pro ukončení obrázků stiskněte v obrázku libovolnou klávesu
* feature: 
* * +- v 10% po startu se random někde ubere 100 bodů, může být na více místech v závislosti na logaritmu dat o základě 2
* * váhováné generování všechny body se zvednou nad 0 a transformují podle 1/(x+1)+1

## TODO list:
* jde kombinovat otázka (obrázek) a odpověď (text) nebo opačně, ale ne oboje v jedné části lexému !!!
* možnost sdílení státnicových otázek mezi sebou a jiných testů dle předmětu
* v průběhu testování je otevřen soubor, který při terminaci programu nebo nástání chyby, kterou nechytím smaže full data v statnice.txt !!!
* * řešení: překopat program a vícekrát otvírat program bez přepisu a až nakonec s přepisem (moc práce)

## otázky, doporučení, diskuze a jiné: 
* https://docs.google.com/document/d/1pS1C7GzmWBDG4wQL8p9XjimN5QFL6Xd9b8NFtWrB_Wo/edit?usp=sharing
