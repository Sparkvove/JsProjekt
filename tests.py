
import unittest
import Towary
import pygame
import ui
from game import Game
import game


def create_game(counter_value, mode):
    pygame.init()
    testing_game = Game()
    counter = ui.Counter()
    testing_game.set_game_caption()
    testing_game.menuState = False
    p1 = Towary.TowarNaSztuki()
    p2 = Towary.TowarNaSztuki()
    p1.how_many = 20
    testing_game.towar_list = [p1, p2]
    counter.value = counter_value

    while testing_game.run:
        testing_game.window.fill(testing_game.screen.bg)
        if testing_game.stateOfGame == 'GAME':
            counter, testing_game = game.show_game_screen(counter, testing_game, True, mode)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                testing_game.run = False
                pygame.quit()

        pygame.display.update()

    return counter, testing_game


class TestGame(unittest.TestCase):

    def test_scanning_towar_na_sztuki_by_clicking_few_times(self):
        counter, testing_game = create_game('1', 1)
        self.assertEqual(testing_game.curr_towar, 1)

    def test_scanning_towar_na_sztuki_by_clicking_one_time(self):
        counter, testing_game = create_game('20', 1)
        self.assertEqual(counter.value, '1')

    def test_scanning_towar_na_sztuki_by_clicking_one_time_and_exceed_value(self):
        counter, testing_game = create_game('40', 1)
        self.assertEqual(testing_game.stateOfGame, 'GAMEOVER')

    def test_weight_towar_na_sztuki(self):
        counter, testing_game = create_game('40', 2)
        self.assertEqual(testing_game.stateOfGame, 'GAMEOVER')

    def test_win_game(self):
        counter, testing_game = create_game('20', 1)
        self.assertEqual(testing_game.stateOfGame, 'GAMEWIN')

    def test_check_if_values_equals_one_enough_times(self):
        ilosc_liczb = 100
        licznik = 0
        for x in range(ilosc_liczb):
            y = Towary.TowarNaSztuki.get_how_many()
            if y == 1:
                licznik += 1

        self.assertGreater(licznik, (ilosc_liczb/2)-10)
