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
        self.items = pygame.sprite.Group()
        self.value_label = Label(16, item_list[0])
        self.value_label.text_rect.centerx = self.rect.centerx
        self.value_label.text_rect.centery = self.rect.centery
        for index, item in enumerate(item_list):
            item_label = ComboBoxSelection(self.rect.centerx, (index * 2 + 1) * self.rect.centery, 200, item)
            self.items.add(item_label)
        self.highlighted = False
        self.pressed = False
        self.activated = False
        self.label = Label(size, text)
        self.label.text_rect.x = self.rect.x
        self.label.text_rect.y = self.rect.y - (self.label.text_rect.height + 2)

    def check(self, event_list):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        if self.rect.x <= pos[0] <= self.rect.topright[0] and self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if pygame.MOUSEBUTTONDOWN in vnt_type and not self.activated:
                print("MOUSEBUTTONDOWN detected")
                self.pressed = True
                self.highlighted = False
                self.activated = False
            elif pygame.MOUSEBUTTONUP in vnt_type and not self.activated and self.pressed:
                print("MOUSEBUTTONUP detected")
                self.pressed = False
                self.highlighted = False
                self.activated = True
            else:
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
        else:
            self.image.fill(color.COMBO_BACKGROUND_DEFAULT_COLOR.get(tuple))

        for item in self.items:
            if item.selected:
                self.value_label.set_text(item.text)

    def font_draw(self, screen):
        self.label.draw(screen)
        self.value_label.draw(screen)

    def activated_draw(self, event_list, screen):
        if self.activated:
            self.items.update()
            for item in self.items:
                item.check(event_list)
            self.items.draw(screen)
            for item in self.items:
                item.font_draw(screen)
                # TODO: FIX RENDERING BUG


class ComboBoxSelection(pygame.sprite.Sprite):
    def __init__(self, x, y, width, item_text):
        super().__init__()
        self.image = pygame.Surface([width, 20])
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.image.fill(color.COMBO_ACTIVATED_DEFAULT_COLOR.get(tuple))

        self.label = Label(14, item_text)
        self.label.text_rect.centerx = x
        self.label.text_rect.centery = y
        self.text = item_text

        self.highlighted = False

        self.selected = False

    def check(self, event_list):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        if self.rect.x <= pos[0] <= self.rect.topright[0] and self.rect.y <= pos[1] <= self.rect.bottomleft[1]:
            if pygame.MOUSEBUTTONDOWN in vnt_type:
                self.highlighted = False
                self.selected = True
            else:
                self.highlighted = True
        else:
            self.highlighted = False

        if self.highlighted:
            self.image.fill(color.COMBO_ACTIVATED_HIGHLIGHTED_COLOR.get(tuple))
        else:
            self.image.fill(color.COMBO_ACTIVATED_DEFAULT_COLOR.get(tuple))

    def font_draw(self, screen):
        self.label.draw(screen)
