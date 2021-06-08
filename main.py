import pygame
import ui
import game

pygame.init()
counter = ui.counter()
GAME = game.Game()
GAME.SetGameCaption()
game.application(GAME, counter)
pygame.quit()
