import pygame
from pygame.draw import *
from random import random
import math

X = 1200
Y = 600


def mountain_generator(delta, x_size, y_size):
    '''
    Функция, рисующая горы
    :param delta: характерный размер, масштаб гор
    :param x_size: длина гор по оси x
    :param y_size: максимально возможная высота гор по оси y
    '''
    points = []
    x = 0
    y = 0
    sign = 1
    while x < x_size:
        points.append((x, max(1, y)))
        x += random()*delta
        y += sign * random() * delta
        if y > random()*y_size:
            sign = -sign
        if y < 0: sign = 1
        if y > y_size: y = y_size
    points.append((x_size,0))
    return points


def bird_generator(size):
    '''
    Функция, рисующая птиц
    :param size: - размер птицы
    '''
    x = [0.1*j for j in range (-40, 41)]
    points = []
    for j in range(len(x)):
       points.append((size * x[j], size * math.sqrt(math.fabs(x[j]))))
    for j in range(len(x)):
       points.append((size * x[::-1][j], size * (0.75 * math.sqrt(math.fabs(x[::-1][j])) + 0.5)))
    return points


pygame.init()

FPS = 30
screen = pygame.display.set_mode((X, Y))
r_sun = Y/10
mount_color = [(252, 153, 45), (173, 65, 49), (44, 7, 33)]
sky_color =[(254, 214, 163), (254, 214, 197), (254, 214, 163), (180, 135, 149)]

for i in range (0, 3):
    rect(screen, sky_color[i], (0, i*0.225*Y, X, 0.225*Y))
rect(screen, sky_color[3], (0, 0.675*Y, X, 0.325*Y))

circle(screen, (252, 239, 27), (X/2, Y/4), r_sun)

polygon(screen, mount_color[0], [(x, 0.45*Y-y) for (x, y) in mountain_generator(10, X, Y/6)], 0)
polygon(screen, mount_color[1], [(x, 0.675*Y-y) for (x, y) in mountain_generator(20, X, Y/4)], 0)
polygon(screen, mount_color[2], [(x, Y-y) for (x, y) in mountain_generator(30, X, Y/2)], 0)


num_birds = 9
for i in range(num_birds):
    x0 = random() * X
    y0 = random() * (Y-100)
    size = random()*Y/40
    polygon(screen, (64, 27, 3), [(x0+x, y0-y) for (x, y) in bird_generator(size)], 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
