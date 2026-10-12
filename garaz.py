class Vozidlo:
    def __init__(self,znacka:str, rok_vyroby:int,stav_nadrze:int = 100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze

    def zvuk_motoru(self):
        return f"vrm vrm "

    
    def info(self):
        return f"Značka {self.znacka}, Rok výroby {self.rok_vyroby}"

    def nastartuj(self):
        if self.stav_nadrze > 0:
            return f"Motor nastartován"
        else:
            return f"Motor nenastartován, nádrž je prázdná"

class Auto(Vozidlo):
    def __init__(self,znacka:str, rok_vyroby:int, stav_nadrze:int = 100,typ_prevodovky: str = "manuál"):
        super().__init__(znacka,rok_vyroby,stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zatrub(self):
        return f"Hou Hou"


class Moped(Vozidlo):
    def __init__(self,znacka:str,rok_vyroby:int, stav_nadrze:int = 100, ma_slapadla: bool = True):
        super().__init__(znacka,rok_vyroby,stav_nadrze,)
        self.ma_slapadla = ma_slapadla

    def slapej(self):
        if self.ma_slapadla:
            return f"slap slap"
        else:
            return f"nemam slapadla"

Auto1 = Auto("Škoda", 2020, 100, "automat")
Moped1 = Moped("Honda", 2019, 80, True)

Garaz = [Auto1,Moped1]

for Vozidlo in Garaz:
    print(Vozidlo.info())
    print(Vozidlo.nastartuj())
    print("_"*20)
  
