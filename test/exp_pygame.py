
import pygame
import os
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Animal(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, colour = BLACK, size = 5, velocity = [0, 0] ):
        super.__init__()
        pass


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
