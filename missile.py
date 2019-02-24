import pygame
from settings import *


class missile:
    def __init__(self, x, y, start):
        self.y_ini = y
        self.x = x
        self.y = y
        #self.type = ty
        self.start = start
        self.destroy = False

    def draw(self):
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        gameDisplay.blit(self.image, self.rect)


class missile1(missile):
    def __init__(self, x, y, start):
        self.ty = 1
        super().__init__(x, y, start)

    def draw(self):
        self.y = self.y_ini - (missile_speed) * \
            (time() / 1000 - self.start)
        self.image = myfont.render('i', False, white)
        super().draw()


class missile2(missile):
    def __init__(self, x, y, start):
        self.ty = 2
        super().__init__(x, y, start)

    def draw(self):
        self.y = self.y_ini - (2 * missile_speed) * \
            (time() / 1000 - self.start)
        self.image = myfont.render('l', False, white)
        super().draw()
