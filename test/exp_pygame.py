
import pygame
import os
import time
import random
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MENGENTA = (204, 0, 204)

BACKGROUND = WHITE

WIDTH, HEIGHT = (750, 450)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("...Simulation...")

class Person(pygame.sprite.Sprite):
    def __init__(self, x, y, colour = MENGENTA, radius = 5, velocity = [0, 0] ):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([radius*2, radius*2])
        self.image.fill(BACKGROUND)
        pygame.draw.circle(self.image, colour, (radius, radius), radius)

        self.rect = self.image.get_rect()
        self.position = np.array([x, y], dtype = np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)
        
    def update(self):

        self.position += self.velocity
        
        x, y = self.position
        
        if x < 0:
            self.velocity[0] *= -1
            x = 0
        if x > WIDTH:
            self.velocity[0] *= -1
            x = WIDTH
        if y < 0:
            self.velocity[1] *= -1
            y = 0
        if y > HEIGHT:
            self.velocity[1] *= -1
            y = HEIGHT

        self.rect.x = x
        self.rect.y = y

pygame.init()

container = pygame.sprite.Group()

for _ in range(25):
    x = np.random.randint(0, WIDTH + 1)
    y = np.random.randint(0, HEIGHT + 1)
    velocity = np.random.rand(2) *2 -1
    person = Person(x, y, velocity=velocity)
    container.add(person)

os.system("cls")

def main():
    run = True
    FPS = 120
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                run = False
        
        container.update()
        WINDOW.fill(BACKGROUND)
        container.draw(WINDOW)
        pygame.display.flip()

        clock.tick(FPS)

main()
pygame.quit()

#os.system("exit")
