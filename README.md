# Testovač 3000
* popis: váhovaný multiple-choice generátor testů i s obrázky (v nové verzi)
* autor: Pastušek Václav
* škola: VUT FEKT
* rok: 2021/22
* testeři: Pastušek Václav, Petr Medek, Ondra Rýšavý

## Potřeba nainstalovat:
* Aktuálně nejlepší stáhnout jen Anacondu(odkaz níže) a ona nainstaluje Spyder
* https://www.anaconda.com/products/distribution
* Vyhledat a spustit Spyder(pokud jste stáhli Spyder bez Anacondy, tak tam nemusí fungovat pip pro instalaci!!)
* dál dole vpravo v terminálu napsat: pip install tk
* počkat na instalaci(musí tam být napsané complete)
* poté: pip install opencv-python
* počkat a už by to mělo vše, pak už jen vybrat stáhnutý python skript new_main.py a spustit
* v případě obrázků se první obrázek objeví za Spyderem, tak na něj kliknout a enterem zavřít, ostatní už se budou vytvářet před ním
* !!nejede to paralelně, takže dokud se nezavřou všechny obrázky(klávesou enterem/křížkem), tak program čeká 
* pokud chcete otvírat jiný TXT soubor, tak v kódu musíte změnit cestu FILEPATH
* V TXT datech je první číslo body, pokud chcete mít na 99.9% jen část otázek, tak změnte u nich body na -10000
*
* Ignorujte(avšak taky funguje):
* Python verze 3.8+
* https://www.python.org/downloads/
* !!pozor při instalaci Spyder bez Anacondy, bylo zaznamenáno nestandardní chování IPython terminálu!!


## BAT spuštění (Windows):
* Potřeba nainstalovat opencv-python pro novou verzi, pro starou ne (skip na bod 3):
  1) otevřít příkazový řádek (do vyhledávače napsat: cmd)
  2) spustit run_old.bat

## SH spuštění (Linux):
  1) spustit run_old.sh

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
* * +- v 25% po startu se random někde ubere 100 bodů, může být na více místech v závislosti na logaritmu dat o základě 2
* * váhováné generování lineární klesající funkce

## TODO list:
* jde kombinovat otázka (obrázek) a odpověď (text) nebo opačně, ale ne oboje v jedné části lexému !!!
* možnost sdílení státnicových otázek mezi sebou a jiných testů dle předmětu
* v průběhu testování je otevřen soubor, který při terminaci programu nebo nástání chyby, kterou nechytím smaže full data v statnice.txt !!!
* * řešení: překopat program a vícekrát otvírat program bez přepisu a až nakonec s přepisem (moc práce)
* GUI, za to mi nikdo neplatí XD
* Výběr dat z TXT, aktuálně lze obejít zakomentování zbytku, nebo změnou bodů u dat na nízká čísla (okolo -10000) a ty se budou na 99,5% vyskytovat

## YT, otázky, doporučení, diskuze a jiné:
* https://www.youtube.com/channel/UC9r0edjX9d8riV0OkaP7Cow
* https://docs.google.com/document/d/1pS1C7GzmWBDG4wQL8p9XjimN5QFL6Xd9b8NFtWrB_Wo/edit?usp=sharing