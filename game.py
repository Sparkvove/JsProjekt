import ui
import Towary
import pygame

pygame.init()


class Game():

    def __init__(self):
        self.run = True
        self.menuState = True
        self.stateOfGame = 'GAME'
        self.curr_towar = 0
        self.do_zwazenia = False
        self.towar_list = Towary.shuffle_list_and_return([Towary.TowarNaSztuki() if x < int(Towary.how_many_towar / 2)
                                                          else Towary.TowarNaWage() for x in
                                                          range(Towary.how_many_towar)])

    @staticmethod
    def SetGameCaption():
        pygame.display.set_caption('Symulacja Kasjera')


screen = ui.screen
window = ui.window

def show_game_win_screen(counter, game):
    wygranaText = screen.font.render('Wygrałeś! o to Podsumowanie: ', True, screen.white)
    window.blit(wygranaText, (300, 300))
    if buttonRestart.draw_button():
        counter.ClearCounterValue()
        game.menuState = True
        game.stateOfGame = 'GAME'
        game.curr_towar = 0
    return counter, game


def show_game_over_screen(counter, game):
    przegranaText = screen.font.render('Przegrałeś!', True, screen.white)
    window.blit(przegranaText, (300, 300))
    if buttonRestart.draw_button():
        counter.ClearCounterValue()
        game.menuState = True
        game.stateOfGame = 'GAME'
        game.curr_towar = 0
    return counter, game


def show_game_screen(counter, game):

    counter.CreateBGForCounter()

    buttonTowar1 = CreateTowaryButtons(game.curr_towar, game)

    typ = type(game.towar_list[game.curr_towar])

    if game.menuState:
        if buttonNastepnyKlient.draw_button():
            game.menuState = False
            counter.ClearCounterValue()
            counter.setCounterValue('1')
    if not game.menuState:
        counter.CreateCounterAsText()
        if buttonTowar1.draw_button():
            if typ == Towary.TowarNaSztuki:

                if int(counter.value) > game.towar_list[game.curr_towar].how_many:
                    game.stateOfGame = 'GAMEOVER'

                elif int(counter.value) == game.towar_list[game.curr_towar].how_many:
                    game.curr_towar += 1

                elif int(counter.value) < game.towar_list[game.curr_towar].how_many:
                    game.towar_list[game.curr_towar].how_many -= int(counter.value)
                counter.ClearCounterValue()
                counter.setCounterValue('1')

            if typ == Towary.TowarNaWage:

                if game.towar_list[game.curr_towar].weighed == True:
                    game.curr_towar += 1

                elif game.towar_list[game.curr_towar].weighed == False:
                    game.do_zwazenia = True


    if button1.draw_button():
        counter.setCounterValue('1')
    if button2.draw_button():
        counter.setCounterValue('2')
    if button3.draw_button():
        counter.setCounterValue('3')
    if button4.draw_button():
        counter.setCounterValue('4')
    if button5.draw_button():
        counter.setCounterValue('5')
    if button6.draw_button():
        counter.setCounterValue('6')
    if button7.draw_button():
        counter.setCounterValue('7')
    if button8.draw_button():
        counter.setCounterValue('8')
    if button9.draw_button():
        counter.setCounterValue('9')
    if button0.draw_button():
        counter.setCounterValue('0')
    if buttonBackspace.draw_button():
        counter.BackspaceCounter()
    if buttonWyczysc.draw_button():
        counter.ClearCounterValue()
        counter.setCounterValue('')
    if buttonZwaz.draw_button():

        if typ == Towary.TowarNaSztuki:
            game.stateOfGame = 'GAMEOVER'
        else:
             if game.do_zwazenia == True:
                game.towar_list[game.curr_towar].weighed = True
                game.do_zwazenia = False

    if buttonPrzegrana.draw_button():
        game.stateOfGame = 'GAMEOVER'
    return counter, game


def CreateTowaryButtons(curr_item, game):
    typ = type(game.towar_list[curr_item])
    if typ == Towary.TowarNaSztuki:
        buttonTowar1 = ui.button(20, 20, 1, game.towar_list[curr_item].name + ' x' + str(game.towar_list[curr_item].how_many))
    else:
        if game.towar_list[curr_item].weighed == False:
            buttonTowar1 = ui.button(20, 20, 1, game.towar_list[curr_item].name + ' ?kg')
        else:
            buttonTowar1 = ui.button(20, 20, 1, game.towar_list[curr_item].name + ' '
                                     + str(game.towar_list[curr_item].weight) + 'kg')
    return buttonTowar1


button1 = ui.button(420, 80, 1, '1')
button2 = ui.button(480, 80, 1, '2')
button3 = ui.button(540, 80, 1, '3')
button4 = ui.button(420, 140, 1, '4')
button5 = ui.button(480, 140, 1, '5')
button6 = ui.button(540, 140, 1, '6')
button7 = ui.button(420, 200, 1, '7')
button8 = ui.button(480, 200, 1, '8')
button9 = ui.button(540, 200, 1, '9')
button0 = ui.button(540, 260, 1, '0')
buttonBackspace = ui.button(420, 260, 2, 'backspace')
buttonWyczysc = ui.button(420, 320, 3, 'wyczysc')
buttonZwaz = ui.button(420, 380, 3, 'zwaz')
buttonNastepnyKlient = ui.button(0, 0, 3, 'Następny klient')
buttonPrzegrana = ui.button(0, 320, 1, 'Przegrana')
buttonRestart = ui.button(280, 320, 1, 'Restart')


