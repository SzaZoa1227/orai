#otodik feladatig!! +8as

class Adat:
    def __init__(self, datum:str,nagydij: str, helyezes:int, befejezett_kor:int, pont:int, konstruktor:str, celba_ert:bool, hiba_oka: str) -> None:
        self.datum = datum
        self.nagydij = nagydij
        self.helyezes = helyezes
        self.befejezett_kor = befejezett_kor
        self.pont = pont
        self.konstruktor = konstruktor
        self.celba_ert = celba_ert
        self.hiba_oka = hiba_oka
        pass
adatok = []
with open("kimi.csv","rt",encoding="utf-8") as be:
    be.readline()
    for sor in be:
        sor = sor.strip().split(';')
        sor[2] = int(sor[2]) if sor[2] != "" else 0
        sor[3] = int(sor[3])
        sor[4] = int(sor[4])
        sor[6] = True if sor[6] == "I" else False
        adatok.append(Adat(sor[0],sor[1],sor[2],sor[3],sor[4],sor[5],sor[6],sor[7]))

