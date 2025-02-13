import pygame
import random


pygame.init()


display = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Відгадай число")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 10
input_text = ""
message = "Введіть число від 1 до 100"
game_over = False
clock = pygame.time.Clock()
input_box = pygame.Rect(180, 160, 250, 40)  # x, y, ширина, висота

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_RETURN:
                    if input_text:
                        input_text = int(input_text)
                        attempts += 1
                        if input_text == secret_number:
                            message = "Ви виграли!"
                            game_over = True
                        elif input_text < secret_number:
                            message = "Загадане число більше!"
                        else:
                            message = "Загадане число менше!"
                        if attempts >= max_attempts:
                            message = f"Ви програли! Загадане число: {secret_number}"
                            game_over = True
                        input_text = ""
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode
    display.fill(WHITE)
    msg_surface = font.render(message, True, BLACK)
    display.blit(msg_surface, (150, 100))
    pygame.draw.rect(display, BLACK, input_box, 2)
    input_surface = font.render(input_text, True, BLACK)
    display.blit(input_surface, (input_box.x + 5, input_box.y + 5))
    attempts_surface = font.render(f"Спроби: {attempts}/{max_attempts}", True, BLACK)
    display.blit(attempts_surface, (235, 235))
    pygame.display.update()
    clock.tick(30)
    if event.type == pygame.QUIT:
        pygame.quit()
        break