import pygame
from script.menu.utils import load_pic

class Bouton:
    def __init__(self,text, image_path, position, width, height):
        self.text = text
        self.image_normal = load_pic(image_path, width, height)
        self.image_hover = self.image_normal.copy()
        self.image_hover.fill((50, 50, 50, 50), special_flags=pygame.BLEND_RGBA_ADD)

        self.image = self.image_normal
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.hovered = False

    def draw(self, screen):
        screen.blit(self.image_hover if self.hovered else self.image_normal, self.rect)

    def update_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)