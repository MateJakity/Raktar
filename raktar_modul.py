import csv
import os
from cikk import Cikk

FAJL_NEV = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "resources",
    "keszlet.csv"
)

def keszlet_betolt():
    keszlet = []

    os.makedirs(os.path.dirname(FAJL_NEV), exist_ok=True)

    if not os.path.exists(FAJL_NEV):
        with open(FAJL_NEV, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["id", "nev", "egyseg", "mennyiseg", "egysegar"])
        return keszlet

    try:
        with open(FAJL_NEV, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")
            for sor in reader:
                cikk = Cikk(
                    id=int(sor["id"]),
                    nev=sor["nev"],
                    egyseg=sor["egyseg"],
                    mennyiseg=float(sor["mennyiseg"]),
                    egysegar=float(sor["egysegar"])
                )
                keszlet.append(cikk)
    except Exception as e:
        print("Hiba történt a CSV beolvasása közben:", e)

    return keszlet


def keszlet_ment(keszlet):

    try:
        os.makedirs(os.path.dirname(FAJL_NEV), exist_ok=True)

        with open(FAJL_NEV, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["id", "nev", "egyseg", "mennyiseg", "egysegar"])
            for c in keszlet:
                writer.writerow([c.id, c.nev, c.egyseg, c.mennyiseg, c.egysegar])

    except Exception as e:
        print("Hiba mentés közben:", e)

def cikk_keres(keszlet, id):
    return next((c for c in keszlet if c.id == id), None)


def uj_cikk_letrehozasa(keszlet):
    print("\n--- Új cikk felvétele ---")
    nev = input("Cikk neve: ").strip()
    if not nev:
        print("A név nem lehet üres.")
        return

    egyseg = input("Egység (db/kg/l): ").strip()
    if not egyseg:
        print("Az egység nem lehet üres.")
        return

    try:
        mennyiseg = float(input("Kezdő mennyiség: ").replace(",", "."))
        egysegar = float(input("Egységár (Ft): ").replace(",", "."))
    except ValueError:
        print("Hibás számformátum.")
        return

    uj_id = max([c.id for c in keszlet], default=0) + 1

    uj = Cikk(uj_id, nev, egyseg, mennyiseg, egysegar)
    keszlet.append(uj)

    print(f"Cikk hozzáadva: {nev} (ID: {uj_id})")


def cikkek_listazasa(keszlet):
    print("\n--- Készlet listázása ---")
    if not keszlet:
        print("A készlet üres.")
        return

    print("{:<5} {:<20} {:>10} {:<6} {:>10}".format("ID", "Név", "Menny.", "Egys.", "Ár"))
    print("-" * 60)
    for c in keszlet:
        print("{:<5} {:<20} {:>10.2f} {:<6} {:>10.2f}".format(
            c.id, c.nev, c.mennyiseg, c.egyseg, c.egysegar
        ))


def mennyiseg_modositas(keszlet):
    print("\n--- Mennyiség módosítása ---")
    try:
        id = int(input("Cikk ID: "))
    except ValueError:
        print("Érvénytelen ID.")
        return

    cikk = cikk_keres(keszlet, id)
    if not cikk:
        print("Nincs ilyen cikk!")
        return

    try:
        valtozas = float(input("Mennyivel változzon? (+/-): ").replace(",", "."))
    except ValueError:
        print("Érvénytelen szám.")
        return

    if cikk.mennyiseg + valtozas < 0:
        print("A mennyiség nem lehet negatív!")
        return

    cikk.mennyiseg += valtozas
    print("Mennyiség módosítva.")


def cikk_torlese(keszlet):
    print("\n--- Cikk törlése ---")
    try:
        id = int(input("Cikk ID: "))
    except ValueError:
        print("Érvénytelen ID.")
        return

    cikk = cikk_keres(keszlet, id)
    if not cikk:
        print("Nincs ilyen cikk!")
        return

    keszlet.remove(cikk)
    print("Cikk törölve.")


def teljes_ertek(keszlet):
    ertek = sum(c.ertek() for c in keszlet)
    print(f"\nA teljes készlet értéke: {ertek:.2f} Ft")
