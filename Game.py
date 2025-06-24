from Square import *
import random

class Game():
    START_LEFT = 35
    START_TOP = 35

    def __init__(self, window):
        self.window = window
        LEGAL_MOVES_DICT = {
            0: (1,3),
            1: (0,2,4),
            2: (1,5),
            3: (0,4,6),
            4: (1,3,5,7),
            5: (2,4,8),
            6: (3,7),
            7: (4,6,8),
            8: (5,7)
        }

        yPos = Game.START_TOP
        self.squaresList = []

        for row in range(0, 3):
            xPos = Game.START_LEFT
            for col in range(0, 3):
                squareNumber = (row * 3) + col
                legalMovesTuple = LEGAL_MOVES_DICT[squareNumber]
                oSquare = Square(self.window, xPos, yPos, squareNumber, legalMovesTuple)
                self.squaresList.append(oSquare)
                xPos += SQUARE_WIDTH
            yPos += SQUARE_HEIGHT

        self.soundTick = pygame.mixer.Sound('sounds/tick.wav')
        self.soundApplause = pygame.mixer.Sound('sounds/applause.wav')
        self.soundNope = pygame.mixer.Sound('sounds/nope.wav')

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        for oSquare in self.squaresList:
            oSquare.reset()

        self.oOpenSquare = self.squaresList[STARTING_OPEN_SQUARES]

        for i in range(0, 200):
            legalMovesForThisTile = self.oOpenSquare.getLegalMoves()
            nextMoveNumber = random.choice(legalMovesForThisTile)
            oSquare = self.squaresList[nextMoveNumber]

            self.switch(oSquare, playMoveSound=False)

        self.playing = True

    def gotClick(self, clickLoc):
        if not self.playing:
            return

        for oSquare in self.squaresList:
            if oSquare.clickedInside(clickLoc):
                squareNumber = oSquare.getSquareNumber()
                legalMovesForOpenSquare = self.oOpenSquare.getLegalMoves()
                legalMove = squareNumber in legalMovesForOpenSquare

                if legalMove:
                    self.switch(oSquare, playMoveSound=True)
                else:
                    self.soundNope.play()
                return

    def switch(self, oSquareToSwitch, playMoveSound=False):
        oSquareToSwitch.switch(self.oOpenSquare)
        self.oOpenSquare = oSquareToSwitch

        if playMoveSound:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False

        for oSquare in self.squaresList:
            if not oSquare.isTIleInProperPlace():
                return False

        self.playing = False
        self.soundApplause.play()
        return True

    def getGamePlaying(self):
        return self.playing

    def stopPlaying(self):
        self.playing = False

    def draw(self):
        for oSquare in self.squaresList:
            oSquare.draw()