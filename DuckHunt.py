#!/usr/bin/env python

import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

pre = (0, 0, 0)
color = (255, 255, 255)

screen = pygame.display.set_mode((890, 550), 0, 32)


pygame.display.set_caption("Duck Hunt")


x_pos = 0
y_pos = 0


x_click = 0
y_click = 0


x_duck = 0
y_duck = randint(0, 450)

points = 0
velocity = 2
error = False


pygame.mixer.init(44100, -16, 2, 1024)

pygame.mixer.music.set_volume(0.8)

while True:
    for event in pygame.event.get():
        
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEMOTION:
            x_pos, y_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONDOWN:
            x_click, y_click = pygame.mouse.get_pos()

    pos = (x_pos - 50, y_pos - 50)

    x_duck += 1

    if x_duck * velocity > 890 and not error:
        x_duck = 0
        y_duck = randint(0, 450)

        
        pygame.mixer.music.load("gameover.mp3")
        pygame.mixer.music.play()

        error = True

   
    screen.fill(pre)
    pygame.mouse.set_visible(False)


    screen.blit(pygame.image.load("background.png"), (0, 0))
    screen.blit(pygame.font.SysFont("Times", 44).render("Points: " + str(points), True, color), (600, 50))

 
    if x_click in range(x_duck * velocity - 30, x_duck * velocity + 30) and y_click in range(y_duck - 30, y_duck + 30):

        pygame.mixer.music.load("hit.mp3")
        pygame.mixer.music.play()

        points += 1
        velocity += 1
        x_duck = 0
        y_duck = randint(50, 500)

    screen.blit(pygame.image.load("duck.gif"), (x_duck * velocity, y_duck))

    if error:
        x_duck = -50
        y_duck = -50
        screen.blit(pygame.image.load("dog.gif"), (400, 340))

    screen.blit(pygame.image.load("aim.gif").convert(), pos)

    pygame.display.update()
