




Wymagania:
- python 2.7.x (https://www.python.org/downloads/)
- modul lxml  (http://lxml.de/installation.html polecam: pip install lxml)


Jak to działa:
Definicja żetonów dla WB-95:

W pliku example-wb95.ods definijujemy jakie chcemy żetony. Jedna linia definiuje jeden żeton.
Do ustawinia mamy następujące pola:
COUNTRY - określa jakiego kraju jest to żeton (zatem też jego kolor tła oraz grupowanie z innymi).
	Obecnie obsługiwane są:
	- RU - Związek Radziecki
	- DE - Niemcy
	- DE-SS - Niemcy SS
TYPE - opisuje jaki to typ jednostki, do wyboru są:
	- HQ - sztaby
	- GU - jednostka naziemna
UNIT NAME - nazwa jednostki. Wpisujemy ciąg znaków. 
	OGRANICZENIA!:
	- dla sztabów max 12 znaków inaczej zaczynają wyjeżdżąć poza krawędź żetonu
	- dla jednostek lądowych max 5 znaków (+ewentualnie kropka ".")
ARMY-DIV - numer dywizji, armii dla jednostek lądowych, lub korpusu armii dla sztabów, do której przynależy żeton.
	OGRANICZENIA!:
	- max 3 cyfry/litery - może się trochę "rozjechać"
	- może być puste
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


Po przygotowaniu pliku zapisujem go File->Save a Copy w formacie CSV. Jako kodowanie wybieramy UTF-8, reszta bez zmian.



Generowanie żetonów:

1. Odpalamy CMD
2. Przechodzimy do katalogu gdzie mamy ściągnięty generator.
3. Wykonujemy polecenie:
	python gen4.py wb95 example-wb95.csv
4. wygenerowane zetony znajduja sie w pliku gen4-counters-sheet-1.svg
5. możemy sobie pooglądać arkusz w przeglądarce
