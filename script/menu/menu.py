import pygame
from script.menu.utils import load_pic_BG, refresh

def menu(screen, clock):

    menu_bg = load_pic_BG(screen, "assets/img/Doom_Logo.png")
    # --- Configuration du texte ---
    #font_title = pygame.font.SysFont("Arial", 72, bold=True)
    #font_prompt = pygame.font.SysFont("Arial", 32)

    #title_text = font_title.render("DOOM", True, (255, 0, 0))
    #prompt_text = font_prompt.render("Appuyez sur [ENTRÉE] pour commencer", True, (200, 200, 200))
    #quit_text = font_prompt.render("Appuyez sur [ECHAP] pour quitter", True, (200, 200, 200))

    running_menu = True

    while running_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "lvl1"
                elif event.key == pygame.K_ESCAPE:
                    return "quit"

        # Affichage du texte
        #screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 150))
        #screen.blit(prompt_text, (WINDOW_WIDTH // 2 - prompt_text.get_width() // 2, 450))
        #screen.blit(quit_text, (WINDOW_WIDTH // 2 - quit_text.get_width() // 2, 500))

        screen.blit(menu_bg, (0, 0))

        refresh(clock)
        
