import pygame
import ui
import game
if __name__ == '__main__':
    pygame.init()
    counter = ui.counter()
    GAME = game.Game()
    GAME.SetGameCaption()
    game.application(GAME, counter)
    pygame.quit()
