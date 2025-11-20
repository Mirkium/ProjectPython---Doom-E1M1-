import pygame
import sys
from script.constante import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE
from script.menu.lvl1 import lvl1
from script.menu.utils import close

def menu():
    pygame.init()
    pygame.mixer.init()  # pour le son

    # Création de la fenêtre
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    # --- Chargement des ressources ---
    try:
        menu_bg = pygame.image.load("assets/img/Doom_Logo.png")
        menu_bg = pygame.transform.scale(menu_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    except:
        print("⚠️  Impossible de charger l'image 'menu_background.png'. Vérifie le dossier assets.")
        menu_bg = None

    try:
        pygame.mixer.music.load("assets/doom_theme.mp3")
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)  # boucle infinie
    except:
        print("⚠️  Impossible de charger la musique 'doom_theme.mp3'. Vérifie le dossier assets.")

    # --- Configuration du texte ---
    font_title = pygame.font.SysFont("Arial", 72, bold=True)
    font_prompt = pygame.font.SysFont("Arial", 32)

    title_text = font_title.render("DOOM", True, (255, 0, 0))
    prompt_text = font_prompt.render("Appuyez sur [ENTRÉE] pour commencer", True, (200, 200, 200))
    quit_text = font_prompt.render("Appuyez sur [ECHAP] pour quitter", True, (200, 200, 200))

    running = {'menu': True, 'lvl1': False, 'pause': False}

    while running['menu']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close(running)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("🚀 Lancement du jeu...")
                    running['lvl1'] = True
                    lvl1(screen, running)
                elif event.key == pygame.K_ESCAPE:
                    running['menu'] = False

        # --- Affichage ---
        if menu_bg:
            screen.fill((20, 20, 20))
            screen.blit(menu_bg, (0, 0))

        # Affichage du texte
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 150))
        screen.blit(prompt_text, (WINDOW_WIDTH // 2 - prompt_text.get_width() // 2, 450))
        screen.blit(quit_text, (WINDOW_WIDTH // 2 - quit_text.get_width() // 2, 500))

        # Mise à jour de l'écran
        pygame.display.flip()
        clock.tick(60)

    # --- Fermeture propre ---
    pygame.mixer.music.stop()
    pygame.quit()
    sys.exit()