from datetime import datetime
import random

import ui

towar_names = ["Jabłko", "Banan", "Gruszka", "Pomidor", "Pomelo", "Truskawka", "Malina", "Pomarańcza", "Brokuł", "Arbuz",
               "Dynia", "Papryka", "Cebula", "Ogórek", "Burak", "Ananas", "Cytryna", "Kukurydza", "Czosnek", "Melon"]


how_many_towar = random.randint(10, 20)



global current_item_type
global current_item
global current_item_index


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
        if(one_or_more == 1):
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



towar_list = shuffle_list_and_return([TowarNaSztuki() if x < int(how_many_towar / 2)
                                      else TowarNaWage() for x in range(how_many_towar)])

