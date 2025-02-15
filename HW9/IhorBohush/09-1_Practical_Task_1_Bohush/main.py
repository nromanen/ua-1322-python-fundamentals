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
    """Creating multiline text to display the result in some rows in the output_rectangle"""
    x = 220
    y = 400
    for i in mt_text.splitlines():
        txt_surf = font1.render(i, True, BLACK)
        screen.blit(txt_surf, (x, y))
        y += 50


def enter_button(guess_text, random_num, number, scr_text):
    """Comparison the number entered by user with the random number and displaying the result
    into the output rectangle"""
    screen_text = ''
    try:
        # If the user guessed the number, the game corresponds the congratulatory message and stops
        if int(guess_text) == random_num:
            screen_text = (f'Your number: {guess_text} is true \n'
                           f'Congratulations!!!')
            random_num = None
            scr_text = 'Click "Play game"'  # The second text above the input row
            guess_text = ''
            return screen_text, scr_text, number, random_num, guess_text
        # The user gets message if entered number is bigger or lesser the random number
        elif int(guess_text) < random_num:
            screen_text = (f'Your number: {guess_text} \n'
                           f'Lesser')
        elif int(guess_text) > random_num:
            screen_text = (f'Your number: {guess_text} \n'
                           f'Bigger')
        guess_text = ''
        number += 1

        if number == 10:  # The user has 10 tries
            scr_text = 'Click "Play game"'
            screen_text = "Try again"
            random_num = None
    # If the user enters the number after 10 tries or after guessed it, the random number becomes None,
    # and it cannot to comparison these numbers, that's why an error occurs as TypeError and the game
    # asks to click 'Play game'
    except TypeError:
        screen_text = 'Click "Play game"'
        number = 0
    # The ValueError occurs if the user enters not number or empty value
    except ValueError:
        screen_text = 'Enter correct number'
    return screen_text, scr_text, number, random_num, guess_text


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and input_active:  # Entering the number into the input row
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rectangle.collidepoint(event.pos):  # Click the button 'Play game'
                random_number = randint(1, 100)
                number_attempt = 0
                text = ''
                display_text = ''
                display_text1 = 'Enter number from 1 to 100:'  # The first text above the input row

            if button_rect.collidepoint(event.pos):  # Click the button 'Enter'
                result_enter = enter_button(text, random_number, number_attempt, display_text1)
                display_text = result_enter[0]
                display_text1 = result_enter[1]
                number_attempt = result_enter[2]
                random_number = result_enter[3]
                text = result_enter[4]

            if exit_rect.collidepoint(event.pos):  # Click the button 'Exit' to exit the game
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
