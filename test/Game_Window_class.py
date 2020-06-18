
import pygame
vector = pygame.math.Vector2

from cells import Cells

class Game_Window:
    def __init__(self, window, x, y, width, height, name = "Game" ,background = (224, 224, 224)):
        self.name = name
        self.position = vector(x, y)
        self.window = window
        self.width = width
        self.height = height
        self.screen = pygame.Surface((self.width, self.height))
        self.grid = [[Cells(self.screen, x, y, 30, 30) for x in range(16)] for y in range(25)]
        self.background = background
        self.rect = self.screen.get_rect()


    def update(self):
        self.rect.topleft = self.position
        for row in self.grid:
            for cell in row:
                cell.update()

    def draw(self):
        self.screen.fill(self.background)
        self.window.blit(self.screen, (self.position.x, self.position.y))
        for row in self.grid:
            for cell in row:
                cell.draw()
                #print(cell.foreground, self.position)
