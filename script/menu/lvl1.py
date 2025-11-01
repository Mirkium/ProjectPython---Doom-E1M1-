import pygame
import sys
from script.constante import WINDOW_WIDTH, WINDOW_HEIGHT
from script.menu.pause import pause
from script.menu.utils import close


def lvl1(screen, running):
    lvl1_bg = pygame.image.load("assets/sprites/weapon/Weapons Doom Alpha.png")
    lvl1_bg = pygame.transform.scale(lvl1_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    while running['lvl1']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close(running)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running['pause'] = True
                    running['lvl1'] = False
                    pause(screen, running)

        screen.blit(lvl1_bg, (0, 0))
        pygame.display.flip()
        clock.tick(60)