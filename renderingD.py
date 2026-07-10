# import the pygame module for graphics rendering
import pygame
from pygame.locals import *

# initialize the pygame module
pygame.init()

# create separate window for the simulation
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("COLLISION SIMULATOR")

# main loop for the simulation
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255)) # blank white background
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 200, 150), 5)
    pygame.display.flip()

pygame.quit()