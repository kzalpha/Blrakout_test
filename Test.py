#!/opt/local/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import os
import sys

SCR_RECT = Rect(0, 0, 1024, 768)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCR_RECT.size)) #Window size
    pygame.display.set_caption("Break Block")

    all = pygame.sprite.RenderUpdates()
    Paddle.containers = all
    paddle = Paddle()
    clock = pygame.time.Clock()

    while True:
    	clock.tick(60)
        screen.fill((0,0,0))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWn and event.key == K_ESCAPE:
            	pygame.quit()
            	sys.exit()
