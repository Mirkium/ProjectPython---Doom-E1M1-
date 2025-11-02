import pygame
import os
import sys
from script.constante import WINDOW_WIDTH, WINDOW_HEIGHT

def close():
    pygame.quit()
    sys.exit()

def load_pic_BG(screen, image):
    screen.fill((0, 0, 0))
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        full_path = os.path.join(base_path, image)

        bg = pygame.image.load(full_path).convert_alpha()
        bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
        return bg
    except Exception as e:
        print("Impossible de charger l'image. Vérifie le dossier assets.")
        print(f"{e}")
        return None

def refresh(clock):
    pygame.display.flip()
    clock.tick(60)