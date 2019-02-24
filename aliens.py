import pygame
import random
from settings import *

unhit = 'notcrying.png'
hit = 'crying.png'


class alien:
    def __init__(self, start):
        self.timer = 8
        self.start = start
        self.x = random.randrange(50, dis_width - 50)
        self.y = random.randrange(0.125 * dis_height, 0.25 * dis_height)
        self.destroy = False
        self.hit = False
        self.flag = False

    def first(self):
        self.destroy = True

    def second(self, hit_time):
        self.timer = 5
        self.hit = True
        self.hit_time = hit_time
        self.flag = True

    def draw(self):
        if self.flag is True:
            self.image = pygame.image.load(hit)
        else:
            self.image = pygame.image.load(unhit)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        gameDisplay.blit(self.image, self.rect)
