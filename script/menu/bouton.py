import pygame

class Bouton:
    def __init__(self, text, position, key=None, font=None, size=40):
        self.text = text
        self.position = position
        self.key = key 
        self.font = font or pygame.font.SysFont("Arial", size)
        self.color_normal = (255, 255, 255)
        self.color_hover = (255, 200, 0)
        self.selected = False
        self.rect = None
        self.render_text()

    def render_text(self):
        color = self.color_hover if self.selected else self.color_normal
        self.image = self.font.render(self.text, True, color)
        self.rect = self.image.get_rect(center=self.position)

    def draw(self, screen):
        self.render_text()
        screen.blit(self.image, self.rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)