import pygame
from pygame.locals import *


pygame.init()


class Screen():
    def __init__(self):
        self.width = 600
        self.height = 440
        self.bg = (204, 102, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.font = pygame.font.SysFont('Constantia', 25)

    def PrintScreen(self):
        return pygame.display.set_mode((self.width, self.height))


screen = Screen()
window = screen.PrintScreen()

# Definicja klikniecie
clicked = False


class button():
    # Kolory przycisku
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = screen.black

    def __init__(self, x, y, multiplier, text):
        self.x = x
        self.y = y
        self.width = multiplier*60
        self.height = 60
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
                pygame.draw.rect(window, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(window, self.hover_col, button_rect)
        else:
            pygame.draw.rect(window, self.button_col, button_rect)

        # Dodanie cieniowania
        pygame.draw.line(window, screen.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(window, screen.white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(window, screen.black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(window, screen.black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # Dodanie tekstu
        text_img = screen.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        window.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


class counter():

    def __init__(self):
        self._value = '1'
        self.x = 420
        self.y = 0
        self.width = 180
        self.height = 80

    def getCounterValue(self):
        return self._value

    def getCounterValueAsINT(self):
        return int(self._value)

    def setCounterValue(self, value):
        tmpvalue = self.value
        self.ClearCounterValue()
        self.value = tmpvalue + value

    def ClearCounterValue(self):
        self.value = ''

    def CreateCounterAsText(self):
        counterText = screen.font.render(self.value, True, screen.white)
        window.blit(counterText, (510, 40))

    def BackspaceCounter(self):
        self.value = self.value[:-1]

    def CreateBGForCounter(self):
        pygame.draw.rect(window, screen.black, (self.x, self.y, self.width, self.height))
