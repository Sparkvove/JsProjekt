import pygame
import ui
import game
if __name__ == '__main__':
    pygame.init()
    counter = ui.Counter()
    GAME = game.Game()
    GAME.set_game_caption()
    game.application(GAME, counter)
    pygame.quit()
