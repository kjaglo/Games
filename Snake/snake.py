import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0

    def __init__(self):
        pass


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):  # index and cube object
            p = c.position[:]
            if p in self.turns: # if position is in the turns
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body):
                    self.turns.pop(p)


def drawGrid(w, rows, surface):
    sizeBtwn = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # vertical line
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # horizontal line


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


def main():
    global rows, width
    width = 500
    rows = 20

    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))
    flag = True
    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)  # the lower delay is the faster snake is going to be
        clock.tick(10)  # snake moves 10 blocks in 1 sec, the lower this one goes the faster snake is going to be
        redrawWindow(win)


main()
