class Kolcsonzes:
    def __init__(self, neve: str, jarmuazonosito: str, KidoO: int, KidoP: int, VidoO: int, VidoP: int) -> None:
        self.nev = neve
        self.jarmuazonosito = jarmuazonosito
        self.KidoO = KidoO
        self.KidoP = KidoP
        self.VidoP = VidoP
        self.VidoO = VidoO
    def neve(self) -> str:
        return self.nev
    def kolcsonzesIdeje(self) -> tuple[int,int]:
        kezdet = self.KidoO *60*60 + self.KidoP*60
        veg = self.VidoO *60*60 + self.VidoP*60
        return kezdet, veg

kolcsonzesek: list = []


with open("kolcsonzesek.txt","rt",encoding="utf-8") as be:
    be.readline()
    for sor in be:
        sor = sor.strip().split(";")
        kolcsonzesek.append(Kolcsonzes(sor[0],sor[1],int(sor[2]),int(sor[3]),int(sor[4]),int(sor[5])))

print(f"Első feladat: \n{len(kolcsonzesek)} kölcsönzés adata található meg a fájlban.")
rossz = 1
nev = ""
while rossz:
    nev = (input("Adj meg egy nevet, akinek a kölcsönzéseit meg akarod nézni!\t"))
    if nev == "":
        print("Adj is meg valamit!")
    else:
        rossz = 0
print("Második feladat")
for kolcsonzo in kolcsonzesek:
    if kolcsonzo.neve().lower() == nev.lower():
        print(f"{kolcsonzo.nev} kölcsönzött {kolcsonzo.KidoO}:{kolcsonzo.KidoP}-{kolcsonzo.VidoO}:{kolcsonzo.VidoP} között kölcsönzött.")
bekerO = 0
bekerP = 0
rossz = 1
while rossz:
    bekerO = input("Adj meg egy számot:)