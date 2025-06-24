import pygame
from Constants import *
from Tile import *

class Square():
    def __init__(self, window, left, top, squareNumber, legalMovesTuple):
        self.window = window
        self.rect = pygame.Rect((left, top, SQUARE_WIDTH, SQUARE_HEIGHT))
        self.squareNumber = squareNumber
        self.legalMovesTuple = legalMovesTuple
        self.loc = (left, top)
        self.reset()

    def reset(self):
        self.oTile = Tile(self.window, self.squareNumber)

    def isTIleInProperPlace(self):
        tileNumber = self.oTile.getTileNumber()
        return tileNumber == self.squareNumber

    def getLegalMoves(self):
        return self.legalMovesTuple

    def clickedInside(self, mouseLoc):
        hit = self.rect.collidepoint(mouseLoc)
        return hit

    def getSquareNumber(self):
        return self.squareNumber

    def switch(self, oOtherSquare):
        self.oTile, oOtherSquare.oTile = oOtherSquare.oTile, self.oTile

    def draw(self):
        self.oTile.draw(self.loc)