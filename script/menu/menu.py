import pygame
from script.menu.utils import load_pic_BG, refresh
from script.menu.bouton import Bouton

def menu(screen, clock):
    menu_bg = load_pic_BG(screen, "assets/img/doommenu.png")

    boutons = [
        Bouton("Jouer", (screen.get_width()//2, 300), key=pygame.K_RETURN),
        Bouton("Quitter", (screen.get_width()//2, 400), key=pygame.K_ESCAPE)
    ]

    selected_index = 0
    boutons[selected_index].selected = True

    running_menu = True

    while running_menu:
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    boutons[selected_index].selected = False
                    selected_index = (selected_index + 1) % len(boutons)
                    boutons[selected_index].selected = True
                elif event.key == pygame.K_UP:
                    boutons[selected_index].selected = False
                    selected_index = (selected_index - 1) % len(boutons)
                    boutons[selected_index].selected = True
                elif event.key == pygame.K_RETURN:
                    if boutons[selected_index].text == "Jouer":
                        return "lvl1"
                    elif boutons[selected_index].text == "Quitter":
                        return "quit"

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