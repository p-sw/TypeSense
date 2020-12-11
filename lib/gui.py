import pygame
from lib.Gui.Base import color
from lib.Gui.button import Button
from lib import logger
from lib.Gui.slider import Slider
from lib.Gui.label import Label
from lib import globalvar


class GUI:
    def __init__(self):
        self.stopped = False
        pygame.init()
        self.display = pygame.display.set_mode((400, 200))
        logger.info("Display initialized")
        pygame.display.set_caption(globalvar.APPNAME)
        self.clock = pygame.time.Clock()

        # GUI Sprite Init
        self.AutoTypeEnable = Button(10, 20, "AutoType", 15)
        self.AutoTypeKeyDelay = Slider(10, 60, 200, "KeyDelay", 15, "s", 0.005, 0.001, 0.5, 3)
        self.AutoTypeReturnDelay = Slider(10, 100, 200, "ReturnDelay", 15, "s", 0.1, 0.001, 0.5, 3)
        self.AutoHackMsgEnable = Button(10, 130, "AutoHackMessage", 15)
        self.CreditLabel = Label(12, "Made by SSerVe, Build {} {}".format(globalvar.VERSION, globalvar.APPTYPE))

        self.CreditLabel.get_rect().centerx = 200
        self.CreditLabel.get_rect().centery = 180

        self.interactive_sprite_group = pygame.sprite.Group()
        self.interactive_sprite_group.add(self.AutoTypeEnable)
        self.interactive_sprite_group.add(self.AutoTypeKeyDelay)
        self.interactive_sprite_group.add(self.AutoTypeReturnDelay)
        self.interactive_sprite_group.add(self.AutoHackMsgEnable)
        logger.info("GUI Initialized")

    def run(self):
        while not self.stopped:
            vnt = pygame.event.get()
            for event in vnt:
                self.event_handler(event)
            self.display.fill(color.HEAVY_BLACK.get(tuple))

            # do draw & update thing
            self.interactive_sprite_group.update()
            for s_obj in self.interactive_sprite_group:
                s_obj.check(vnt, self.display)

            self.interactive_sprite_group.draw(self.display)

            for s_obj in self.interactive_sprite_group:
                s_obj.font_draw(self.display)

            self.display.blit(self.CreditLabel.get_text(), self.CreditLabel.get_rect())

            pygame.display.update()
            self.clock.tick(30)

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            logger.debug("QUIT Event")
            self.stopped = True
