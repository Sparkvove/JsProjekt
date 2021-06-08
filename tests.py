import unittest
import Towary
import random
from game import Game


class TestGame(unittest.TestCase):
    #
    # Skasowanie towaru na sztuki po klikając na niego kilka razy. Skasowanie towaru na sztuki wpisując jego liczność i
    # klikając raz. Wymagane jest resetowanie pola do wartości 1. Próba skasowania towaru na sztuki wpisując zbyt dużą
    # liczność (oczekiwana informacja o przegranej). Próba zważenia towaru na sztuki (oczekiwana informacja o
    # przegranej). Próba skasowania towaru na wagę jakby był towarem na sztuki (oczekiwana informacja o przegranej). -
    # NIE DO ZROBIENIA Skasowanie wszystkich towarów (oczekiwane okno z podsumowaniem symulacji). Pokazanie,
    # że liczebność 1 występuje odpowiednio często.
    #

    def ScanningTowarNaSztukiByClickinFewTimes(self):
        Towar = Towary.TowarNaSztuki()
        Towar.how_many = random.randint(2, 50)
