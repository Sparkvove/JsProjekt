from datetime import datetime
import random

towar_names = ["Jabłko", "Banan", "Gruszka", "Pomidor", "Pomelo", "Truskawka", "Malina", "Pomarańcza", "Brokuł",
               "Arbuz", "Dynia", "Papryka", "Cebula", "Ogórek", "Burak",
               "Ananas", "Cytryna", "Kukurydza", "Czosnek", "Melon"]

how_many_towar = random.randint(10, 20)


class Towar:

    def __init__(self):
        self.name = random.choice(towar_names)
        self.create_time = datetime.now()
        self.checkout_time = datetime.now()


class TowarNaSztuki(Towar):

    def __init__(self):
        super().__init__()
        self.how_many = self.get_how_many()

    @staticmethod
    def get_how_many():
        one_or_more = random.choice([1, 2])
        if one_or_more == 1:
            return 1
        else:
            return random.randint(2, 50)


class TowarNaWage(Towar):

    def __init__(self):
        super().__init__()
        self.weight = round(random.uniform(0.05, 2), 2)
        self.weighed = False


def shuffle_list_and_return(x):
    random.shuffle(x)
    return x
