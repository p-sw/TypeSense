import pygame
from lib.Gui.Base import color


class Label:
    def __init__(self, size: int, text: str, x: int = 0, mid_y: int = 0):
        self.font = pygame.font.Font("assets\\arial.ttf", size)
        self.text = self.font.render(text, True, color.TEXT_COLOR.get(tuple))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = x
        self.text_rect.centery = mid_y

    def get_text(self):
        return self.text

    def get_rect(self):
        return self.text_rect

    def change_text(self, text):
        self.text = self.font.render(text, True, color.TEXT_COLOR.get(tuple))

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
