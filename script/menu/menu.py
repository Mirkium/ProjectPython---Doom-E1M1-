import pygame
from script.menu.utils import load_pic_BG, refresh
from script.menu.bouton import Bouton
from script.menu.config import Screen

def menu(screen, clock):
    menu_bg = load_pic_BG(screen, "assets/img/doommenu.png")

    boutons = [
        Bouton("Jouer",'assets/img/newgame.png', (screen.get_width()//2, 500), Screen.WIDTH/7, Screen.HEIGHT/13),
        Bouton("Quitter",'assets/img/quitgame.png', (screen.get_width()//2, 700), Screen.WIDTH/7, Screen.HEIGHT/13)
    ]

    running_menu = True

    while running_menu:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"
                elif event.key == pygame.K_RETURN:
                    return "lvl1"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for bouton in boutons:
                        if bouton.is_hovered(mouse_pos):
                            if bouton.text == "Jouer":
                                return "lvl1"
                            elif bouton.text == "Quitter":
                                return "quit"

        for i, bouton in enumerate(boutons):
            bouton.selected = bouton.is_hovered(mouse_pos)

        screen.blit(menu_bg, (0, 0))

        for bouton in boutons:
            bouton.draw(screen)

        refresh(clock)