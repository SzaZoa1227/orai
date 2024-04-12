class Nev:
    def __init__(self,utonev,elso,masodik,ujsz_1,ujsz_2,nem) -> None:
        self.utonev = utonev
        self.elso = (elso)
        self.masodik =(masodik)
        self.ujsz_1 = (ujsz_1)
        self.ujsz_2 = (ujsz_2)
        self.nem = nem
        if self.elso == "":
            self.elso = 0
        else: self.elso = int(self.elso)
        if self.masodik == "":
            self.masodik = 0
        else: self.masodik = int(self.masodik)
        if self.ujsz_1 == "":
            self.ujsz_1 = 0
        if self.ujsz_2 == "":
            self.ujsz_2 = 0
        if self.nem == "F":
            self.nem = "Férfi"
        else: self.nem = "Női"
        pass

    def __str__(self)-> str:
        return f"{self.utonev} {self.nem} keresztnevet régen {self.elso} alkalommal adták első keresztnévnek, {self.masodik} alkalommal második keresztnévnek.\
        \nÚjabban {self.ujsz_1} alkalommal adták első, {self.ujsz_2} alkallommal második keresztnévnek."
nevek = []
nepesseg: int = 0
nok:int = 0
ferfiak:int = 0
with open("UTONEV.txt","rt",encoding="ANSI") as be:
    be.readline()
    for sor in be:
        sor = sor.strip().split(";")
        nevek.append(Nev(sor[0],sor[1],(sor[2]),(sor[3]),(sor[4]),sor[5]))
for nev in nevek:
    nepesseg += nev.elso
for nev in nevek:
    if nev.nem == "Férfi":
        ferfiak += nev.elso
    else: nok += nev.elso
print(f"{len(nevek)} névről van adat a listában")
print(f"Az adott évben {nepesseg} volt az ország népessége")
print(f"Az adott évben a nők száma: {nok}\nAz adott évben a férfiak száma: {ferfiak}")