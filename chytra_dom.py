class Ch_zarizeni:
    def __init__ (self,nazev:str,mistnost:int, zapnuto: bool = False ):
        self.nazev = nazev
        self.mistnost = mistnost
        self.zapnuto = zapnuto

        pass

    def prepni_stav(self):
        self.zapnuto = not self.zapnuto
        return f"stav {self.zapnuto} "


    def proved_akci(self):
        return f"{self.nazev } čeká na příkaz"
    
class Ch_zarovka(Ch_zarizeni):
    def __init__ (self,nazev,mistnost,barva: str = "bílá",zapnuto: bool = False):
            super().__init__(nazev,mistnost,zapnuto)
            self.barva = barva

    def proved_akci (self):
         if self.zapnuto:
              return f"Žárovka {self.nazev} svítí barvou: {self.barva}"
         
         else:
              return f"Žárovka je zhasnuta"
         

    def zmen_barvu(self,nova_barva):
         return f"změna barvy:  {nova_barva}"
            


ch_zarizeni = Ch_zarizeni("Reproduktor",2,"Zapnuto")

print(ch_zarizeni.nazev)
print(ch_zarizeni.mistnost)
print(ch_zarizeni.zapnuto)

print(ch_zarizeni.prepni_stav())
print(ch_zarizeni.proved_akci())
