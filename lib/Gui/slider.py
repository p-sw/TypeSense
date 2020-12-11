import pygame
from lib.Gui.Base import color
from lib.Gui.label import Label
from lib import logger


class Slider(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, text: str, size: int, unit_str: str,
                 default_v: int or float, start_v: int or float, limit_v: int or float, decimal_limit: int = 2):
        if start_v >= limit_v:
            raise ValueError
        super().__init__()
        self.image = pygame.Surface([width, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color.SLIDER_BACKGROUND_DEFAULT_COLOR.get(tuple))

        self.value = round(default_v, decimal_limit)
        self.start_v = start_v
        self.limit_v = limit_v
        self.activated = False
        self.highlighted = False
        self.value_per_px = (limit_v - start_v) / width
        self.level_px = int(self.value / self.value_per_px)
        self.decimal_limit = decimal_limit

        self.unit = unit_str
        self.value_label = Label(16, str(self.value)+self.unit, self.rect.x + int(width / 4), self.rect.centery)

        self.label = Label(size, text)
        self.label.text_rect.x = self.rect.x
        self.label.text_rect.y = self.rect.y - (self.label.text_rect.height + 2)

    def update(self):
        super().update()
        pos = pygame.mouse.get_pos()
        in_bar_px = pos[0] - self.rect.x
        if self.activated:
            self.value = round(in_bar_px * self.value_per_px, self.decimal_limit)
            self.value_label.change_text(str(self.value)+self.unit)
            self.level_px = int(self.value / self.value_per_px)
        if self.value < self.start_v:
            self.value = self.start_v
        if self.value > self.limit_v:
            self.value = self.limit_v
        # Do not add draw function here

    def check(self, event_list, screen):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        if self.rect.x <= pos[0] <= self.rect.topright[0] and self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if pygame.MOUSEBUTTONDOWN in vnt_type:
                self.activated = True
                self.highlighted = False
                logger.debug("Slider Activated")
            elif pygame.MOUSEBUTTONUP in vnt_type and self.activated:
                self.activated = False
                self.highlighted = True
                logger.debug("Slider Deactivated")
            elif pygame.MOUSEBUTTONUP not in vnt_type and self.activated:
                self.activated = True
                self.highlighted = False
            else:
                self.activated = False
                self.highlighted = True
        else:
            self.activated = False
            self.highlighted = False

        if not self.rect.x <= pos[0] <= self.rect.topright[0] or not self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if self.activated:
                self.activated = False
                logger.debug("Slider Deactivated")

        if self.activated:
            self.image.fill(color.SLIDER_BACKGROUND_ACTIVATED_COLOR.get(tuple))
        elif self.highlighted:
            self.image.fill(color.SLIDER_BACKGROUND_HIGHLIGHTED_COLOR.get(tuple))
        else:
            self.image.fill(color.SLIDER_BACKGROUND_DEFAULT_COLOR.get(tuple))
        pygame.draw.rect(self.image, color.SLIDER_FILLED_COLOR.get(tuple), [0, 0, self.level_px, self.rect.height])
        pygame.draw.rect(self.image, color.SLIDER_FILLED_SHADOW_COLOR.get(tuple),
                         [0, self.rect.height / 2, self.level_px, self.rect.height / 2])

    def font_draw(self, screen):
        self.label.draw(screen)
        self.value_label.draw(screen)
