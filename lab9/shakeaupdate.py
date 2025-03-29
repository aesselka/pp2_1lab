import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shake Game")
clock = pygame.time.Clock()
wi_img = pygame.image.load('win.jpg')
win_img = pygame.transform.scale(wi_img, (500, 400))
speed = 5
block_size = 20
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
target_wins = 30
font_style = pygame.font.SysFont("Times New Roman", 25)


class SnakeGame:
    def __init__(self):
        self.food_time = 0
        self.game_over = False
        self.game_close = False
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.x_speed = 0
        self.y_speed = 0
        self.snake_list = []
        self.len_snake = 1
        self.foodx = round(random.randint(0, WIDTH - block_size) / block_size) * block_size
        self.foody = round(random.randint(0, HEIGHT - block_size) / block_size) * block_size
        self.score = 0
        self.food_color = self.random_food_color()
        # zapysyvaem vremy poivleniya pishi


    def message(self, msg, color, x0, y0):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [x0, y0])

    def random_food_color(self):
        colors = [BLUE, GREEN, YELLOW, RED]
        return random.choice(colors)
    
    # def reset_food(self):
    #     self.foodx = round(random.randint(0, WIDTH - block_size) / block_size) * block_size
    #     self.foody = round(random.randint(0, HEIGHT - block_size) / block_size) * block_size
    #     self.food_color=self.random_food_color()
    #     self.food_time=pygame.time.get_ticks() #obnovlenya vremya poivlenya novogo apple

    def gameloop(self):
        while not self.game_over:
            
            while self.game_close:
                screen.fill(BLACK)
                self.message("lost", RED, WIDTH / 5, HEIGHT / 4)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.game_over = True
                        self.game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            self.__init__()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.x_speed == 0:
                        self.x_speed = -block_size
                        self.y_speed = 0
                    elif event.key == pygame.K_RIGHT and self.x_speed == 0:
                        self.x_speed = block_size
                        self.y_speed = 0
                    elif event.key == pygame.K_UP and self.y_speed == 0:
                        self.x_speed = 0
                        self.y_speed = -block_size
                    elif event.key == pygame.K_DOWN and self.y_speed == 0:
                        self.x_speed = 0
                        self.y_speed = block_size

            # check enter za granici
            if (self.x >= WIDTH or self.x < 0) or (self.y >= HEIGHT or self.y < 0):
                self.game_close = True

            self.x += self.x_speed
            self.y += self.y_speed
            screen.fill(BLACK)

            # сетка
            for i in range(0, WIDTH, block_size):
                for j in range(0, HEIGHT, block_size):
                    pygame.draw.rect(screen, WHITE, (i, j, block_size, block_size), 1)
#check if 10 sec pass
           
                #  #obnovlenya vremya poivlenya novogo apple

            # food draw
            pygame.draw.rect(screen, self.food_color, [self.foodx, self.foody, block_size, block_size])

            # draw snake
            head = [self.x, self.y]
            self.snake_list.append(head)
            if len(self.snake_list) > self.len_snake:
                del self.snake_list[0]

            # check ne staknulsya s telom
            for i in self.snake_list[:-1]:
                if i == head:
                    self.game_close = True

            # draw all segments of snake
            for block in self.snake_list:
                pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])
            # check eating food
            if self.x == self.foodx and self.y == self.foody:
                self.food_time = pygame.time.get_ticks()

                if self.food_color == GREEN:
                    self.score += 2
                    self.len_snake += 1
                elif self.food_color == RED:
                    self.score -= 2
                    self.len_snake += 1
                elif self.food_color == YELLOW:
                    pass  # no points for yellow
                    self.len_snake += 1
                elif self.food_color == BLUE:
                    self.score += 1
                    self.len_snake += 1
            
                self.foodx = round(random.randrange(0, WIDTH - block_size) / block_size) * block_size
                self.foody = round(random.randrange(0, HEIGHT - block_size) / block_size) * block_size
                self.food_color = self.random_food_color()  #Now calling function properly

            if pygame.time.get_ticks() - self.food_time >= 5000:
                self.foodx = round(random.randint(0, WIDTH - block_size) / block_size) * block_size
                self.foody = round(random.randint(0, HEIGHT - block_size) / block_size) * block_size
                self.food_color=self.random_food_color()
                self.food_time = pygame.time.get_ticks()

            # message count
            self.message("Score: " + str(self.score), WHITE, 10, 10)
            pygame.display.update()
            clock.tick(speed)

            if self.score >= target_wins:
                screen.blit(win_img, (50, 150))
                pygame.display.update()
                pygame.time.delay(2000)
        pygame.quit()
        quit()

game = SnakeGame()
game.gameloop()
