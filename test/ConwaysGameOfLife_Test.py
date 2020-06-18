
import pygame

from Game_Window_class import Game_Window

WIDTH, HEIGHT = 850, 640
GREY = (224, 224, 224)

BACKGROUND = GREY

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game Of Life")

pygame.init()

clock = pygame.time.Clock()

def main():
    RUN = True
    FPS = 120

    # if WIDTH = 850, (15*WIDTH)//17 = 750. 750 / 30 = 25
    # if HEIGHT = 640, (4.5 * HEIGHT)//6 = 480. 480 / 30 = 16
    # which implyes we can have (25 * 16) cells
    game_window = Game_Window(WINDOW, WIDTH//17, HEIGHT//6, (15*WIDTH)//17, (4.5 * HEIGHT)//6, background=(0, 0, 0))
    
    def update():
        game_window.update()
    
    def draw():
        WINDOW.fill(BACKGROUND)
        game_window.draw()
    
    while RUN:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        update()
        draw()
        pygame.display.flip()
main()
pygame.quit()
