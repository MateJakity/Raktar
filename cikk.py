class Cikk:
    def __init__(self, id, nev, egyseg, mennyiseg, egysegar):
        self.id = id
        self.nev = nev
        self.egyseg = egyseg
        self.mennyiseg = mennyiseg
        self.egysegar = egysegar

    def ertek(self):
        return self.mennyiseg * self.egysegar

    def __repr__(self):
        return f"Cikk({self.id}, {self.nev}, {self.mennyiseg} {self.egyseg}, {self.egysegar} Ft)"