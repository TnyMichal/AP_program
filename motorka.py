class Motorka:
   def __init__(self, znacka:str, kategorie:str, stav_nadrze:int):
       self.znacka = znacka
       self.kategorie = kategorie
       self.stav_nadrze = stav_nadrze
       self.stojanek = "Vklopeny"   
       
   def zatoc_plyn(self):
       return "VRRUM!"
   def popis_moto(self):
       return f"{self.znacka} ({self.kategorie}), nadrz: {self.stav_nadrze}%"
   
   def stav_stojanku_vypis(self):
       return f"Stojanek je: {self.stojanek}"
   
   def zmen_stojanek(self):
       if self.stojanek == "Vklopeny":
           self.stojanek = "Vyklopeny"
       else:
           self.stojanek = "Vklopeny"
       return f"Novy stav stojanku: {self.stojanek}"
   
   def popojeď(self, km:int):
       ubytek = km // 2
       self.stav_nadrze -= ubytek
       return f"Popojel jsem {km} km, ubylo {ubytek}% paliva"
   
   def vypis_palivo(self):
       return f"Aktualne je v nadrzi {self.stav_nadrze}%"
   
   def natankuj(self, mnozstvi:int):
       self.stav_nadrze += mnozstvi
       return f"Natankovano {mnozstvi}%, nadrz ma ted {self.stav_nadrze}%"

moto = Motorka("Honda", "Nahač", 60)
print(moto.popis_moto())
print(moto.zatoc_plyn())
print(moto.stav_stojanku_vypis())
print(moto.zmen_stojanek())
print(moto.popojeď(20))
print(moto.vypis_palivo())
print(moto.natankuj(30))