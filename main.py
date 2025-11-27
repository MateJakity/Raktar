from raktar_modul import (
    keszlet_betolt,
    keszlet_ment,
    uj_cikk_letrehozasa,
    cikkek_listazasa,
    mennyiseg_modositas,
    cikk_torlese,
    teljes_ertek
)
from grafikus_modul import rajzol_keszlet

def menu():
    print("\n========== KÉSZLETKEZELŐ ==========")
    print("1 - Cikkek listázása")
    print("2 - Új cikk hozzáadása")
    print("3 - Mennyiség módosítása")
    print("4 - Cikk törlése")
    print("5 - Teljes készlet érték")
    print("6 - Grafikus megjelenítés (turtle)")
    print("0 - Kilépés és mentés")
    print("===================================")


def main():
    keszlet = keszlet_betolt()

    while True:
        menu()
        v = input("Választás: ")

        if v == "1":
            cikkek_listazasa(keszlet)
        elif v == "2":
            uj_cikk_letrehozasa(keszlet)
        elif v == "3":
            mennyiseg_modositas(keszlet)
        elif v == "4":
            cikk_torlese(keszlet)
        elif v == "5":
            teljes_ertek(keszlet)
        elif v == "6":
            rajzol_keszlet(keszlet)
        elif v == "0":
            keszlet_ment(keszlet)
            print("Mentés kész. Kilépés.")
            break
        else:
            print("Ismeretlen menüpont!")


if __name__ == "__main__":
    main()
