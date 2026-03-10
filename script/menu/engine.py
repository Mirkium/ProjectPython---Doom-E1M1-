import pygame
from script.menu.config import Screen
from script.menu.utils import close
from script.menu.menu import menu
from script.menu.lvl1 import lvl1
from script.menu.pause import pause
from script.menu.gameover import gameover

def engine():
    pygame.init()

    screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
    clock = pygame.time.Clock()

    state = "menu"
    running = True

    while running:
        match state:
            case "menu":
                state = menu(screen, clock)
            case "lvl1":
                state = lvl1(screen, clock)
            case "pause":
                state = pause(screen, clock)
            case "gameover":
                state = gameover(screen, clock)
            case "quit":
                running = False
            case _:
                print("etat inconnu")
                running = False

    close()
