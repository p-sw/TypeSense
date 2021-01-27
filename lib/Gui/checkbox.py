import pygame
from lib.Gui.Base import color
from lib import logger
from lib.Gui.label import Label


class Checkbox(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, text: str, size: int):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(color.BUTTON_BACKGROUND_DEFAULT_COLOR.get(tuple))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.enabled = False
        self.activated = False
        self.label = Label(size, text, self.rect.topright[0] + 2, self.rect.centery)

    def check(self, event_list):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        if self.rect.x <= pos[0] <= self.rect.topright[0] and self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if self.activated:
                self.image.fill(color.BUTTON_BACKGROUND_ACTIVATED_COLOR.get(tuple))
            if pygame.MOUSEBUTTONDOWN in vnt_type:
                self.image.fill(color.BUTTON_BACKGROUND_ACTIVATED_COLOR.get(tuple))
                self.activated = True
                logger.debug("Button Pressed")
            elif pygame.MOUSEBUTTONUP in vnt_type and self.activated:
                self.image.fill(color.BUTTON_BACKGROUND_DEFAULT_COLOR.get(tuple))
                self.activated = False
                self.enabled = not self.enabled
                logger.debug("Button Enabled")
            else:
                self.image.fill(color.BUTTON_BACKGROUND_HIGHLIGHTED_COLOR.get(tuple))
        elif not self.rect.x <= pos[0] <= self.rect.topright[0] or not self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            self.image.fill(color.BUTTON_BACKGROUND_DEFAULT_COLOR.get(tuple))
            if self.activated:
                self.activated = False

        if self.enabled:
            pygame.draw.rect(self.image, color.BUTTON_FILLED_COLOR.get(tuple), [2, 2, 11, 11])

    def font_draw(self, screen):
        self.label.draw(screen)
