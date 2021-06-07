import pygame
import random
from pygame.locals import *
import Towary

do_zwazenia = False
towar_list = Towary.towar_list
pygame.init()

screen_width = 600
screen_height = 440

screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont('Constantia', 25)

# Kolory
bg = (204, 102, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Definicja klikniecie
clicked = False


class button():
    # Kolory przycisku
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black

    def __init__(self, x, y, width,height,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # Uzyskanie pozycji myszki
        pos = pygame.mouse.get_pos()

        # Tworzenie tla przycisku
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # Dodanie Klikniecia i najechania na przycisk
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        # Dodanie cieniowania
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # Dodanie tekstu
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


def show_game_win_screen(counter, menuState, stateOfGame, curr_towar):
    wygranaText = font.render('Wygrałeś! o to Podsumowanie: ', True, white)
    screen.blit(wygranaText, (300, 300))
    if buttonRestart.draw_button():
        counter = ''
        menuState = True
        stateOfGame = 'GAME'
        curr_towar = 0
    return counter, menuState, stateOfGame, curr_towar


def show_game_over_screen(counter, menuState, stateOfGame, curr_towar):
    przegranaText = font.render('Przegrałeś!', True, white)
    screen.blit(przegranaText, (300, 300))
    if buttonRestart.draw_button():
        counter = ''
        menuState = True
        stateOfGame = 'GAME'
        curr_towar = 0
    return counter, menuState, stateOfGame, curr_towar


def show_game_screen(counter, menuState, stateOfGame, curr_towar):
    global towar_list, do_zwazenia
    pygame.draw.rect(screen, black, (xCounter, yCounter, widthCounter, heightCounter))


    counterText = font.render(str(counter), True, white)


    buttonTowar1 = CreateTowaryButtons(curr_towar)

    typ = type(towar_list[curr_towar])

    if menuState:
        if buttonNastepnyKlient.draw_button():
            counter = ''
            menuState = False
    if not menuState:
        screen.blit(counterText, (510, 40))
        if buttonTowar1.draw_button():
            if typ == Towary.TowarNaSztuki:

                if int(counter) > towar_list[curr_towar].how_many:
                    stateOfGame = 'GAMEOVER'

                elif int(counter) == towar_list[curr_towar].how_many:
                    curr_towar += 1

                elif int(counter) < towar_list[curr_towar].how_many:
                    towar_list[curr_towar].how_many -= int(counter)

            if typ == Towary.TowarNaWage:

                if towar_list[curr_towar].weighed == True:
                    curr_towar += 1

                elif towar_list[curr_towar].weighed == False:
                    do_zwazenia = True


    if button1.draw_button():
        counter += '1'
    if button2.draw_button():
        counter += '2'
    if button3.draw_button():
        counter += '3'
    if button4.draw_button():
        counter += '4'
    if button5.draw_button():
        counter += '5'
    if button6.draw_button():
        counter += '6'
    if button7.draw_button():
        counter += '7'
    if button8.draw_button():
        counter += '8'
    if button9.draw_button():
        counter += '9'
    if button0.draw_button():
        counter += '0'
    if buttonBackspace.draw_button():
        counter = counter[:-1]
    if buttonWyczysc.draw_button():
        counter = ''
    if buttonZwaz.draw_button():

        if typ == Towary.TowarNaSztuki:
            stateOfGame = 'GAMEOVER'
        else:
             if do_zwazenia == True:
                towar_list[curr_towar].weighed = True
                do_zwazenia = False

    if buttonPrzegrana.draw_button():
        stateOfGame = 'GAMEOVER'
    return counter, menuState, stateOfGame, curr_towar





# Definiowanie przyciskow
buttonWidth = 60
buttonHeight = 60
button1 = button(420, 80,buttonWidth,buttonHeight, '1')
button2 = button(480, 80,buttonWidth,buttonHeight, '2')
button3 = button(540, 80,buttonWidth ,buttonHeight,'3')
button4 = button(420, 140,buttonWidth,buttonHeight, '4')
button5 = button(480, 140,buttonWidth,buttonHeight, '5')
button6 = button(540, 140,buttonWidth,buttonHeight, '6')
button7 = button(420, 200,buttonWidth,buttonHeight, '7')
button8 = button(480, 200,buttonWidth ,buttonHeight,'8')
button9 = button(540, 200,buttonWidth ,buttonHeight,'9')
button0 = button(540, 260,buttonWidth,buttonHeight, '0')
buttonBackspace = button(420, 260,2*buttonWidth,buttonHeight, 'backspace')
buttonWyczysc = button(420, 320,3*buttonWidth,buttonHeight, 'wyczysc')
buttonZwaz = button(420, 380,3*buttonWidth,buttonHeight, 'zwaz')
buttonNastepnyKlient = button(0,0,180,70, 'Następny klient')
buttonPrzegrana = button(0,320,buttonWidth,buttonHeight,'Przegrana')
buttonRestart = button(280,320,buttonWidth,buttonHeight,'Restart')


def CreateTowaryButtons(curr_item):
    global towar_list
    typ = type(towar_list[curr_item])
    if typ == Towary.TowarNaSztuki:
        buttonTowar1 = button(20, 20, buttonWidth, buttonHeight,
                              towar_list[curr_item].name + ' x' + str(towar_list[curr_item].how_many))
    if typ == Towary.TowarNaWage:
        if towar_list[curr_item].weighed == False:
            buttonTowar1 = button(20, 20, buttonWidth, buttonHeight,
                                towar_list[curr_item].name + ' ?kg')
        else:
            buttonTowar1 = button(20, 20, buttonWidth, buttonHeight,
                                  towar_list[curr_item].name + ' '+ str(towar_list[curr_item].weight) + 'kg')
    return buttonTowar1





# Definiowanie zmiennych pod tlo licznika
xCounter= 420
yCounter= 0
widthCounter = 180
heightCounter = 80