import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shake Game")
clock = pygame.time.Clock()

wi_img = pygame.image.load('win.jpg')
win_img=pygame.transform.scale( wi_img , (500,400))

block=pygame.image.load('square.png')
block_img=pygame.transform.scale(block ,(20,20))

speed = 5 
block_size = 20
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
score = 0
target_wins=30
font_style = pygame.font.SysFont("Times New Roman", 25)
# функция для отображения сообщений 
def message(msg, color, x0, y0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x0, y0])
# основная игровая логика
def gameloop():
    game_over = False
    game_close = False
    # first position
    x = WIDTH / 2
    y = HEIGHT / 2
    # first speed
    x_speed = 0
    y_speed = 0
    # snake
    snake_list = []
    len_snake = 1

    # GENERATION FOOD
    foodx = round(random.randint(0, WIDTH - block_size) / block_size) * block_size
    foody = round(random.randint(0, HEIGHT - block_size) / block_size) * block_size
    score = 0

    while not game_over:
        while game_close: #если змейка столкнулась с собой или стенкой
            screen.fill(BLACK)
            message("lost", RED, WIDTH / 5, HEIGHT / 4) # сообщение о поражении
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # нажал q -выходим
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: #нажал с -начинаем заново
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # управление змейкой с помощью стрелок
                if event.key == pygame.K_LEFT and x_speed == 0:  
                    x_speed = -block_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT and x_speed == 0:  
                    x_speed = block_size
                    y_speed = 0   
                elif event.key == pygame.K_UP and y_speed == 0: 
                    x_speed = 0
                    y_speed = -block_size
                elif event.key == pygame.K_DOWN and y_speed == 0:  
                    x_speed = 0
                    y_speed = block_size

        # check enter za granici
        if (x >= WIDTH or x < 0) or (y >= HEIGHT or y < 0):
            game_close = True

        x += x_speed
        y += y_speed
        screen.fill(BLACK)

        # сетка
        for i in range(0, WIDTH, block_size):
            for j in range(0, HEIGHT, block_size):
                pygame.draw.rect(screen, WHITE, (i, j, block_size, block_size), 1)

        # food draw
        pygame.draw.rect(screen, RED, [foodx, foody, block_size, block_size])

        # draw snake
        head = []


        head.append(x)
        head.append(y)
        snake_list.append(head)
        if len(snake_list) > len_snake:
            del snake_list[0]

        # check ne staknulsya s telom
        for i in snake_list[:-1]:  
            if i == head:
                game_close = True

        # draw all segments of snake
        for block in snake_list:
            # pygame.draw.image(screen, block_img, [block[0], block[1]])
            screen.blit(block_img, [block[0], block[1]])

        # check eating food
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
            foody = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size
            len_snake += 1
            score += 5

        # message count
        message("Score: " + str(score), WHITE, 10, 10)
        pygame.display.update()
        clock.tick(speed)

        #проверка на победу
        if score >= target_wins:
            screen.blit(win_img, (50,150))#показываем картинку победы
            pygame.display.update()
            pygame.time.delay(2000) # зардержка на 2 секунды
    pygame.quit()
    quit()
gameloop()