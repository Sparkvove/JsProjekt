import pygame
import ui
from pygame.locals import *

pygame.init()

screen = ui.screen
pygame.display.set_caption('Symulacja Kasjera')

font = ui.font


# Zdefiniowanie licznika
counter = ""

run = True
while run:

    screen.fill(ui.bg)

    if ui.button1.draw_button():
        print('1')
        counter += '1'
    if ui.button2.draw_button():
        print('2')
        counter += '2'
    if ui.button3.draw_button():
        print('3')
        counter += '3'
    if ui.button4.draw_button():
        print('4')
        counter += '4'
    if ui.button5.draw_button():
        print('5')
        counter += '5'
    if ui.button6.draw_button():
        print('6')
        counter += '6'
    if ui.button7.draw_button():
        print('7')
        counter += '7'
    if ui.button8.draw_button():
        print('8')
        counter += '8'
    if ui.button9.draw_button():
        print('9')
        counter += '9'
    if ui.button0.draw_button():
        print('0')
        counter += '0'
    if ui.buttonBackspace.draw_button():
        print('Backspace')
        counter = counter[:-1]
    if ui.buttonWyczysc.draw_button():
        print('wyczysc')
        counter = ''
    if ui.buttonZwaz.draw_button():
        print('zwaz')
        counter -= 1

    pygame.draw.rect(screen, ui.black, (ui.xCounter, ui.yCounter, ui.widthCounter, ui.heightCounter))

    counter_img = font.render(str(counter), True, ui.white)
    screen.blit(counter_img, (510, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
