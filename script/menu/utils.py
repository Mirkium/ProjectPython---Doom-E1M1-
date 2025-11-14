import pygame
import os
import sys
from script.menu.config import Screen

def close():
    pygame.quit()
    sys.exit()

def load_pic_BG(screen, image):
    screen.fill((0, 0, 0))
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        full_path = os.path.join(base_path, image)

        bg = pygame.image.load(full_path)
        bg = pygame.transform.scale(bg, (Screen.WIDTH, Screen.HEIGHT))
        return bg
    except Exception as e:
        print("Impossible de charger l'image. Vérifie le dossier assets.")
        print(f"{e}")
        return None

def load_pic(image_path, width=None,height=None):
    try:
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        full_path = os.path.join(base_path, image_path)

        img = pygame.image.load(full_path).convert_alpha()
        img = crop_alpha_surface(img)

        if width and height:
            img = pygame.transform.smoothscale(img, (width, height))

        return img
    except Exception as e:
        print(f"Impossible de charger l'image du bouton : {image_path}")
        print(f"Erreur : {e}")
        return None

def refresh(clock):
    pygame.display.flip()
    clock.tick(60)

def crop_alpha_surface(surface):
    rect = surface.get_bounding_rect()
    cropped = pygame.Surface(rect.size, pygame.SRCALPHA)
    cropped.blit(surface, (0, 0), rect)
    return cropped
