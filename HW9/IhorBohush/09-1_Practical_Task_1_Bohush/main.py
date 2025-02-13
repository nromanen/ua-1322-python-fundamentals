import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('My game')
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('arial', 24)
font1 = pygame.font.SysFont('arial', 48)
text = ''
display_text = ''
display_text1 = ''
input_active = True
number_attempt = 0
random_number = None
play_rectangle = pygame.Rect(100, 100, 285, 40)
play_rectangle1 = pygame.Rect(105, 105, 275, 30)
exit_rect = pygame.Rect(415, 100, 285, 40)
exit_rect1 = pygame.Rect(420, 105, 275, 30)
input_rectangle = pygame.Rect(100, 250, 400, 40)
input_rectangle1 = pygame.Rect(105, 255, 390, 30)
button_rect = pygame.Rect(530, 250, 170, 40)
button_rect1 = pygame.Rect(535, 255, 160, 30)
output_rectangle = pygame.Rect(100, 350, 600, 200)
output_rectangle1 = pygame.Rect(105, 355, 590, 190)


def multiline_text(mt_text):
    x = 220
    y = 400
    for i in mt_text.splitlines():
        txt_surf = font1.render(i, True, BLACK)
        screen.blit(txt_surf, (x, y))
        y += 50


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rectangle.collidepoint(event.pos):
                random_number = randint(1, 100)
                number_attempt = 0
                text = ''
                display_text = ''
                display_text1 = 'Enter number from 1 to 100:'
            try:
                if button_rect.collidepoint(event.pos):
                    if int(text) == random_number:
                        display_text = (f'Your number: {text} is true \n'
                                        f'Congratulations!!!')
                        random_number = None
                        display_text1 = 'Click "Play game"'
                        text = ''
                        break
                    elif int(text) < random_number:
                        display_text = (f'Your number: {text} \n'
                                        f'Lesser')
                    elif int(text) > random_number:
                        display_text = (f'Your number: {text} \n'
                                        f'Bigger')
                    text = ''
                    number_attempt += 1
                    if number_attempt >= 10:
                        display_text1 = 'Click "Play game"'
                        display_text = "Try again"
                        random_number = None
            except TypeError:
                display_text = 'Click "Play game"'
                number_attempt = 0
            except ValueError:
                display_text = 'Enter correct number'
                break
            if exit_rect.collidepoint(event.pos):
                pygame.quit()
                quit()

    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, play_rectangle, width=5)
    pygame.draw.rect(screen, (66, 245, 138), play_rectangle1)
    text_button1 = font.render('Play game', True, BLACK)
    screen.blit(text_button1, (play_rectangle.x + 100, play_rectangle.y + 5))
    pygame.draw.rect(screen, WHITE, exit_rect, width=5)
    pygame.draw.rect(screen, (66, 245, 138), exit_rect1)
    text_surf1 = font.render(display_text1, True, BLACK)
    screen.blit(text_surf1, (100, 200))
    text_button2 = font.render('Exit', True, BLACK)
    screen.blit(text_button2, (exit_rect.x + 120, exit_rect.y + 5))
    pygame.draw.rect(screen, WHITE, input_rectangle, width=5)
    pygame.draw.rect(screen, (66, 245, 138), input_rectangle1)
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (input_rectangle.x + 10, input_rectangle.y + 5))
    pygame.draw.rect(screen, WHITE, button_rect, width=5)
    pygame.draw.rect(screen, (66, 245, 138), button_rect1)
    text_button3 = font.render('Enter', True, BLACK)
    screen.blit(text_button3, (button_rect.x + 60, button_rect.y + 5))
    pygame.draw.rect(screen, WHITE, output_rectangle, width=5)
    pygame.draw.rect(screen, (240, 128, 242), output_rectangle1)

    if display_text:
        multiline_text(display_text)
    clock.tick(60)
    pygame.display.flip()
