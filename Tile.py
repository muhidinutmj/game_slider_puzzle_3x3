import pygame
from Constants import *

pygame.init()
pygame.font.init()

class Tile():
    font = pygame.font.SysFont(None, 60)
    def __init__(self, window, tileNumber):
        self.window = window
        self.tileNumber = tileNumber

        surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
        if self.tileNumber == STARTING_OPEN_SQUARES:
            surface.fill(COLOR5)
            pygame.draw.rect(surface, COLOR1, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)), 2)
        else:
            surface.fill(COLOR3)
            pygame.draw.rect(surface, COLOR1, pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)), 2)
            centerX = SQUARE_WIDTH // 2
            centerY = SQUARE_HEIGHT // 2
            pygame.draw.circle(surface, COLOR4, (centerX, centerY), 35)
            numberAsImage = Tile.font.render(str(self.tileNumber + 1), True, COLOR1)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (SQUARE_WIDTH - widthOfNumber) // 2
            heightOfNumber = numberAsImage.get_height()
            topPos = (SQUARE_HEIGHT - heightOfNumber) // 2
            surface.blit(numberAsImage, (leftPos, topPos))

        self.image = surface

    def getTileNumber(self):
        return self.tileNumber

    def draw(self, loc):
        self.window.blit(self.image, loc)