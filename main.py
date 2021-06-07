import pygame
import ui
import Towary
from pygame.locals import *

pygame.init()

window = ui.screen.PrintScreen()

counter = ui.counter()

pygame.display.set_caption('Symulacja Kasjera')

curr_towar = 0

stateOfGame = 'GAME'
menuState = True
run = True
while run:
    window.fill(ui.screen.bg)
    if stateOfGame == 'GAME':

        counter, menuState, stateOfGame, curr_towar = ui.show_game_screen(counter, menuState, stateOfGame, curr_towar)

        if curr_towar == Towary.how_many_towar - 1:
            stateOfGame = 'GAMEWIN'

    elif stateOfGame == 'GAMEOVER':
        counter, menuState, stateOfGame, curr_towar = ui.show_game_over_screen(counter, menuState, stateOfGame, curr_towar)

    elif stateOfGame == 'GAMEWIN':
        counter, menuState, stateOfGame, curr_towar = ui.show_game_win_screen(counter, menuState, stateOfGame, curr_towar)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
