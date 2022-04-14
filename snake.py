import pygame
from random import randint
from pygame.locals import *
from sys import exit

# randomly set apple spawn


def position_20():
    x = randint(0, 590)
    y = randint(0, 590)
    return (x//20*20, y//20*20)

# identify collision of the snake's head with her body or with the apple


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# open the game window
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

# initial body snake cosntruction
snake = [(200, 200), (220, 200), (240, 200),
         (260, 200), (280, 200), (300, 200)]
snake_skin = pygame.Surface((20, 20))
snake_skin.fill((50, 205, 50))

# body apple construction and set randomly spawn
apple = pygame.Surface((20, 20))
apple.fill((255, 0, 0))
apple_pos = position_20()

# important variables
my_direction = DOWN
clock = pygame.time.Clock()
speed = 14
score = 0
gameOver = False
play = False
with open('record.txt', 'r') as arq:
    for valor in arq:
        record = valor
finish = False
pygame.display.update()

while not finish:
    # home screen
    while not play:
        finish = True
        home_font = pygame.font.Font('freesansbold.ttf', 60)
        home_screen = home_font.render('SNAKE GAME', True, (255, 255, 255))
        home_rect = home_screen.get_rect()
        home_rect.midtop = (300, 15)
        screen.blit(home_screen, home_rect)
        mouse = pygame.mouse.get_pos()
        button = pygame.draw.rect(screen, (255, 255, 255), (150, 500, 300, 70))
        button_font = pygame.font.Font('freesansbold.ttf', 60)
        button_screen = button_font.render('JOGAR', True, (0, 255, 0))
        button_rect = button_screen.get_rect()
        button_rect.midtop = (300, 510)
        screen.blit(button_screen, button_rect)
        text1_font = pygame.font.Font('freesansbold.ttf', 20)
        text1_screen = text1_font.render(
            'Aumente o tamanho da cobra comendo as maçãs.', True, (255, 255, 255))
        text1_rect = text1_screen.get_rect()
        text1_rect.midtop = (300, 250)
        screen.blit(text1_screen, text1_rect)
        text2_font = pygame.font.Font('freesansbold.ttf', 20)
        text2_screen = text2_font.render(
            'Cuidado com a cabeça!', True, (255, 255, 255))
        text2_rect = text2_screen.get_rect()
        text2_rect.midtop = (300, 300)
        screen.blit(text2_screen, text2_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    play = True

    # game process
    while not gameOver:
        clock.tick(speed)

        # quit game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # command settings
            if event.type == KEYDOWN:
                if event.key == K_UP and my_direction != DOWN:
                    my_direction = UP
                if event.key == K_DOWN and my_direction != UP:
                    my_direction = DOWN
                if event.key == K_RIGHT and my_direction != LEFT:
                    my_direction = RIGHT
                if event.key == K_LEFT and my_direction != RIGHT:
                    my_direction = LEFT

        # increase the snake body when he eats the apple
        if collision(snake[0], apple_pos):
            apple_pos = position_20()
            snake.append((0, 0))
            score += 1
            if score % 5 == 0:
                speed += 2

        # check if snake collided with borders
        if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
            gameOver = True
            break

        # die the snake when he collides with himself
        for c in range(1, len(snake)):
            if collision(snake[0], snake[c]):
                gameOver = True
                break

        # check game over
        if gameOver:
            break

        # move the snake
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
        if my_direction == UP:
            snake[0] = (snake[0][0], snake[0][1] - 20)
        if my_direction == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 20)
        if my_direction == RIGHT:
            snake[0] = (snake[0][0] + 20, snake[0][1])
        if my_direction == LEFT:
            snake[0] = (snake[0][0] - 20, snake[0][1])

        # att the screen and show the elements
        screen.fill((0, 0, 0))
        screen.blit(apple, apple_pos)

        # draw lines
        # vertical
        for x in range(0, 600, 20):
            pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, 600))
        # horizontal
        for y in range(0, 600, 20):
            pygame.draw.line(screen, (40, 40, 40), (0, y), (600, y))

        # show score
        score_font = pygame.font.Font('freesansbold.ttf', 20)
        score_screen = score_font.render(
            f'Score: {score}', True, (255, 255, 255))
        score_rect = score_screen.get_rect()
        score_rect.topleft = (510, 10)
        screen.blit(score_screen, score_rect)

        for pos in snake:
            screen.blit(snake_skin, pos)
        pygame.display.update()

    # show gameover
    while gameOver:
        gameOver_font = pygame.font.Font('freesansbold.ttf', 75)
        gameOver_screen = gameOver_font.render(
            'Game Over', True, (255, 255, 255))
        gameOver_rect = gameOver_screen.get_rect()
        gameOver_rect.midtop = (300, 55)
        screen.blit(gameOver_screen, gameOver_rect)
        if score > int(record):
            record = score
            with open('record.txt', 'w') as arq:
                arq.write(str(record))
            record_font = pygame.font.Font('freesansbold.ttf', 70)
            record_screen = record_font.render(
                'NEW RECORD!', True, (255, 255, 255))
            record_rect = record_screen.get_rect()
            record_rect.midtop = (300, 200)
            screen.blit(record_screen, record_rect)
        recordatual_font = pygame.font.Font('freesansbold.ttf', 45)
        recordatual_screen = recordatual_font.render(
            f'Record atual: {record}', True, (255, 255, 255))
        recordatual_rect = recordatual_screen.get_rect()
        recordatual_rect.midtop = (300, 350)
        screen.blit(recordatual_screen, recordatual_rect)
        restart_font = pygame.font.Font('freesansbold.ttf', 30)
        restart_screen = restart_font.render(
            f'Clique "R" para restart', True, (255, 255, 255))
        restart_rect = restart_screen.get_rect()
        restart_rect.midtop = (300, 480)
        screen.blit(restart_screen, restart_rect)
        credits_font = pygame.font.Font('freesansbold.ttf', 20)
        credits_screen = credits_font.render(
            f'Copyright - João Vitor Schweikart', True, (255, 255, 255))
        credits_rect = credits_screen.get_rect()
        credits_rect.midtop = (300, 560)
        screen.blit(credits_screen, credits_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            # restart game
            if event.type == KEYDOWN:
                if event.key == K_r:
                    # initial body snake cosntruction
                    snake = [(200, 200), (220, 200), (240, 200),
                             (260, 200), (280, 200), (300, 200)]
                    snake_skin = pygame.Surface((20, 20))
                    snake_skin.fill((50, 205, 50))

                    # body apple construction and set randomly spawn
                    apple = pygame.Surface((20, 20))
                    apple.fill((255, 0, 0))
                    apple_pos = position_20()

                    # important variables
                    my_direction = DOWN
                    clock = pygame.time.Clock()
                    speed = 14
                    score = 0
                    gameOver = False
                    play = True
                    finish = False
                    font = pygame.font.Font('freesansbold.ttf', 18)
                    pygame.display.update()
