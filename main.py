import pygame
import ui
import Towary
from pygame.locals import *

pygame.init()

screen = ui.screen
pygame.display.set_caption('Symulacja Kasjera')

counter = ""
stateOfGame = 'GAME'
menuState = True

run = True
while run:
    screen.fill(ui.bg)
    if stateOfGame == 'GAME':
        counter, menuState, stateOfGame = ui.show_game_screen(counter, menuState, stateOfGame)
    elif stateOfGame == 'GAMEOVER':
        counter, menuState, stateOfGame = ui.show_game_over_screen(counter, menuState, stateOfGame)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
