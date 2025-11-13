class Npc(entity):
    def __init__(self, name="ennemy", speed=0, life=100, position=[0,0]):
        super().__init__(name, speed, life, position)