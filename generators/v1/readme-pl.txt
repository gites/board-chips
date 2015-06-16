Wymagania dla *nix'ów:
- python 2.7.x (https://www.python.org/downloads/)
- modul lxml  (http://lxml.de/installation.html polecam: pip install lxml)
- zainstalowany Inkscape (https://inkscape.org/en/)

Wymagania dla Windows:
- Microsoft Visual C++ 2008 Redistributable Package (jeżeli nie ma)(http://www.microsoft.com/downloads/en/details.aspx?FamilyID=9b2da534-3e03-4391-8a4d-074b9f2bc1bf&displaylang=en)
- zainstalowany Inkscape (https://inkscape.org/en/)


Jak to działa:
Definicja żetonów dla WB-95:

W pliku example-wb95.ods (example-wb95.csv) definijujemy jakie chcemy żetony. Jedna linia definiuje jeden żeton.


Do ustawinia mamy następujące pola:
COUNTRY - określa jakiego kraju jest to żeton (zatem też jego kolor tła oraz grupowanie z innymi).
	Definicje kolorów dla każdego kraju ustawiamy w pliku colours.ods (colours.csv). Jeżeli w definicji żetonu odwołamy się do kraju którego nie ma zdefiniowanego, skrypt przestanie działać.
	Obecnie obsługiwane są:
	- RU - Związek Radziecki
	- DE - Niemcy
	- DE-SS - Niemcy SS
	- HU - Węgrzy
TYPE - opisuje jaki to typ jednostki, do wyboru są:
	- HQ - sztaby
	- GU - jednostka naziemna
UNIT NAME - nazwa jednostki. Wpisujemy ciąg znaków. 
	OGRANICZENIA!:
	- dla sztabów max 12 znaków inaczej zaczynają wyjeżdżąć poza krawędź żetonu
	- dla jednostek lądowych max 5 znaków (+ewentualnie kropka ".")
UNIT NAM2 - druga linia nazwy jednostek. Działa tylko dla żetonow, które mają odpowiedni tag. W założeniu przeznaczona na nazwy radzieckich korpusów.
ARMY-DIV - numer dywizji, armii dla jednostek lądowych, lub korpusu armii dla sztabów, do której przynależy żeton.
	OGRANICZENIA!:
	- max 3 cyfry/litery - może się trochę "rozjechać"
	- może być puste, wtedy z żetonu znika ramka z dywizją
SIZE - wielkość jednostki. Pole ignorowane dla sztabów. Wpisujemy jedno z oznaczeń:
	- I, II, III, X, XX, XXX
ICON1 - nazwa pliku z wzorem ikony dla żetonu (do obejrzenia w katalogu res\wb-95 przy pomocy przeglądarki).
ICON2 - nazwa pliku z alternatywnym wzorem ikony na rewersie. Działa tylko dla jednostek lądowych.
ATACK1 - siła ataku na awersie
ATACK2 - siła ataku na rewersie
DEFENSE1 - siła obrony na awersie. Działa tylko dla plików z wzorem ikon, które mają przygotowane to pole. Dla reszty jest ignorowane.
DEFENSE2 - j/w dla rewersu
MOVMENT1 - ruch na awersie
MOVMENT2 - ruch na rewersie
WHITE STAR - ilość białych gwiazdek
BLACK STAR - ilość czarnych gwiazdek
YELLOW STAR - ilość żółtych gwiazdek
BLUE STAR - ilość niebieskich gwiazdek
	
Sumarycznie na żetonie może być max 4 gwiazdki. Jeżeli jest więcej pozostałe zostaną zignorowane.


Po przygotowaniu pliku zapisujem go poprzez "File->Save a Copy" w formacie CSV. Jako kodowanie wybieramy UTF-8, reszta bez zmian.

Definicja kolorów żetonów:

W pliku colours.ods (colours.csv) definijujemy jakie chcemy żetony. Jedna linia definiuje kolory dla jednego kraju (typu żetonów). Podająć kolor używamy standardowej notacji kolorów z html. Można użyć http://html-color-codes.info/ lub http://www.w3schools.com/tags/ref_colorpicker.asp

Opis poszczegółnych pól: 
COUNTRY - określa jakiego kraju jest to żeton. Tego samego samego oznaczenia używamy przy definiowaniu żetonów
BACKGROUND - tło żetonu
BORDER - ramka w okół żetonu oraz kolory napisów (nazwa, wielkość jednostki, współczynniki)
DIV_BOX - kolor tła pod numerem dywizji/armii
DIV_BOX_BORDER - kolor ramki tła pod pod  numerem dywizji/armii
DIV_COLOR - określa kolor numery dywizji/armi. Można podać kod koloru zgodny z html(wtedy będzie dla wszystkich żetonów danego kraju), albo RNG i skrypt sam "wylosuje" kolory. Za każdym uruchomieniem mogą być inne kolory, więc jak się coś nie podoba, trzeba próbować do skutku. Skrypt rozróżnia dywizjie/armie po numerze, jeżeli jest "1DPanc" i "1DP" a zapiszemy ich nazwę jako "1" to dostaną ten sam kolor.
ATTACK_BOX - kolor tła pod siłą ataku jednostki
DEF_BOX - kolor tła pod siłą obrony jednostki
MOVE_BOX - kolor tła pod ilością punktów ruchu jednostki

Po przygotowaniu pliku zapisujem go poprzez "File->Save a Copy" w formacie CSV. Jako kodowanie wybieramy UTF-8, reszta bez zmian.



Generowanie żetonów:

1. Odpalamy CMD
2. Przechodzimy do katalogu gdzie mamy ściągnięty generator.
3. Wykonujemy polecenie:
	gen4.exe wb95 example-wb95.csv colours.csv
4. wygenerowane zetony znajduja sie w pliku <nazewa CSV>-counters-sheet-1.svg. Na jeden arkusz mieści się 108 dwustronnych żetonów. Jeżeli generujemny więcej, zostaną utworzone pliki .svg z kolejnymi numerami.

dla leniwych:
można odpalić gen-exmaple.bat (albo  gen-budapeszt1945.bat



Co dalej:
Możemy obejrzeć sobie plik w przeglądarce (wystarczy go przeciągnąć na zakładkę). Wszystkie współczesne (Opera, FF, Chrome, IE11) przeglądarki obsługują wyświetlanie SVG. Polecam robić oględziny żetonów w przeglądarce, jeżeli znajdziemy jakieś błędy to poprawiamy w arkuszu/csv i generujemy ponownie.

Jeżeli chcemy zrobić jakieś ręczne korekty w arkuszu to możemy użyć do tego celu programu Inkscape (https://inkscape.org/en/). Jeżeli masz mniej niż 2GB RAM w komputrze - uzbrój się w cierpliwość ;)

Drukwanie:
NIE ZALECAM DRUKOWANIA Z PRZEGLĄDARKI. Drukowanie z przeglądarek powoduje iż traci się skale żetonów i wychodzą za małe albo z a duże w stosunku do hexów na mapie. 

Najlepiej drukować prosto z Inkscape (https://inkscape.org/en/) jeżeli nie mamy takiej możliwość polecam export z Inkscape do pdf (File->Save a copy...) i drukowanie z pdf. Również do dzielenia się swoją pracą z innymi polecam wersje w pdf, zajmują mniej miejsca.


