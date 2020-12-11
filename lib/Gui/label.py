import pygame
from lib.Gui.Base import color
from lib.Gui.Base.RGB import RGB


class Label:
    def __init__(self, size: int, text: str, x: int = 0, mid_y: int = 0, cl: RGB = None, bg_cl: RGB = None):
        self.font = pygame.font.Font("assets\\arial.ttf", size)
        self.text = self.font.render(text, False, (0, 0, 0))
        self.cl = cl
        self.bg_cl = bg_cl

        self.set_text(text)

        self.text_rect = self.text.get_rect()
        self.text_rect.x = x
        self.text_rect.centery = mid_y

    def get_text(self):
        return self.text

    def get_rect(self):
        return self.text_rect

    def set_text(self, text):
        if self.cl is None and self.bg_cl is None:
            self.text = self.font.render(text, True, color.DEFAULT_TEXT_COLOR.get(tuple))
        else:
            if self.cl is not None or self.bg_cl is not None:
                if self.cl is not None:
                    self.text = self.font.render(text, True, self.cl.get(tuple))
                elif self.bg_cl is not None:
                    self.text = self.font.render(text, True, color.DEFAULT_TEXT_COLOR.get(tuple), self.bg_cl.get(tuple))
            elif self.cl is not None and self.bg_cl is not None:
                self.text = self.font.render(text, True, self.cl.get(tuple), self.bg_cl.get(tuple))

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
