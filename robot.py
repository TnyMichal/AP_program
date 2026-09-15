class Robot:
    def __init__(self,oznaceni:str, baterie:int, ukol:str):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        
        pass
    
    def zvuk(self):
        return("Wrum Wrum")
    
    def diagnostika(self):
        return f"model:  {self.oznaceni}" f"baterie:   {self.baterie}"
    
    def aktualni_ukol(self):
        return f"Zbírám   {self.ukol}"
    
    def zadej_ukol(self, novy_ukol:str):
        self.ukol = novy_ukol
        return f"Nový úkol:  {novy_ukol}"
    
robot = Robot("Rezavá mršina",20,"Odpadky")

print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)

print(robot.zvuk())
print(robot.diagnostika())
print(robot.aktualni_ukol())
print(robot.zadej_ukol("Nabít se"))
