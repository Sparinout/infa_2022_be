import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

#фон
circle(screen, (128, 128, 128), (200, 175), 1250)

#тело
circle(screen, (255, 255, 0), (200, 175), 125)
circle(screen, (0, 0, 0), (200, 175), 125, 5)

#глаза
circle(screen, (255, 0, 0), (250, 150), 20)
circle(screen, (0, 0, 0), (250, 150), 20, 3)
circle(screen, (0, 0, 0), (250, 150), 10)

circle(screen, (255, 0, 0), (150, 150), 30)
circle(screen, (0, 0, 0), (150, 150), 30, 3)
circle(screen, (0, 0, 0), (150, 150), 15)

#губы
rect(screen, (0, 0, 0), (140, 230, 120, 25))

polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()