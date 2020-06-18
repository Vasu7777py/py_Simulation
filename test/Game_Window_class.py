
import pygame
vector = pygame.math.Vector2

class Game_Window:
    def __init__(self, window, x, y, width, height, name = "Game" ,background = (224, 224, 224)):
        self.name = name
        self.position = vector(x, y)

        self.window = window
        self.width = width
        self.height = height
        self.screen = pygame.Surface((self.width, self.height))
        self.background = background
        self.rect = self.screen.get_rect()


    def update(self):
        self.rect.topleft = self.position

    def draw(self):
        self.screen.fill(self.background)
        self.window.blit(self.screen, (self.position.x, self.position.y))
