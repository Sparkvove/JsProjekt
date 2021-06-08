import pygame
import ui
import Towary
import game
from datetime import datetime
import random
pygame.init()
counter = ui.counter()
GAME = game.Game()
GAME.SetGameCaption()

while GAME.run:
    GAME.window.fill(GAME.screen.bg)
    if GAME.stateOfGame == 'GAME':
        counter, GAME = game.show_game_screen(counter, GAME)

        if GAME.curr_towar == Towary.how_many_towar - 1:
            GAME.timerStop = datetime.now()
            GAME.stateOfGame = 'GAMEWIN'

    elif GAME.stateOfGame == 'GAMEOVER':
        counter, GAME = game.show_game_over_screen(counter, GAME)

    elif GAME.stateOfGame == 'GAMEWIN':
        counter, GAME = game.show_game_win_screen(counter, GAME)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME.run = False

    pygame.display.update()

pygame.quit()
