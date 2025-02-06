import pygame
import random

GAME_HEIGHT = 300
GAME_WIDTH = 300
pygame.init()
answer = random.randint(1,100)

class TextDisplay():
    def __init__(self, txt, size, x, y, color = (0, 0, 0)):
        self.txt = txt
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.base_font = pygame.font.Font(pygame.font.match_font('arial'), size)
        self.surface = self.base_font.render(txt, True, self.color)

    def draw(self):
        self.surface = self.base_font.render(self.txt, True, self.color)
        return screen.blit(self.surface, ((GAME_WIDTH - self.surface.get_width())/2 - self.x, self.y))

class RectDisplay():
    def __init__(self, size_x, size_y, x, y, border = None):
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y
        self.border = border
        self.color = pygame.Color('lightskyblue3')

    def draw(self):
        self.rect = pygame.Rect((GAME_WIDTH-self.size_x)/2 - self.x, self.y, self.size_x, self.size_y)
        return pygame.draw.rect(screen, self.color, self.rect) if self.border == None else pygame.draw.rect(screen, self.color, self.rect, self.border)


explain2 = TextDisplay("Guess a number from 1-100", 18, 0, 20)
explain1 = TextDisplay("This is a number guessing game", 18, 0, 0)
sys_msg = TextDisplay("", 22, 0, 100)
button_guess = RectDisplay(100, 32, 0, 200)
button_guess_text = TextDisplay("Guess!", 18, button_guess.x, button_guess.y + button_guess.size_y/6)
button_quit = RectDisplay(100, 32, 0, 250)
button_quit_text = TextDisplay("Quit!", 18, button_quit.x, button_quit.y + button_quit.size_y/6)
input_rect = RectDisplay(40, 32, 0, 140, 2)
input_answer = TextDisplay("", 18, input_rect.x, input_rect.y + input_rect.size_y/6 )
attempts_txt = TextDisplay("Attemps left:", 18, 0, 70)
attempts = TextDisplay("10", 18, -attempts_txt.surface.get_width()/2 - 10, 70, (255, 0, 0))
game_over1 = TextDisplay(f"Game over, you lost!", 30, 0, GAME_HEIGHT/2 - 30, (255, 0, 0))
you_won = TextDisplay("Game over, you Won!!!", 30, 0, GAME_HEIGHT/2 - 30, (0, 255, 0))
replay_button = RectDisplay(100, 32, 0, 200)
replay_text = TextDisplay("Replay", 18, replay_button.x, replay_button.y + replay_button.size_y/6)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((GAME_HEIGHT, GAME_WIDTH))
pygame.display.set_caption('Number Guessing Game')


def check_answer(input: str) -> None:
    try:
        input = int(input)
    except ValueError:
        sys_msg.txt = "NOT A NUMBER!"
        return
    if input == answer:
        sys_msg.txt = "You Won!"
        attempts.txt = "-1"
    elif input > answer:
        sys_msg.txt = f"Answer is smaller than {input}"
        input_answer.txt = ""
        attempts.txt = str(int(attempts.txt)-1)
    else:
        sys_msg.txt = f"Answer is bigger than {input}"
        input_answer.txt = ""
        attempts.txt = str(int(attempts.txt)-1)

def restart() -> None:
    global answer
    attempts.txt = "10"
    sys_msg.txt = ""
    answer = random.randint(1,100)




def game() -> None:
    running = True
    while running:
        game_over2 = TextDisplay(f"correct answer: {answer}", 30, 0, GAME_HEIGHT/2, (255, 0, 0))
        screen.fill((255,255,255))
        button_quit.draw()
        button_quit_text.draw()
        #draw all the objects on screen
        if int(attempts.txt) > 0:
            button_guess.draw()
            button_guess_text.draw()
            input_rect.draw()
            input_answer.draw()
            explain1.draw()
            explain2.draw()
            sys_msg.draw()
            attempts_txt.draw()
            attempts.draw()
        elif attempts.txt == "0":
            game_over1.draw()
            game_over2.draw()
            replay_button.draw()
            replay_text.draw()
        elif attempts.txt == "-1":
            you_won.draw()
            replay_button.draw()
            replay_text.draw()

        #Event management 
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_answer.txt = input_answer.txt[:-1]
                elif event.key == pygame.K_RETURN:
                    check_answer(input_answer.txt)
                    pygame.time.wait(100)
                elif event.key != pygame.K_RETURN:
                    if event.unicode.isdigit():
                        test_result = input_answer.txt + event.unicode
                        if len(input_answer.txt) == 0 and event.unicode == "0":
                            pass
                        elif len(input_answer.txt) < 3 and int(test_result) <= 100:
                            input_answer.txt += event.unicode

        if button_guess.rect.collidepoint(mouse_pos):
            if int(attempts.txt) <= 0:
                if pygame.mouse.get_pressed()[0]:
                    restart()
                    pygame.time.wait(100)
            else:
                if pygame.mouse.get_pressed()[0] and input_answer.txt != "":
                    check_answer(input_answer.txt)
                    pygame.time.wait(100)


        if button_quit.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                running = False




        clock.tick(60)
        pygame.display.flip()



if __name__ == '__main__':
    game()
    pygame.quit()
