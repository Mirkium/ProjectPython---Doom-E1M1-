import pygame
from script.constante import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from script.menu.utils import close
from script.menu.menu import menu
from script.menu.lvl1 import lvl1
from script.menu.pause import pause

def engine():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
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
            case "quit":
                running = False
            case _:
                print("etat inconnu")
                running = False

    close()
