class Naradi:
    def __init__(self,znacka:str,model:str):
        self.znacka = znacka
        self.model = model
        pass
    
    def identifikace(self):
        return f"Značka nářadí: {self.znacka}"
    
    def pracuj(self):
        return f"Model nářadí je: {self.model}"
    
class Akuvrtacka(Naradi):
    def __init__(self, znacka, model,baterie: int):
        super().__init__(znacka, model,baterie)
        self.baterie = baterie
        return f"Procent baterie: {self.baterie}"
    
    def pracuj(self):
        if self.baterie > 0:
            self.baterie -= 10
            if self.baterie < 0:
                self.baterie = 0
            return f"Vrtá {self.model} stav baterie:  {self.baterie}"
        else:
            return f"nutno nabít!!!!"         
        
class Motorova_pila(Naradi):
    def __init__(self, znacka, model,nadrz_plna: bool = True):
        super().__init__(znacka, model, nadrz_plna)
        self.nadrz_plna = nadrz_plna  
        
    def pracuj(self):
        if self.nadrz_plna:
            return f"Motorová pila {self.model} řezá dřevo"
        else:
            return f"Motorové {self.model} pile došlo palivo "             
        
vrtacka = []     
while .baterie > 0:
    print(Akuvrtacka.pracuj())    
    
print (Akuvrtacka.pracuj())
        
        
        
        