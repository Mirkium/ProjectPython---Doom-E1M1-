import pygame
import sys
from script.constante import WINDOW_WIDTH, WINDOW_HEIGHT
from script.menu.utils import close

def pause(screen, running):
    pause_bg = pygame.image.load("assets/sprites/zombie/Zombie.png")
    pause_bg = pygame.transform.scale(pause_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    
    while running['pause']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close(running)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running['pause'] = False
                elif event.key == pygame.K_RETURN:
                    running['lvl1'] = True
                    running['pause'] = False

        screen.blit(pause_bg, (0, 0))
        pygame.display.flip()
        clock.tick(60)