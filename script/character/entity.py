class Entity:
    def __init__(self, name:str, speed:int, life:int, position:list[int]):
        self.name = name
        self.speed = speed
        self.life = life
        self.position = position

    def vision(self):
        pass #def le champ visuel

    def apperance(self):
        pass 

    def getDamages(self):
        pass #explicite lmao

    def fire(self):
        pass #same XD    peut etre joidre les deux

    def dead(self):
        if life == 0:
            print("U're dead")  #a override dans les classes filles
