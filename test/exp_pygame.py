
import pygame
import os
import time

WIDTH, HEIGHT = (750, 450)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("...Simulation...")

pygame.init()

os.system("cls")

def main():
    run = True
    FPS = 120
    clock = pygame.time.Clock()

    def redraw_window():
        pass

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                run = False

main()
