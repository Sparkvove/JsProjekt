import unittest
import Towary
import pygame
import ui
from game import Game
import game


def create_game(counter_value, mode):
    """
    Funkcja ta służy do Tworzenia testowej głównej pętli gry dla Testów
    tworzymy w niej obiekt klasy game, counter, przypisujemy do testowania spredefiniowane elementy p1, p2
    oraz przypisujemy przekazywaną wartość licznika
    :param counter_value: przekazujemy wartość licznika (używane w licznych testach)
    :param mode: przekazujemy tryb testowania pętli
    """
    pygame.init()
    testing_game = Game()
    counter = ui.Counter()
    testing_game.set_game_caption()
    testing_game.menuState = False
    p1 = Towary.TowarNaSztuki()
    p2 = Towary.TowarNaSztuki()
    p1.how_many = 20

    set_testing_list = lambda first, second: [first, second]
    testing_game.towar_list = set_testing_list(p1, p2)

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
    """
    Klasa odpowiadająca za wszystkie testy w aplikacji
    """

    def test_scanning_towar_na_sztuki_by_clicking_few_times(self):
        """
        Meotda ta sprawdza czy działa skasowanie towaru poprzez klikanie na niego pare razy
        """
        counter, testing_game = create_game('1', 1)
        self.assertEqual(testing_game.curr_towar, 1)

    def test_scanning_towar_na_sztuki_by_clicking_one_time(self):
        """
        Metoda ta sprawdza czy działa skasowanie towaru poprzez kliknięcie na niego jeden raz
        """
        counter, testing_game = create_game('20', 1)
        self.assertEqual(counter.value, '1')

    def test_scanning_towar_na_sztuki_by_clicking_one_time_and_exceed_value(self):
        """
        Metoda ta sprawdza czy przegrywamy gre w przypadku kliknięcia na towar o mniejszej ilości niż licznik
        """
        counter, testing_game = create_game('40', 1)
        self.assertEqual(testing_game.stateOfGame, 'GAMEOVER')

    def test_weight_towar_na_sztuki(self):
        """
        Meotda ta sprawdza czy przegrywamy gre w przypadku próby zważenia towaru na sztuki
        """
        counter, testing_game = create_game('40', 2)
        self.assertEqual(testing_game.stateOfGame, 'GAMEOVER')

    def test_win_game(self):
        """
        Metoda ta sprawdza czy wygramy gre, w przypadku skasowania wszystkich towarów
        """
        counter, testing_game = create_game('20', 1)
        self.assertEqual(testing_game.stateOfGame, 'GAMEWIN')

    def test_check_if_values_equals_one_enough_times(self):
        """
        Metoda ta sprawdza czy ilosć towaru = 1 występuje wystarczająco często (50%)
        od określonej liczby_liczb w wyniku odejmuje 10, ponieważ pomimo tego że szansa
        na ilość_towaru wynosic 50%, to w niektrych przypadkach ilość tych towarów będzie mniejsza lub większa niz 50%
        Dlatego jako fakt zadawalajoncy uznaje 40% wszystkich liczb
        """
        ilosc_liczb = 100
        licznik = 0
        for x in range(ilosc_liczb):
            y = Towary.TowarNaSztuki.get_how_many()
            if y == 1:

                licznik += 1

        met_conditions = lambda range_value: (range_value/2)-10
        condition = met_conditions(ilosc_liczb)

        self.assertGreater(licznik, condition)
