import pygame
from pygame.locals import *


pygame.init()

# Definicja klikniecia
clicked = False


class Colours():
    def __init__(self):
        self.bg = (204, 102, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)


class Screen(Colours):
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 440
        self.font = pygame.font.SysFont('Constantia', 20)
        self.window = Screen.PrintScreen(self)

    def PrintScreen(self):
        return pygame.display.set_mode((self.width, self.height))


screen = Screen()



class button(Colours):

    def __init__(self, x, y, multiplier, text):
        super().__init__()
        self.x = x
        self.y = y
        self.width = multiplier*60
        self.height = 60
        self.text = text
        self.button_col = self.red
        self.hover_col = (75, 225, 255)
        self.click_col = (50, 150, 255)
        self.text_col = self.black
        self.button_rect = button.button_bg(self)


    def button_shade(self):
        pygame.draw.line(screen.window, self.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen.window, self.white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen.window, self.black, (self.x, self.y + self.height),
                         (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen.window, self.black, (self.x + self.width, self.y),
                         (self.x + self.width, self.y + self.height), 2)

    def button_text(self):
        text_img = screen.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.window.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

    def button_bg(self):
        return Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        global clicked
        action = False

        # Uzyskanie pozycji myszki
        pos = pygame.mouse.get_pos()

        # Dodanie Klikniecia i najechania na przycisk
        if self.button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen.window, self.click_col, self.button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen.window, self.hover_col, self.button_rect)
        else:
            pygame.draw.rect(screen.window, self.button_col, self.button_rect)

        # Dodanie tekstu
        button.button_text(self)
        # Dodanie cieniowania
        button.button_shade(self)

        return action


class counter(Colours):

    def __init__(self):
        super().__init__()
        self.value = '1'
        self.x = 420
        self.y = 0
        self.width = 180
        self.height = 80

    def getCounterValue(self):
        return self.value

    def getCounterValueAsINT(self):
        return int(self.value)

    def setCounterValue(self, value):
        tmpvalue = self.value
        self.ClearCounterValue()
        self.value = tmpvalue + value

    def ClearCounterValue(self):
        self.value = ''

    def CreateCounterAsText(self):
        counterText = screen.font.render(self.value, True, self.white)
        screen.window.blit(counterText, (510, 40))

    def BackspaceCounter(self):
        self.value = self.value[:-1]

    def CreateBGForCounter(self):
        pygame.draw.rect(screen.window, self.black, (self.x, self.y, self.width, self.height))
