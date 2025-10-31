# main.py
# ==============================================
# Menu principal pour le projet DOOM (E1M1) – Python / Pygame
# Inspiré de DOOM 1993 / DOOM 2016
# ==============================================

import pygame
import sys

# --- Configuration de la fenêtre ---
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "DOOM (E1M1) - Menu Principal"

def main():
    # Initialisation de Pygame
    pygame.init()
    pygame.mixer.init()  # pour le son

    # Création de la fenêtre
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()

    # --- Chargement des ressources ---
    try:
        background = pygame.image.load("../assets/img/Doom_Logo.png")
        background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
    except:
        print("⚠️  Impossible de charger l'image 'menu_background.png'. Vérifie le dossier assets.")
        background = None

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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print("🚀 Lancement du jeu...")
                    # Ici tu lanceras ton code du jeu principal (ex: start_game())
                    running = False
                elif event.key == pygame.K_ESCAPE:
                    running = False

        # --- Affichage ---
        if background:
            screen.blit(background, (0, 0))
        else:
            screen.fill((20, 20, 20))

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


if __name__ == "__main__":
    main()
