
import pygame
Vector = pygame.math.Vector2

class Cells:
    def __init__(self, screen, x, y, width, height, background = (224, 224, 224), foreground= (127, 0, 255)):
        self.position = Vector(x, y)
        
        self.alive = False

        self.width, self.height = width, height
        self.screen = screen
        self.cell = pygame.Surface((self.width, self.height))
        self.background, self.foreground = background, foreground
        self.rect = self.cell.get_rect()

    def update(self):
        self.rect.topleft = self.position

    def draw(self):
        self.cell.fill(self.foreground)
        self.screen.blit(self.cell, (self.position.x*30, self.position.y*30))

