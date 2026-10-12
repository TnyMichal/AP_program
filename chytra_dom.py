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
         

    def zmen_barvu(self,nova_barva:str):
        self.barva = nova_barva
        return f"změna barvy:  {nova_barva}"
     
class Ch_zasuvka(Ch_zarizeni):
    def __init__(self, nazev: str, mistnost: str, zapnuto: bool = False, aktualni_odber_w: float = 0.0):
         super().__init__(nazev, mistnost, zapnuto)
         self.aktualni_odber_w = aktualni_odber_w
    
    def proved_akci(self):
         if self.zapnuto:
             return f"Zasuvka {self.nazev} propouští proud, odběr {self.aktualni_odber_w} W"
         else:
             return f"Zásuvka {self.nazev} je vypnutá "
        
            




zarovka = Ch_zarovka("Stropní světlo", "Kuchyně",zapnuto=True, barva= "žlutá")
zasuvka = Ch_zasuvka("Pračka","Kumbál", zapnuto=True, aktualni_odber_w= 50000)

domacnost = [zarovka,zasuvka]


for zarizeni in domacnost:
    zarizeni.zapnuto = False
    print(zarizeni.proved_akci())

