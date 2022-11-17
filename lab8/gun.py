import math
import random
from random import choice

import pygame

FPS = 60

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 300

    def move(self, dt):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        self.vy += dt/2
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.y + self.r >= HEIGHT and self.vy > 0:
            self.vy = -0.5*self.vy
            self.y = HEIGHT - self.r
        if self.x + self.r >= WIDTH and self.vx >= 0:
            self.vx = -0.5*self.vx
            self.x = WIDTH - self.r
        if self.x - self.r <= 0 and self.vx <= 0:
            self.vx = -0.5*self.vx
            self.x = self.r
        if (self.live < 0):
            balls.pop(balls.index(self))
        else:
            self.live-=1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )
        pygame.draw.circle(
            self.screen,
            (0, 0, 0),
            (self.x, self.y),
            self.r, 1
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        # return False
        if ((obj.x - self.x)**2 + (obj.y - self.y)**2)**0.5 <= (self.r + obj.r):
            return True
        else:
            return False



class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        for i in range (0, 4):
            new_ball = Ball(self.screen)
            new_ball.r = 3
            new_ball.vx = (self.f2_power) * math.cos(self.an + random.uniform(-0.1, 0.1))
            new_ball.vy = (self.f2_power) * math.sin(self.an + random.uniform(-0.1, 0.1))
            balls.append(new_ball)

        self.f2_on = 0
        self.f2_power = 10


    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan2((event.pos[1] - 450), (event.pos[0] - 20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it
        if self.f2_on:
            pygame.draw.line(self.screen, "orange", (40, 450), (40 + (80 + self.f2_power) * math.cos(self.an), 450 + (80 + self.f2_power) * math.sin(self.an)), 15)
        else:
            pygame.draw.line(self.screen, "black", (40, 450), (40 + (80 + self.f2_power) * math.cos(self.an), 450 + (80 + self.f2_power) * math.sin(self.an)), 15)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()

    def __init__(self):
        self.new_target()
        self.points = 0


    def start(self):
        self.points = 0
        self.live = 1
        self.new_target()


    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.uniform(600, 780)
        self.y = random.uniform(300, 550)
        self.r = random.uniform(10, 50)
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-5, 5)
        self.color = RED
        self.live = True

    def hit(self):
        """Попадание шарика в цель."""
        self.points += 1

    def hit_count(self):
        return self.points

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.y + self.r >= HEIGHT and self.vy >= 0:
            self.vy = -self.vy
        if self.x + self.r >= WIDTH and self.vx >= 0:
            self.vx = -self.vx
        if self.x - self.r <= 0 and self.vx <= 0:
            self.vx = -self.vx
        if self.y - self.r <= 0 and self.vy <= 0:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 2)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
targets = []
number_of_targets = 2
clock = pygame.time.Clock()
gun = Gun(screen)

for i in range(number_of_targets):
    targets.append(Target())

finished = False
font = pygame.font.SysFont(None, 24)
dt = 1
name = input("Your name: ")

while not finished:

    clock.tick(FPS)
    screen.fill(WHITE)
    gun.draw()

    for t in targets:
        t.draw()
        t.move(dt)

    for b in balls:
        b.draw()

    temp1 = 0
    for t in targets:
        temp1 += t.hit_count()
    temp = "Счет: " + str(temp1)
    img = font.render(temp, True, (0, 0, 0), (255, 255, 255))
    screen.blit(img, (20, 20))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move(dt)
        for t in targets:
            if b.hittest(t) and t.live:
                t.live = False
                t.hit()
                t.new_target()
    gun.power_up()

    pygame.display.update()

f = open("text.txt", "a")
f.writelines(name + ": " + str(temp1) + '\n')

pygame.quit()
