import math

class Entity:
    def __init__(self, name:str, speed:int, life:int, position:tuple[int, int]):
        self.name = name
        self.speed = speed
        self.life = life
        self.position = position

    def vision(self, map):
        posx, posy = self.position
        nb_rays = 360
        step = 1
        rayon_max = 50

        visible_points = []

        for i in range(nb_rays):
            angle = (2 * math.pi / nb_rays) * i

            dx = math.cos(angle)
            dy = math.sin(angle)

            distance = 0
            rx, ry = posx, posy

            while distance < rayon_max:
                rx += dx * step
                ry += dy * step
                distance += step

                grid_x = int(rx)
                grid_y = int(ry)

                if grid_y < 0 or grid_y >= len(map_grid) or grid_x < 0 or grid_x >= len(map_grid[0]):
                    break

                visible_points.append((rx, ry))

                if map[grid_y][grid_x] == 1:
                    break
        

    def apperance(self):
        pass 

    def getDamages(self):
        pass #explicite lmao

    def fire(self):
        pass #same XD    peut etre joidre les deux

    def dead(self):
        if life == 0:
            print("U're dead")