Név: Jakity Máté
Neptun-kód: U1K1PR

Feladat rövid leírása:
A beadandó feladata egy raktárkészlet-nyilvántartó Python alkalmazás.
A program CSV fájlban tárolt készletadatokat kezel, lehetőséget biztosít:
-új cikk felvételére
-cikkek mennyiségének módosítására
-cikkek törlésére
-a teljes készlet értékének kiszámítására
-valamint a készlet grafikus megjelenítésére turtle segítségével.

Modulok és a modulokban használt függvények
1. main.py
A program belépési pontja.
Feladata a menü megjelenítése és a felhasználói interakciók kezelése.

Függvények:
menu() – menü kiírása
main() – programirányítás, funkciók hívása

2. raktar_modul.py
A raktárkészlet logikai műveletei és a CSV-kezelés.
Függvények:
- keszlet_betolt() – adatok beolvasása CSV-ből
- keszlet_ment() – adatok mentése CSV-be
- uj_cikk_letrehozasa() – új cikk felvétele
- cikkek_listazasa() – cikkek kilistázása
- cikk_keres() – ID alapú keresés
- mennyiseg_modositas() – mennyiség növelése/csökkentése
- cikk_torlese() – cikk törlése
- teljes_ertek() – teljes készlet értékének kiszámítása

3. cikk.py - > Saját osztály
Saját osztály modul.
Osztály:
Cikk
Attribútumai:
- id
- nev
- egyseg
- mennyiseg
- egysegar

Metódusai:
ertek() – a cikk összértéke
__repr__() – objektum reprezentációja

4. grafika.py
Grafikai modul turtle segítségével.
Az oszlopdiagram kattintható → eseménykezelés!

Függvények:
- rajzol_keszlet(keszlet)
- a készlet mennyiségeit oszlopdiagramként ábrázolja
- kattintásra kiírja az adott cikk adatait (onscreenclick eseménykezelő)