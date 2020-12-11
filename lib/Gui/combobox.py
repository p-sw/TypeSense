import pygame
from lib.Gui.label import Label
from lib.Gui.Base import color


class ComboBox(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, item_list: list or tuple, text: str, size: int):
        super().__init__()
        self.image = pygame.Surface([width, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color.COMBO_BACKGROUND_DEFAULT_COLOR.get(tuple))
        self.items = []
        for index, item in enumerate(item_list):
            item_label = Label(16, item, bg_cl=color.WHITE)
            item_label.text_rect.centerx = self.rect.centerx
            item_label.text_rect.centery = (index * 2 + 1) * self.rect.centery
            self.items.append(item_label)
        self.highlighted = False
        self.pressed = False
        self.activated = False
        # TODO: MAKE TEXT LABEL

    def check(self, event_list, screen: pygame.Surface):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        if self.rect.x <= pos[0] <= self.rect.topright[0] and self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if pygame.MOUSEBUTTONDONW in vnt_type and not self.activated:
                self.pressed = True
                self.highlighted = False
                self.activated = False
            if pygame.MOUSEBUTTONUP in vnt_type and not self.activated and self.pressed:
                self.pressed = False
                self.highlighted = False
                self.activated = True
            if pygame.MOUSEBUTTONUP not in vnt_type and pygame.MOUSEBUTTONDOWN not in vnt_type:
                if not self.activated and not self.pressed:
                    self.highlighted = True
        else:
            if pygame.MOUSEBUTTONDOWN in vnt_type and self.activated:
                self.activated = False
            else:
                self.activated = False
                self.pressed = False
                self.highlighted = False
        if self.highlighted:
            self.image.fill(color.COMBO_BACKGROUND_HIGHLIGHTED_COLOR.get(tuple))
        elif self.pressed:
            self.image.fill(color.COMBO_BACKGROUND_PRESSED_COLOR.get(tuple))
        # elif self.activated:
            # TODO: MAKE ACTIVATED STATE
        else:
            self.image.fill(color.COMBO_BACKGROUND_DEFAULT_COLOR.get(tuple))
