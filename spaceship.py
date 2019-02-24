import pygame
from settings import *
from missile import *


class spaceship:
    def __init__(self):
        self.x = dis_width / 2
        self.y = dis_height - 25
        self.coor = (self.x, self.y)

    def missile(self, type):
        mis = missile(self.x, self.y - 100, type)
        return mis

    def draw(self):
        self.image = pygame.image.load('space.png')
        self.rect = self.image.get_rect()
        screen_rect = gameDisplay.get_rect()
        self.rect.centerx = self.x
        self.rect.bottom = screen_rect.bottom
        gameDisplay.blit(self.image, self.rect)
