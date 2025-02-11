import pygame
import random
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock() # how fast the screen updates
gameDisplay = pygame.display.set_mode((800,650)) # game display settings
pygame.display.set_caption("Try to guess a number!") # name in the game window

color_blue = pygame.Color('lightskyblue3')
font = pygame.font.SysFont('Calibri', 25, True, False)
font_small = pygame.font.SysFont('Calibri', 18, True, False)

# surface = pygame.Surface((100, 100))

image = pygame.image.load("image_monkey.jpg")
image = pygame.transform.scale(image, (460, 307))

done = False

def render_text(text, pos, font, color=BLACK):
    """renders text on the game screen"""
    text_surface = font.render(text, True, BLACK)
    gameDisplay.blit(text_surface, pos)

def guess_number ():
    """runs the number guessing game"""
    correct_number = random.randint(1, 100)
    attempt = 0
    max_attempts = 10

    input_box = pygame.Rect(350, 130, 100, 40)
    user_text = ""
    result = ""
    no_attempts_left = False
    won = False

    while True:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                sys.exit()

            if not no_attempts_left:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if len(user_text) < 3:
                            user_text += event.unicode
                    if event.key == pygame.K_RETURN:
                        if user_text.strip().isdigit():
                            user_number = int(user_text)
                            attempt += 1

                            if user_number > correct_number:
                                result = f"The number is smaller than {user_number}"
                            elif user_number < correct_number:
                                result = f"The number is bigger than {user_number}"
                            else:
                                result = (f"Congrats! {user_number} is the correct number!")
                                won = True
                        else:
                            result = "Hmm, this is not a number. Please enter a number."

                        user_text = ""
                        if attempt >= max_attempts and not won:
                            result = f"Oops, you run out of attempts. The number was {correct_number}."
                            no_attempts_left = True

        gameDisplay.fill(WHITE)

        pygame.draw.rect(gameDisplay, color_blue, input_box, 2, 5)
        text_surface = font.render(user_text, True, (0, 0, 0))
        gameDisplay.blit(text_surface,(input_box.x + 5, input_box.y + 5))

        gameDisplay.blit(image, (170, 300))

        render_text("Try to guess a number from 1 to 100", (170, 30), font)
        render_text("Write your number and press Enter", (170, 80), font_small)
        render_text(f"Attempts used: {attempt}/{max_attempts}", (170, 250), font_small)
        render_text(result, (170, 200), font_small)

        pygame.display.flip()
        clock.tick(60)	# Limit to 60 frames per second

guess_number ()