# BIOS_lab3_zad1_ProteinContactMap
Program korzysta z bibliotek BioPython (Bio.PDB), numpy, pylab

Na początku kodu ustawiane są parametry wejściowe: pdb_code (id w bazie PDB) oraz nazwa pliku PDB, z którego program ma korzystać.

_Funkcje:_

* calculate_distance(x,y) - wylicza odległość między dwoma atomami alfa węgli z różnych reszt

* calculate_distance_matrix(chain) - tworzy macierz odległościi dla atomów CA łańcucha nukleotydów białka

_Działanie programu:_

wczytanie struktury białka z pliku .PDB

wybór pierwszego modelu struktury

wybór łańcucha (A)

wyliczenie macierzy (distance_matrix) w łańcuchu A

wyświetlenie macierzy

wyświetlenie heatmapy na podstawie transponowanej macierzy (zamiana wierszy i kolumn zwiększa czytelność wykresu)

_Interpretacja wykresu:_

Kolory wskazują odległość między atomami, wzięto pod uwagę 0-8 Angstremów. 

Mapę interpretujemy wyszukując charakterystycznych wystąpień kontaktów - 

wzdłuż przekątnej kontakty wskazują na ułożenie w alfa-helisę, 

przeciwrównoległe beta kartki to fragmenty prostopadłe do przekątnej.

Równoległe beta kartki to te fragmenty, które są równoległe do przekątnej, 
ale nie znajdują się bezpośrednio w jej pobliżu.

Pętle to przerwy w motywach prostopadłych beta kartek.
