import pygame
import weather
import re

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
pygame.display.set_caption('Weather')
pygame.display.set_icon(pygame.image.load('images/icon.png'))
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('arial', 24)
text = ''
display_text = ''
input_active = True
input_rectangle = pygame.Rect(100, 100, 400, 40)
input_rectangle1 = pygame.Rect(105, 105, 390, 30)
button_rect = pygame.Rect(530, 100, 170, 40)
button_rect1 = pygame.Rect(535, 105, 160, 30)
output_rectangle = pygame.Rect(100, 200, 600, 300)
output_rectangle1 = pygame.Rect(105, 205, 590, 290)


def multiline_text(mt_text):
    x = 250
    y = 230
    for i in mt_text.splitlines():
        txt_surf = font.render(i, True, BLACK)
        screen.blit(txt_surf, (x, y))
        y += 50


def check_text(text_input):
    if re.match(r"^[a-zA-Z0-9\W]+ +[a-zA-Z]{2}$", text_input) is not None:
        text1 = (text_input.title()).split()
        pattern = re.compile(r",")
        text2 = pattern.findall(text1[-2])
        if not text2:
            text1[-2] = text1[-2] + ','
        text1[-1] = text1[-1].upper()
        text_input = ' '.join(text1)
        if re.search(r"\W*,\W*", text_input):
            text_input = re.sub(r"\W*,\W*", ", ", text_input)
    else:
        text_input = text_input.title()
        if re.search(r"\W+$", text_input):
            text_input = re.sub(r"\W+$", "", text_input)
    return text_input


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    text = check_text(text)
                    try:
                        display_text = weather.weather(text)
                    except KeyError:
                        display_text = 'Enter correct city'
                    except IndexError:
                        display_text = 'Enter correct city'
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                text = check_text(text)
                try:
                    display_text = weather.weather(text)
                except KeyError:
                    display_text = 'Enter correct city'
                except IndexError:
                    display_text = 'Enter correct city'

    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, input_rectangle, width=5)
    pygame.draw.rect(screen, (66, 245, 138), input_rectangle1)
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (input_rectangle.x + 10, input_rectangle.y + 5))
    pygame.draw.rect(screen, WHITE, button_rect, width=5)
    pygame.draw.rect(screen, (66, 245, 138), button_rect1)
    text_button = font.render('Get weather', True, BLACK)
    screen.blit(text_button, (button_rect.x + 30, button_rect.y + 5))
    pygame.draw.rect(screen, WHITE, output_rectangle, width=5)
    pygame.draw.rect(screen, (240, 128, 242), output_rectangle1)

    if display_text:
        multiline_text(display_text)
    clock.tick(60)
    pygame.display.flip()
