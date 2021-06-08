import datetime
import unittest
import Towary
import pygame
import ui
import game


class TestGame(unittest.TestCase):

    def test_ScanningTowarNaSztukiByClickinFewTimes(self):
        pygame.init()
        GAME = game.Game()
        counter = ui.counter()
        GAME.SetGameCaption()
        GAME.menuState = False
        p1 = Towary.TowarNaSztuki()
        p2 = Towary.TowarNaSztuki()
        p1.how_many = 20
        GAME.towar_list = [p1, p2]
        while GAME.run:
            GAME.window.fill(GAME.screen.bg)
            if GAME.stateOfGame == 'GAME':
                counter, GAME = game.show_game_screen(counter, GAME, True, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME.run = False

            pygame.display.update()

        self.assertEqual(GAME.curr_towar, 1)
        #        GAME = game.Game()
        #        counter, GAME = TestGame.CreateGame(self, '1', 1)
        #        self.assertEqual(GAME.curr_towar, 1)

    def test_ScanningTowarNaSztukiByClickinOneTime(self):
        GAME = game.Game()
        counter = ui.counter()
        GAME.SetGameCaption()
        GAME.menuState = False
        p1 = Towary.TowarNaSztuki()
        p2 = Towary.TowarNaSztuki()
        p1.how_many = 20
        GAME.towar_list = [p1, p2]
        counter.value = '20'
        while GAME.run:
            GAME.window.fill(GAME.screen.bg)
            if GAME.stateOfGame == 'GAME':
                counter, GAME = game.show_game_screen(counter, GAME, True, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME.run = False

            pygame.display.update()

        self.assertEqual(GAME.curr_towar, 1)
        #        GAME = game.Game()
        #        counter, GAME = TestGame.CreateGame(self, '20', 1)
        #        self.assertEqual(GAME.stateOfGame, 'GAMEOVER')



    def test_ScanningTowarNaSztukiByClickinOneTimeAndHavingMoreValue(self):
        GAME = game.Game()
        counter = ui.counter()
        GAME.SetGameCaption()
        GAME.menuState = False
        p1 = Towary.TowarNaSztuki()
        p2 = Towary.TowarNaSztuki()
        p1.how_many = 20
        GAME.towar_list = [p1, p2]
        counter.value = '40'
        while GAME.run:
            GAME.window.fill(GAME.screen.bg)
            if GAME.stateOfGame == 'GAME':
                counter, GAME = game.show_game_screen(counter, GAME, True, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME.run = False

            pygame.display.update()

        self.assertEqual(GAME.stateOfGame, 'GAMEOVER')

#        GAME = game.Game()
#        counter, GAME = TestGame.CreateGame(self, '40', 1)
#        self.assertEqual(GAME.stateOfGame, 'GAMEOVER')

    def test_WeightTowarNaSztuki(self):
        GAME = game.Game()
        counter = ui.counter()
        GAME.SetGameCaption()
        GAME.menuState = False
        p1 = Towary.TowarNaSztuki()
        p2 = Towary.TowarNaSztuki()
        p1.how_many = 20
        GAME.towar_list = [p1, p2]
        counter.value = '40'
        while GAME.run:
            GAME.window.fill(GAME.screen.bg)
            if GAME.stateOfGame == 'GAME':
                counter, GAME = game.show_game_screen(counter, GAME, True, 2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME.run = False

            pygame.display.update()

        self.assertEqual(GAME.stateOfGame, 'GAMEOVER')


    def test_WinGame(self):
        GAME = game.Game()
        counter = ui.counter()
        GAME.SetGameCaption()
        GAME.menuState = False
        p1 = Towary.TowarNaSztuki()
        p2 = Towary.TowarNaSztuki()
        p1.how_many = 20
        GAME.towar_list = [p1, p2]
        counter.value = '20'
        while GAME.run:
            GAME.window.fill(GAME.screen.bg)
            if GAME.stateOfGame == 'GAME':
                counter, GAME = game.show_game_screen(counter, GAME, True, 1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GAME.run = False

            pygame.display.update()

        self.assertEqual(GAME.stateOfGame, 'GAMEWIN')
#        GAME = game.Game()
#        counter, GAME = TestGame.CreateGame(self, '20', 1)
#        self.assertEqual(GAME.stateOfGame, 'GAMEWIN')

#    def test_CheckValues(self):
#        ilosc_liczb = 100
#        licznik = 0
#        for x in range(ilosc_liczb):
#            y = Towary.TowarNaSztuki.get_how_many()
#            if y == 1:
#                licznik += 1
#
#        self.assertGreater(licznik, (ilosc_liczb/2)-10)



