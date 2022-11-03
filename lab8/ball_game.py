import pygame
from pygame.draw import *
import random

pygame.init()

FPS = 60
screen = pygame.display.set_mode((900, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball1():
    global x, y, r, color
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    r = random.randint(30, 50)
    color = COLORS[random.randint(0, 5)]
    circle(screen, color, (x, y), r)


def new_ball2():
    global x, y, r, color
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    r = random.randint(30, 50)
    color = COLORS[random.randint(0, 5)]
    rect(screen, color, (x-r/2, y-r/2, r, r))


def helper():
    global v_x1, v_y1, v_x2, v_y2
    if (x1 + r1 >= 900 and v_x1 >= 0):
        v_x1 = random.uniform(-v, 0)
    elif (y1 + r1 >= 700 and v_y1 >= 0):
        v_y1 = random.uniform(-v, 0)
    elif (x1 - r1 <= 0 and v_x1 <= 0):
        v_x1 = random.uniform(0, v)
    elif (y1 - r1 <= 0 and v_y1 <= 0):
        v_y1 = random.uniform(0, v)

    if (x2 + r2 >= 900 and v_x2 >= 0):
        v_x2 = random.uniform(-v, 0)
    elif (y2 + r2 >= 700 and v_y2 >= 0):
        v_y2 = random.uniform(-v, 0)
    elif (x2- r2 <= 0 and v_x2 <= 0):
        v_x2 = random.uniform(0, v)
    elif (y2 - r2 <= 0 and v_y2 <= 0):
        v_y2 = random.uniform(0, v)


def timer(time):
    time += 1
    if (time == 40):
        save_ball()
        vector_v()
        time = 0
    return(time)


def vector_v():
    global v_x1, v_y1, v_x2, v_y2
    global v
    v = 5
    v_x1 = random.uniform(-v, v)
    v_y1 = random.uniform(-v, v)
    v_x2 = random.uniform(-2.5*v, 2.5*v)
    v_y2 = random.uniform(-2.5*v, 2.5*v)


def save_ball():
    global x1, x2, y1, y2, r1, r2, color1, color2
    new_ball1()
    color1 = color
    x1 = x
    y1 = y
    r1 = r

    new_ball2()
    color2 = color
    x2 = x
    y2 = y
    r2 = r


def dvizhenie():
    global x1, y1, x2, y2
    x1 += v_x1
    y1 += v_y1
    v_x2 = random.uniform(-2.5*v, 2.5*v)
    v_y2 = random.uniform(-2.5*v, 2.5*v)
    x2 += v_x2
    y2 += v_y2
    circle(screen, color1, (x1, y1), r1)
    rect(screen, color, (x2-r2/2, y2-r2/2, r2, r2))
    pygame.display.update()


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
save_ball()
vector_v()
time = 0


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ((((event.pos[0] - x1) ** 2 + (event.pos[1] - y1) ** 2) < r1 ** 2) or
                    (abs(event.pos[0] - x2) < r2/2 and abs(event.pos[1] - y2) < r2/2)):
                score += 1
            print("score :", score)

    pygame.display.update()
    screen.fill(BLACK)
    dvizhenie()
    helper()
    time = timer(time)


pygame.quit()
