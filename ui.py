import pygame
from pygame.locals import *

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

# Definiowanie zmiennych pod tlo licznika
xCounter= 420
yCounter= 0
widthCounter = 180
heightCounter = 80