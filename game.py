import ui
import Towary
import pygame
from datetime import datetime
pygame.init()


class Game:
    """
    Klasa Game - zawiera ona wszystkie przyciski, oraz wszelkie zmienne potrzebne do funkcjonowania aplikacji
    """
    def __init__(self):
        self.run = True
        self.menuState = True
        self.stateOfGame = 'GAME'
        self.curr_towar = 0
        self.do_zwazenia = False
        self.screen = ui.screen
        self.window = ui.screen.window
        self.towar_list = Towary.shuffle_list_and_return([Towary.TowarNaSztuki() if x < int(Towary.how_many_towar / 2)
                                                          else Towary.TowarNaWage() for x in
                                                          range(Towary.how_many_towar)])
        self.button1 = ui.Button(420, 80, 1, '1')
        self.button2 = ui.Button(480, 80, 1, '2')
        self.button3 = ui.Button(540, 80, 1, '3')
        self.button4 = ui.Button(420, 140, 1, '4')
        self.button5 = ui.Button(480, 140, 1, '5')
        self.button6 = ui.Button(540, 140, 1, '6')
        self.button7 = ui.Button(420, 200, 1, '7')
        self.button8 = ui.Button(480, 200, 1, '8')
        self.button9 = ui.Button(540, 200, 1, '9')
        self.button0 = ui.Button(540, 260, 1, '0')
        self.buttonBackspace = ui.Button(420, 260, 2, 'backspace')
        self.buttonWyczysc = ui.Button(420, 320, 3, 'wyczysc')
        self.buttonZwaz = ui.Button(420, 380, 3, 'zwaz')
        self.buttonNastepnyKlient = ui.Button(0, 0, 3, 'Następny klient')
        self.buttonPrzegrana = ui.Button(0, 320, 1, 'Przegrana')
        self.buttonWygrana = ui.Button(0, 380, 1, 'Wygrana')
        self.buttonRestart = ui.Button(280, 320, 1, 'Restart')
        self.TowaryCounter = 0
        self.timerStart = None
        self.timerStop = None
        self.timeToWin = None
        self.timeToMinutes = None
        self.averageTime = None

    @staticmethod
    def set_game_caption():
        """
        Metoda ta odpowiada za ustawienie tytułu aplikacji(okna)
        """
        pygame.display.set_caption('Symulacja Kasjera')


def show_game_win_screen(counter, game):
    """
    Metoda ta odpowiada za wyświetlenie ekranu w przypadku wygrania
    Pokazuje ona wszystkie wymagane statystyki:
    Skasowana ilość towarów, Totalny czas grania oraz średni czas kasowania towaru
    """
    game.timeToWin = game.timerStop - game.timerStart
    game.timeToWin = game.timeToWin.total_seconds()
    game.averageTime = game.timeToWin / game.TowaryCounter
    game.timeToWin = round(game.timeToWin, 2)
    game.averageTime = round(game.averageTime, 2)

    results = game.screen.font.render('Wygrałeś! o to Podsumowanie: ', True, game.screen.white)
    game.window.blit(results, (160, 0))

    results_towary_counter = game.screen.font.render('Skasowana ilosc towarow:  '
                                                     + str(game.TowaryCounter), True, game.screen.white)
    game.window.blit(results_towary_counter, (170, 20))

    results_towary_time_to_win = game.screen.font.render('Totalny czas grania(sek): '
                                                         + str(game.timeToWin), True, game.screen.white)
    game.window.blit(results_towary_time_to_win, (170, 40))

    results_time = game.screen.font.render('Sredni czas kasowania towaru(na sek):  '
                                           + str(game.averageTime), True, game.screen.white)
    game.window.blit(results_time, (120, 60))

    if game.buttonRestart.draw_button():
        counter.clear_counter_value()
        game.menuState = True
        game.stateOfGame = 'GAME'
        game.curr_towar = 0
    return counter, game


def show_game_over_screen(counter, game):
    """
    Metoda ta odpowiada za wyświetlenie ekranu w przypadku przegrania gry
    """
    przegrana_text = game.screen.font.render('Przegrałeś!', True, game.screen.white)
    game.window.blit(przegrana_text, (250, 300))

    if game.buttonRestart.draw_button():
        counter.clear_counter_value()
        game.menuState = True
        game.stateOfGame = 'GAME'
        game.curr_towar = 0

    return counter, game


def show_game_screen(counter, game, testing, mode):
    """
    Najważniesza funkcja programu, obsługuje ona samo "granie" w gre(tzn że gra "trwa")
    W niej wyświetlamy wszystkie elementy interfejsu, tzn. Wszystkie przyciski, licznik
    Sprawdza ona czy jesteśmy w menu(Przycisk nastepny klient) czy jesteśmy już w grze
    Obsługujemy również w niej kliknięcia we wszystkie możliwe przyciski
    Sprawdzamy również czy nie próbujemy ważyć TowaruNaSztuki oraz obsługujemy sam system ważenia towaru

    Dodatkowo w tej funkcji wykonywane są prawie wszystkie testy
    dlatego do funkcji przekazujemy:
    :param game: Głowny obiekt klasy Game
    :param counter: obiekt  klasy Counter
    :param testing: typ Bool(True lub False), określamy czy funkcja ma działać w trybie testów czy nie
    :param mode: typ int(1 lub 2), określamy aktualny typ testowania
    """
    counter.create_bg_for_counter()
    button_towar = create_towary_buttons(game)
    typ = type(game.towar_list[game.curr_towar])

    if testing:
        if mode == 1:
            button_towar.draw_button()
            if int(counter.value) == game.towar_list[game.curr_towar].how_many:
                game.TowaryCounter += int(counter.value)
                game.curr_towar += 1
                game.stateOfGame = "GAMEWIN"
                game.run = False

            elif int(counter.value) < game.towar_list[game.curr_towar].how_many:
                game.towar_list[game.curr_towar].how_many -= int(counter.value)
                game.TowaryCounter += int(counter.value)

            elif int(counter.value) > game.towar_list[game.curr_towar].how_many:
                game.stateOfGame = 'GAMEOVER'
                game.run = False
        elif mode == 2:
            game.buttonZwaz.draw_button()

            if typ == Towary.TowarNaSztuki:
                game.stateOfGame = 'GAMEOVER'
                game.run = False
            else:
                if game.do_zwazenia:
                    game.towar_list[game.curr_towar].weighed = True
                    game.do_zwazenia = False

        counter.clear_counter_value()
        counter.set_counter_value('1')

    if game.menuState:
        if game.buttonNastepnyKlient.draw_button():
            game.timerStart = datetime.now()
            game.menuState = False
            counter.clear_counter_value()
            counter.set_counter_value('1')

    if not game.menuState:
        counter.create_counter_as_text()
        if button_towar.draw_button():
            if typ == Towary.TowarNaSztuki:

                if counter.value == '':
                    pass

                elif int(counter.value) > game.towar_list[game.curr_towar].how_many:
                    game.stateOfGame = 'GAMEOVER'

                elif int(counter.value) == game.towar_list[game.curr_towar].how_many:
                    game.TowaryCounter += int(counter.value)
                    game.curr_towar += 1

                elif int(counter.value) < game.towar_list[game.curr_towar].how_many:
                    game.towar_list[game.curr_towar].how_many -= int(counter.value)
                    game.TowaryCounter += int(counter.value)

            counter.clear_counter_value()
            counter.set_counter_value('1')

            if typ == Towary.TowarNaWage:

                if game.towar_list[game.curr_towar].weighed:
                    game.TowaryCounter += 1
                    game.curr_towar += 1

                elif not game.towar_list[game.curr_towar].weighed:
                    game.do_zwazenia = True

            counter.clear_counter_value()
            counter.set_counter_value('1')

    if game.button1.draw_button():
        counter.set_counter_value('1')
    if game.button2.draw_button():
        counter.set_counter_value('2')
    if game.button3.draw_button():
        counter.set_counter_value('3')
    if game.button4.draw_button():
        counter.set_counter_value('4')
    if game.button5.draw_button():
        counter.set_counter_value('5')
    if game.button6.draw_button():
        counter.set_counter_value('6')
    if game.button7.draw_button():
        counter.set_counter_value('7')
    if game.button8.draw_button():
        counter.set_counter_value('8')
    if game.button9.draw_button():
        counter.set_counter_value('9')
    if game.button0.draw_button():
        counter.set_counter_value('0')
    if game.buttonBackspace.draw_button():
        counter.backspace_counter()
    if game.buttonWyczysc.draw_button():
        counter.clear_counter_value()
        counter.set_counter_value('')
    if game.buttonZwaz.draw_button():

        if typ == Towary.TowarNaSztuki:
            game.stateOfGame = 'GAMEOVER'
        else:
            if game.do_zwazenia:
                game.towar_list[game.curr_towar].weighed = True
                game.do_zwazenia = False

    if game.buttonPrzegrana.draw_button():
        game.stateOfGame = 'GAMEOVER'

    if game.buttonWygrana.draw_button():
        game.timerStop = datetime.now()
        game.stateOfGame = 'GAMEWIN'
    return counter, game


def create_towary_buttons(game):
    """
    Funkcja odpowiadająca za dynamiczne tworzenie i odśweżanie(np. gdy zważymy towar, lub zmniejszymy jego ilość)
    przycisku aktualnego Towaru
    """
    typ = type(game.towar_list[game.curr_towar])
    if typ == Towary.TowarNaSztuki:
        button_towar = ui.Button(20, 20, 2, game.towar_list[game.curr_towar].name + ' x' +
                                 str(game.towar_list[game.curr_towar].how_many))
    else:
        if not game.towar_list[game.curr_towar].weighed:
            button_towar = ui.Button(20, 20, 2, game.towar_list[game.curr_towar].name + ' ?kg')
        else:
            button_towar = ui.Button(20, 20, 2, game.towar_list[game.curr_towar].name + ' '
                                     + str(game.towar_list[game.curr_towar].weight) + 'kg')
    return button_towar


def application(game, counter):
    """
    Funkcja ta odpowiada za główną pętle programu(używając biblioteki pygame musimy używać głównej pętli)
    Sprawdza ona aktualny stan gry(wygrana, przegrana, trwa), odświeża ona również aplikacje, sprawdzając
    wszelkiego rodzaju zdarzenia w aplikacji(np wcisniecie przycisku, wyłączenie aplikacji, lub zmiania stanu gry)

    :param game: Głowny obiekt klasy Game
    :param counter: obiekt  klasy Counter
    """
    while game.run:
        game.window.fill(game.screen.bg)
        if game.stateOfGame == 'GAME':
            counter, game = show_game_screen(counter, game, False, 0)

            if game.curr_towar == Towary.how_many_towar - 1:
                game.timerStop = datetime.now()
                game.stateOfGame = 'GAMEWIN'

        elif game.stateOfGame == 'GAMEOVER':
            counter, game = show_game_over_screen(counter, game)

        elif game.stateOfGame == 'GAMEWIN':
            counter, game = show_game_win_screen(counter, game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.run = False

        pygame.display.update()
