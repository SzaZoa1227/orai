class Fuvar:
    def __init__(self,azonosito:int,indulas:str,idotartam:int,tavolsag:float,viteldij:float,borravalo:float,fizetes_modja:str) -> None:
        self.azonosito = azonosito
        self.indulas = indulas
        self.idotartam = idotartam
        self.tavolsag = tavolsag
        self.viteldij = viteldij
        self.borravalo = borravalo
        self.fizetes_modja = fizetes_modja
        pass
fuvarok = []
with open("fuvar.csv","rt",encoding="utf-8") as bemenet:
    bemenet.readline()
    for sor in bemenet:
        sor = sor.strip()
        sor = sor.replace(",",".")
        sor = sor.split(";")
        fuvarok.append(Fuvar(int(sor[0]),sor[1],int(sor[2]), float(sor[3]),float(sor[4]),float(sor[5]),sor[6]))
print(len(fuvarok))

bevetel = 0
fuvarjai = 0

fizetesimodok = {}

for fuvar in fuvarok:
    if fuvar.fizetes_modja not in fizetesimodok.keys():
        fizetesimodok[fuvar.fizetes_modja] = 1
    else: fizetesimodok[fuvar.fizetes_modja] += 1
    if fuvar.azonosito == 6185:
        fuvarjai += 1
        bevetel += (fuvar.viteldij * fuvar.tavolsag) + fuvar.borravalo
print(f"6185 számú taxinak {fuvarjai} fuvar alatt {bevetel}$ bevétele volt.")

for kulcs,ertek in fizetesimodok.items():
    print(kulcs,ertek)