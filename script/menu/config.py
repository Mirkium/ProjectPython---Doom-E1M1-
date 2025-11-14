import pygame

class Screen:
    pygame.init()
    info = pygame.display.Info()
    WIDTH = info.current_w
    HEIGHT = info.current_h
    pygame.quit()
