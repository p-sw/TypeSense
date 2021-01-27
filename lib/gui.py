import pygame
from lib.Gui.Base import color
from lib.Gui.checkbox import Checkbox
from lib import logger
from lib.Gui.slider import Slider
from lib.Gui.label import Label
from lib.Gui.spinbox import Spinbox
from lib import globalvar


class GUI:
    def __init__(self):
        self.stopped = False
        pygame.init()
        self.window_w = 400
        self.window_h = 500
        self.display = pygame.display.set_mode((400, 500))
        logger.info("Display initialized")
        pygame.display.set_caption(globalvar.APPNAME)
        self.clock = pygame.time.Clock()

        # GUI Sprite Init
        self.AutoTypeEnable = Checkbox(10, 20, "AutoType", 15)
        self.AutoTypeKeyDelay = Slider(10, 60, 200, "KeyDelay", 15, "s", 0.005, 0.001, 0.5, 3)
        self.AutoTypeReturnDelay = Slider(10, 100, 200, "ReturnDelay", 15, "s", 0.2, 0.001, 0.5, 3)
        self.AutoHackMsgEnable = Checkbox(10, 130, "AutoHackMessage", 15)
        """
        self.AutoTarget = Checkbox(10, 150, "AutoTarget", 15)
        self.TargetPriority = Spinbox(10, 185, 200,
                                      ["First in player list", "Last in player list", "Random"],
                                      "Target Priority", 15)
        """
        self.AutoPort = Checkbox(10, 150, "AutoPort", 15)
        self.PortSelection = Spinbox(10, 250, 200,
                                     ["PORT A", 'PORT B', 'PORT C', 'Random'],
                                     "Port Selection", 15)

        self.CreditLabel = Label(12, "Made by SSerVe, Build {} {}".format(globalvar.VERSION, globalvar.APPTYPE))
        self.CreditLabel.get_rect().centerx = int(self.window_w / 2)
        self.CreditLabel.get_rect().centery = self.window_h - 25

        self.interactive_sprite_group = pygame.sprite.Group()
        self.interactive_sprite_group.add(self.AutoTypeEnable)
        self.interactive_sprite_group.add(self.AutoTypeKeyDelay)
        self.interactive_sprite_group.add(self.AutoTypeReturnDelay)
        self.interactive_sprite_group.add(self.AutoHackMsgEnable)
        self.interactive_sprite_group.add(self.AutoPort)
        self.interactive_sprite_group.add(self.PortSelection)
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
                s_obj.check(vnt)

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
