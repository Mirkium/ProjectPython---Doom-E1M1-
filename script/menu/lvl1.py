import pygame
from script.menu.utils import load_pic_BG, refresh


def lvl1(screen, clock):
    lvl1_bg = load_pic_BG(screen, "assets/sprites/weapon/Weapons Doom Alpha.png")

    running_lvl1 = True
    
    while running_lvl1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "pause"

        screen.blit(lvl1_bg, (0, 0))
        
        refresh(clock)