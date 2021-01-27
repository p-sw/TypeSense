import pygame
from lib.Gui.label import Label
from lib.Gui.Base import color
from lib import logger


class Spinbox(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, item_list: list or tuple, text: str, size: int,
                 default_item: int = 0):
        super().__init__()
        self.image = pygame.Surface([width, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(color.SPIN_BACKGROUND_DEFAULT_COLOR.get(tuple))
        self.item_list = item_list
        self.item_label_list = []
        for item in self.item_list:
            item_value_label = Label(16, item)
            item_value_label.text_rect.centerx = self.rect.centerx
            item_value_label.text_rect.centery = self.rect.centery
            self.item_label_list.append(item_value_label)
        self.label = Label(size, text)
        self.label.text_rect.x = self.rect.x
        self.label.text_rect.y = self.rect.y - (self.label.text_rect.height + 2)
        self.item_index = default_item
        self.up_button = SpinButton(self.rect.width - 10,
                                    0,
                                    1,
                                    self.rect)
        self.down_button = SpinButton(self.rect.width - 10,
                                      10,
                                      -1,
                                      self.rect)
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.up_button, self.down_button)

    def check(self, event_list):
        if self.item_index <= 0:
            self.button_group.remove(self.down_button)
        if self.item_index >= len(self.item_list) - 1:
            self.button_group.remove(self.up_button)
        if 0 < self.item_index < len(self.item_list) - 1:
            self.button_group.add(self.up_button, self.down_button)
        print(str(self.item_index))
        print(str(len(self.item_list) - 1))
        self.button_group.update()
        for index, button in enumerate(self.button_group):
            button_clicked = button.check(event_list)
            if button_clicked:
                self.item_index += button.direction
        self.button_group.draw(self.image)

    def font_draw(self, screen):
        self.label.draw(screen)
        self.item_label_list[self.item_index].draw(screen)

    def get_selected_item(self):
        return self.item_list[self.item_index]


class SpinButton(pygame.sprite.Sprite):
    def __init__(self, x, y, t, parent_rect):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(color.SPIN_BUTTON_DEFAULT_COLOR.get(tuple))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.activated = False
        self.highlighted = False

        self.direction = t  # 1 or -1
        self.absolute_rect = {}
        if self.direction == 1:
            self.absolute_rect["pos"] = [parent_rect.topright[0] - self.rect.width, parent_rect.y]
        if self.direction == -1:
            self.absolute_rect["pos"] = [parent_rect.topright[0] - self.rect.width, parent_rect.y + 10]

        self.absolute_rect["topright"] = [self.absolute_rect["pos"][0] + self.rect.width,
                                          self.absolute_rect["pos"][1]]
        self.absolute_rect["topleft"] = self.absolute_rect["pos"]
        self.absolute_rect["bottomright"] = [self.absolute_rect["pos"][0] + self.rect.width,
                                             self.absolute_rect["pos"][1] + self.rect.height]
        self.absolute_rect["bottomleft"] = [self.absolute_rect["pos"][0],
                                            self.absolute_rect["pos"][1] + self.rect.height]
        self.absolute_rect["center"] = [int(self.absolute_rect["bottomleft"][0] - self.absolute_rect["pos"][0] / 2),
                                        int(self.absolute_rect["bottomleft"][1] - self.absolute_rect["pos"][1] / 2)]

    def check(self, event_list):
        pos = pygame.mouse.get_pos()
        vnt_type = [event.type for event in event_list]
        deactivated = False
        if self.absolute_rect["pos"][0] <= pos[0] <= self.absolute_rect["topright"][0] and \
                self.absolute_rect["pos"][1] <= pos[1] <= self.absolute_rect["bottomleft"][1]:
            if pygame.MOUSEBUTTONDOWN in vnt_type:
                self.activated = True
                self.highlighted = False
                logger.debug("Spinbutton Activated")
            elif pygame.MOUSEBUTTONUP in vnt_type and self.activated:
                self.activated = False
                self.highlighted = True
                logger.debug("Spinbutton Deactivated")
                deactivated = True
            elif pygame.MOUSEBUTTONUP not in vnt_type and self.activated:
                self.activated = True
                self.highlighted = False
            else:
                self.activated = False
                self.highlighted = True
        elif not self.absolute_rect["pos"][0] <= pos[0] <= self.absolute_rect["topright"][0] or not \
                self.absolute_rect["pos"][1] <= pos[1] <= self.absolute_rect["bottomleft"][1]:
            self.activated = False
            self.highlighted = False

        if self.activated:
            self.image.fill(color.SPIN_BUTTON_ACTIVATED_COLOR.get(tuple))
        elif self.highlighted:
            self.image.fill(color.SPIN_BUTTON_HIGHLIGHTED_COLOR.get(tuple))
        else:
            self.image.fill(color.SPIN_BUTTON_DEFAULT_COLOR.get(tuple))

        if self.direction == 1:  # Up
            pygame.draw.polygon(self.image, color.SPIN_BUTTON_TRIANGLE_DEFAULT_COLOR.get(tuple),
                                [[2, 8], [8, 8], [5, 2], [6, 2]])
        elif self.direction == -1:  # Down
            pygame.draw.polygon(self.image, color.SPIN_BUTTON_TRIANGLE_DEFAULT_COLOR.get(tuple),
                                [[2, 2], [8, 2], [5, 8], [6, 8]])
        return deactivated
