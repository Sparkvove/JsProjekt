import pygame
from pygame.locals import *

pygame.init()

# Definicja klikniecia
clicked = False


class Colours:
    """
    Klasa Clours, zawiera ona w sobie kolory używanie w tworzeniu interfejsu
    """
    def __init__(self):
        self.bg = (204, 102, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)


class Screen(Colours):
    """
    Klasa ta dziedziczy po klasie Colours, ustawia ona rodzaj i rozmiar czcionki używanej w programie
    Dodatkowo obiektem tej klasy jest wyświetlany ekran
    """
    def __init__(self):
        super().__init__()
        self.width = 600
        self.height = 440

        set_font = lambda font, size: pygame.font.SysFont(font, size)
        self.font = set_font('Constantia', 20)

        self.window = Screen.print_screen(self)

    def print_screen(self):
        return pygame.display.set_mode((self.width, self.height))


screen = Screen()


class Button(Colours):
    """
    Klasa ta dziedziczy po klasie Colours, odpowiada ona za utworzenie wszystkich przycisków w aplikacji
    Wykrywa ona również klikniecie oraz najechania na konkretny przycisk
    """
    def __init__(self, x, y, multiplier, text):
        super().__init__()
        self.x = x
        self.y = y

        calculate_width = lambda m: m * 60
        self.width = calculate_width(multiplier)

        self.height = 60
        self.text = text
        self.button_col = self.red
        self.hover_col = (75, 225, 255)
        self.click_col = (50, 150, 255)
        self.text_col = self.black
        self.button_rect = Button.button_bg(self)

    def button_shade(self):
        """
        Metoda ta odpowiada za tworzenie efektu "cienia" na przyciskach
        """
        pygame.draw.line(screen.window, self.white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen.window, self.white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen.window, self.black, (self.x, self.y + self.height),
                         (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen.window, self.black, (self.x + self.width, self.y),
                         (self.x + self.width, self.y + self.height), 2)

    def button_text(self):
        """
        Metoda ta odpowiada za dodawanie tesktu do przycisków
        """
        text_img = screen.font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.window.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

    def button_bg(self):
        """
        Metoda ta odpowiada za utworzenie tła pod przycisk
        """
        return Rect(self.x, self.y, self.width, self.height)

    def draw_button(self):
        """
        Metoda ta odpowiada za wykrywanie kliknięcia oraz najechania na przyciski
        """
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
        Button.button_text(self)
        # Dodanie cieniowania
        Button.button_shade(self)

        return action


class Counter(Colours):
    """
    Klasa ta dziedziczy po klasie Colours, odpowiada ona za licznik w grze(wyświetlanie, zmiana wartości, tło licznika)
    """
    def __init__(self):
        super().__init__()
        self.value = '1'
        self.x = 420
        self.y = 0
        self.width = 180
        self.height = 80

    def get_counter_value(self):
        return self.value

    def set_counter_value(self, value):
        """
        Metoda ta ustawia wartość licznika poprzez wyczyszczenie licznika oraz utworzenie nowego.
        Dodatkowo sprawdza ona długość licznika, aby nie wykroczył on poza obszar aplikacji
        :param value: Wartość którą chcemy dopisać do naszego licznika
        """
        if len(self.value) < 3:
            tmpvalue = self.value
            self.clear_counter_value()
            self.value = tmpvalue + value

    def clear_counter_value(self):
        """
        Metoda czyszcząca wartość licznika
        """
        self.value = ''

    def create_counter_as_text(self):
        """
        Metoda która zamienia wartość licznika na wyświetlany tekst na ekranie
        """
        counter_text = screen.font.render(self.value, True, self.white)
        if len(self.value) == 1 or 0:
            screen.window.blit(counter_text, (510, 40))
        if len(self.value) == 2:
            screen.window.blit(counter_text, (500, 40))
        if len(self.value) == 3:
            screen.window.blit(counter_text, (500, 40))

    def backspace_counter(self):
        """
        Metoda ta odpowiada za zmiane wartości licznika przy wciśnięciu przyciska backspace
        """
        self.value = self.value[:-1]

    def create_bg_for_counter(self):
        """
        Metoda która tworzy tło pod licznik
        Jest on w formie czarnego prostokąta o określonych rozmiarach
        """
        pygame.draw.rect(screen.window, self.black, (self.x, self.y, self.width, self.height))
