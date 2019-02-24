import pygame
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
dis_height = 400
dis_width = 400
gameDisplay = pygame.display.set_mode((dis_width, dis_height))
time = pygame.time.get_ticks
clock = pygame.time.Clock()
missile_speed = 50
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 25)
freq = 10
