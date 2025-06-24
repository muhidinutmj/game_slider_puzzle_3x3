# 1 import modul
import pygame
from pygame.locals import *
import pygwidgets
import pyghelpers
import sys
from Game import *

# 2 definisi konstanta
WINDOW_WIDTH = 370
WINDOW_HEIGHT = 460
FRAMES_PER_SECOND = 30

# 3 inisialisasi modul
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 load assets
restartButton = pygwidgets.CustomButton(window, (240, 355), up='images/restartButtonUp.jpg', down='images/restartButtonDown.jpg', over='images/restartButtonOver.jpg')

# 5 inisialisasi variabel
clock = pygame.time.Clock()
timerDisplay = pygwidgets.DisplayText(window, (50, 365), '', fontSize=30, textColor=COLOR2)
messageDisplay = pygwidgets.DisplayText(window, (50, 410), 'Klik dijudul untuk dipindahkan', fontSize=29, textColor=COLOR2)

oGame = Game(window)
soundBuzz = pygame.mixer.Sound('sounds/buzz.wav')

oCountDownTimer = pyghelpers.CountDownTimer(TIMER_LENGTH)
oCountDownTimer.start()

# 6 main loop
while True:
    # 7 event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Selamat, Anda Menang!')
                oCountDownTimer.stop()

        if restartButton.handleEvent(event):
            oGame.startNewGame()
            oCountDownTimer.start()

    # 8 update model
    timeToShow = oCountDownTimer.getTimeInHHMMSS(2)
    timerDisplay.setValue('Waktu: ' + timeToShow)
    if oGame.getGamePlaying():
        if oCountDownTimer.ended():
            soundBuzz.play()
            messageDisplay.setText('Waktu Habis')
            oGame.stopPlaying()

    # 9 update view
    window.fill(COLOR1)

    oGame.draw()
    restartButton.draw()

    timerDisplay.draw()
    messageDisplay.draw()

    # 10 update frame
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)