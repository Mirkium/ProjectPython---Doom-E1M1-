import pygame
from script.menu.utils import load_pic_BG, refresh

def pause(screen, clock):
    pause_bg = load_pic_BG(screen, "assets/sprites/zombie/Zombie.png")

    running_pause = True
    
    while running_pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                elif event.key == pygame.K_RETURN:
                    return "lvl1"

        screen.blit(pause_bg, (0, 0))
        
        refresh(clock)