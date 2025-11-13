class Player(entity):
    def __init__(self, name="DoomGuy", speed=0, life=0, position=[0,0]):
        super().__init__(name, speed, life, position)