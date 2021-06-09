from datetime import datetime
import random

towar_names = ["Jabłko", "Banan", "Gruszka", "Pomidor", "Pomelo", "Truskawka", "Malina", "Pomarańcza", "Brokuł",
               "Arbuz", "Dynia", "Papryka", "Cebula", "Ogórek", "Burak",
               "Ananas", "Cytryna", "Kukurydza", "Czosnek", "Melon"]

how_many_towar = random.randint(10, 20)


class Towar:
    """
    Tworzy towar zawierający nazwe towaru, czas stworzenia towaru, oraz czas zeskoanowania
    """
    def __init__(self):
        self.name = random.choice(towar_names)
        self.create_time = datetime.now()
        self.scan_time = datetime.now()


class TowarNaSztuki(Towar):
    """
    Klasa Dziedziczy po klasie towar, tworzy TowarNaSztuki dodając do niego ilość towaru
    """
    def __init__(self):
        super().__init__()
        self.how_many = self.get_how_many()

    @staticmethod
    def get_how_many():
        """
        Metoda przypisana do Klasy TowarNaSztuki, odpowiada za wylosowanie ilości towaru
        """
        one_or_more = random.choice([1, 2])
        if one_or_more == 1:
            return 1
        else:
            return random.randint(2, 50)


class TowarNaWage(Towar):
    """
    Klasa Dziedziczy po klasie towar, tworzy TowarNaSztuki dodając do niego wage towaru, oraz atrybut bycią zważonym
    """
    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)
        self.weighed = False


def shuffle_list_and_return(x):
    """
    Funkcja zamienia losowo miejscami zadaną liste
    """
    random.shuffle(x)
    return x
