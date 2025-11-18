import pygame
from script.menu.utils import load_pic_BG, refresh
from script.menu.bouton import Bouton
from script.menu.config import Screen

def menu(screen, clock):
    menu_bg = load_pic_BG(screen, "assets/img/doommenu.png")

    boutons = [
        Bouton("Jouer", "assets/img/newgame.png",
               (screen.get_width()//2, 500), Screen.WIDTH/7, Screen.HEIGHT/13),

        Bouton("Quitter", "assets/img/quitgame.png",
               (screen.get_width()//2, 700), Screen.WIDTH/7, Screen.HEIGHT/13)
    ]

    while True:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "quit"

                if event.key == pygame.K_RETURN:
                    hovered = next((b for b in boutons if b.hovered),
                                   next(b for b in boutons if b.text == "Jouer"))

                    return "lvl1" if hovered.text == "Jouer" else "quit"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for b in boutons:
                    if b.hovered:
                        return "lvl1" if b.text == "Jouer" else "quit"

        for b in boutons:
            b.update_hover(mouse_pos)

        screen.blit(menu_bg, (0, 0))
        for b in boutons:
            b.draw(screen)

        refresh(clock)
