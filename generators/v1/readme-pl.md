#Wymagania dla *nix'ów
- python 2.7.x (https://www.python.org/downloads/)
- modul lxml  (http://lxml.de/installation.html) 
- zainstalowany Inkscape (https://inkscape.org/en/)
**UWAGA:** skrypt był pisany pod Windowsem (niestety :( ) i nie był testowany na Linuksie. Może się zdarzyć, że gdzieś błęnie przyjąłem założenie odnośnie formatu ścieżek do plików i skrypt nie będzie działał poprawnie. Poprawki mile widziane.

#Wymagania dla Windows
- Microsoft Visual C++ 2008 Redistributable Package(http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en)
- zainstalowany Inkscape (https://inkscape.org/en/)

#Jak to działa
##Definicja żetonów dla WB-95
Aby móc generować żetony musisz najpierw zdefiniować co ma na nich być. Robisz to poprzez wypełnienie arkusza opisującego żetony i zapisanie go do formatu **CSV**, który rozumie skrypt. W pliku example-wb95.ods (example-wb95.csv) definiujemy co i jak. Jedna linia definiuje jeden żeton. 
Do ustawienia mamy następujące pola:
* COUNTRY - określa jakiego kraju jest to żeton (zatem też jego kolor tła oraz grupowanie z innymi).
	Definicje kolorów dla każdego kraju ustawiamy w pliku colours.ods (colours.csv) - o tym później. Jeżeli w definicji żetonu odwołamy się do kraju którego nie ma zdefiniowanego, skrypt przestanie działać.
	Obecnie obsługiwane są:
	- RU - Związek Radziecki
	- DE - Niemcy
	- DE-SS - Niemcy SS
	- HU - Węgrzy
	- BG - Bułgaria
	- JU - Jugosławia
	- RO - Rumunia
	- UT - Utasze (Chorwaci po stronie Niemców)
* TYPE - opisuje jaki to typ jednostki, do wyboru są:
	- HQ - sztaby
	- GU - jednostka naziemna
* UNIT NAME - nazwa jednostki. Wpisujemy ciąg znaków. 
	OGRANICZENIA!:
	- dla sztabów max 12 znaków inaczej zaczynają wyjeżdżać poza krawędź żetonu
	- dla jednostek lądowych max 5 znaków (+ewentualnie kropka ".")
* UNIT NAME2 - druga linia nazwy jednostek. Działa tylko dla żetonów, które mają odpowiedni tag. W założeniu przeznaczona na nazwy radzieckich korpusów.
* ARMY-DIV - numer dywizji, armii dla jednostek lądowych, lub korpusu armii dla sztabów, do której przynależy żeton.
	OGRANICZENIA!:
	- max 3 cyfry/litery - może się trochę "rozjechać"
	- może być puste, wtedy z żetonu znika ramka z dywizją
* SIZE - wielkość jednostki. Pole ignorowane dla sztabów. Wpisujemy jedno z oznaczeń:
	- I, II, III, X, XX, XXX
* ICON1 - nazwa pliku z wzorem ikony dla żetonu (do obejrzenia w katalogu res\wb-95).
* ICON2 - nazwa pliku z alternatywnym wzorem ikony na rewersie. Działa tylko dla jednostek lądowych.
* ATTACK1 - siła ataku na awersie
* ATTACK2 - siła ataku na rewersie
* DEFENSE1 - siła obrony na awersie. Działa tylko dla plików z wzorem ikon, które mają przygotowane to pole. Dla reszty jest ignorowane.
* DEFENSE2 - j/w dla rewersu
* MOVMENT1 - ruch na awersie
* MOVMENT2 - ruch na rewersie
* WHITE STAR - ilość białych gwiazdek
* BLACK STAR - ilość czarnych gwiazdek
* YELLOW STAR - ilość żółtych gwiazdek
* BLUE STAR - ilość niebieskich gwiazdek

Sumarycznie na żetonie może być max 4 gwiazdki. Jeżeli jest więcej pozostałe zostaną zignorowane.

Po przygotowaniu pliku zapisujemy go poprzez "**File->Save a Copy**" i wybieramy format **CSV**. Jako kodowanie wybieramy **UTF-8**, reszta bez zmian.


##Definicja kolorów żetonów
W pliku colours.ods (colours.csv) definiujemy jakie chcemy żetony. Jedna linia definiuje kolory dla jednego kraju (typu żetonów). Podając kolor używamy standardowej notacji kolorów z html. Polecam strony:
 - (http://html-color-codes.info/)
 - (http://www.w3schools.com/tags/ref_colorpicker.asp)
 - (http://www.rapidtables.com/web/color/RGB_Color.htm)
 
Opis poszczególnych pól: 
* COUNTRY - określa jakiego kraju jest to żeton. Tego samego oznaczenia używamy przy definiowaniu żetonów.
* BACKGROUND - tło żetonu
* BORDER - ramka wokół żetonu oraz kolory napisów (nazwa, wielkość jednostki, współczynniki)
* DIV_BOX - kolor tła pod numerem dywizji/armii
* DIV_BOX_BORDER - kolor ramki tła pod numerem dywizji/armii
* DIV_COLOR - określa kolor numery dywizji/armii. Można podać kod koloru zgodny z html (wtedy będzie dla wszystkich żetonów danego kraju), albo **RNG** i skrypt sam "wylosuje" kolory. Za każdym uruchomieniem mogą być inne kolory, więc jak się coś nie podoba, trzeba próbować do skutku. **UWAGA:** Skrypt rozróżnia dywizje/armie po numerze, jeżeli jest "1DPanc" i "1DP" a zapiszemy ich nazwę jako "1" to dostaną ten sam kolor.
* HQ_COLOR - podobnie jak DIV_COLOR ale dla sztabów
* ATTACK_BOX - kolor tła pod siłą ataku jednostki
* DEF_BOX - kolor tła pod siłą obrony jednostki
* MOVE_BOX - kolor tła pod ilością punktów ruchu jednostki

Po przygotowaniu pliku zapisujemy go poprzez "**File->Save a Copy**" i wybieramy format **CSV**. Jako kodowanie wybieramy **UTF-8**, reszta bez zmian.

#Generowanie arkuszy
1. Odpalamy CMD
2. Przechodzimy do katalogu gdzie mamy ściągnięty generator.
3. Wykonujemy polecenie:
	`gen4.exe wb95 example-wb95.csv colours.csv`
4. Wygenerowane żetony znajdują się w pliku `<nazwa CSV>-counters-sheet-1.svg`. Na jeden arkusz mieści się 108 dwustronnych żetonów. Jeżeli generujemy więcej, zostaną utworzone pliki .svg z kolejnymi numerami.
Leniwi mogą skorzystać z plików  `gen-exmaple.bat` (albo  `gen-budapeszt1945.bat`)

#Co dalej
Możemy obejrzeć sobie plik w przeglądarce (wystarczy go przeciągnąć na zakładkę). Wszystkie współczesne (Opera, FF, Chrome, IE11) przeglądarki obsługują wyświetlanie SVG. Polecam robić oględziny żetonów w przeglądarce, jeżeli znajdziemy jakieś błędy to poprawiamy w arkuszu/csv i generujemy ponownie.

Jeżeli chcemy zrobić jakieś ręczne korekty w arkuszu to możemy użyć do tego celu programu [Inkscape](https://inkscape.org/en/). 
**UWAGA:** Jeżeli masz mniej niż 2GB RAM w komputerze - uzbrój się w cierpliwość ;)

#Drukowanie
**NIE ZALECAM DRUKOWANIA Z PRZEGLĄDARKI.** Drukowanie z przeglądarek powoduje iż traci się skale żetonów i wychodzą za małe albo za duże w stosunku do hexów na mapie. 

Najlepiej drukować prosto z [Inkscape](https://inkscape.org/en/) jeżeli nie mamy takiej możliwość polecam export z Inkscape do pdf (File->Save a copy...) i drukowanie z pdf. Również do dzielenia się swoją pracą z innymi polecam wersje w pdf, zajmują mniej miejsca.

#Dodatkowe narzędzia
W trakcie pracy nad tym projektem powstało kilka narzędzi wspomagających. Narzędzia te były pisane na szybko do uproszczenia/zautomatyzowania pewnych operacji. Mogą być niestabilne lub nie działać tak jak powinny, zatem zalecam ostrożność w ich użyciu.
##box-fixer.py
Narzędzie do masowego korygowania pewnych parametrów w szablonach żetonach. Powstało z konieczności wprowadzenia poprawek odnośnie jakiegoś elementu szablonu żetonu na masową skalę (komu by się chciało ręcznie!). Jest tylko wersja pythonowa. Ogólnie narzędzie operuje na wskazanym katalogu i tam we wszystkich plikach szuka odpowiedniego tagu a następnie przeprowadza na nim pewne zmiany, głownie ustawienie jakichś atrubutów typu kolory, ramka, fonty, etc. Zmiany jakie mają być wykonane i na jakich tagach ustawiamy zmieniajć kod skryptu. Zatem potrzeba minimum wiedzy o Pythonie oraz SVG **Nie używać jeżeli nie wie się co się robi!**. Użycie:
`python box-fixer.py target\dir`.
##colorizer.py (colorizer.exe)
Narzędzie do kopiowania palety kolorów z jednego SVG do drugiego SVG. Wymaga aby oba pliki posiadała ikonę z tagiem **ICON** z taką samą ilością ścieżek. Kolory kopiowane są 1 do 1, tzn z pierwsze ścieżki do pierwsze, drugiej do drugiej, etc. Przydaje się jak mamy ikony wytworzone na podstawie obrazków z w różnej kolorystyce a chcemy zmniejszyć pstrokatość wynikowych arkuszy. 
Użycie:  `colorizer.exe source.svg target.svg`
Plik wynikowy zapisywany jest jako `target-from-source-colorized.svg`
##gen4.py (gen4.exe)
Właściwy program do generowania arkuszy - opisany powyżej
##icon2bw.py (icon2bw.exe)
Program zmieniający ikony na białe lub czarne - dla tych, którzy wolą prostotę ;) Wymaga aby ikony na żetonach były oznaczone tagiem **ICON** i/lub **ICON2**.
Użycie: `icon2bw.exe <path_to_icon_dir> <white or black>`
Ikony lądują w katalogu `<path_to_icon_dir>\white` lub `<path_to_icon_dir>\black` w zależności od podanego parametru.
##icon-indexer.py (icon-indexer.exe)
Program do indeksowania ikon z katalogu. 
Użycie: `icon-indexer.exe scieżka\do\ikon`
Jako wynik powstają pliki SVG zawierające szablony z danego katalogu oraz nazwę pliku dla danego szablonu. Przydatne przy tworzeniu definicji żetonów jak nie pamiętamy nazw plików z szablonami.

#Tworzenie nowych szablonów:
Z grubsza:
- znajdujemy obrazek, z którego chcemy zrobić ikonę
- w Inkscape zamieniamy z bitmapy na wektorowy (zalecam użycie 8 ścieżek kolorów, bez wygładzania)
- kopiujemy pusty szablon xx-blnak.svg i zmieniamy mu nazwę na docelową
- skopiowany szablon otwieramy w Inkscape i przeklejamy poprzednio przetworzony obrazek, przy czym pamiętamy o odpowiedniej zmianie skali i ustawieniu ikony na żetonie
- z grubsza gotowe :)
