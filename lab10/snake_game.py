import pygame
import random
import time
import sys
import psycopg2
pygame.init()
sdata=psycopg2.connect(host="localhost", dbname="snake_db" , user="postgres" ,password="12345678" , port=5433)

sdb=sdata.cursor()


sdata.commit()
def customer(username):
    sdb.execute("SELECT id FROM users WHERE username=%s", (username,))
    user=sdb.fetchone()
    if user:
        return user[0]
    else:
        sdb.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        sdata.commit()
        return sdb.fetchone()[0]
def level_current(user_id):
    sdb.execute("SELECT level FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    sdata.commit()
    return row[0] if row else 0
def score_current(user_id):
    sdb.execute("SELECT score FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    sdata.commit()
    return row[0] if row else 0
def speed_current(user_id):
    sdb.execute("SELECT speed FROM user_score WHERE user_id=%s ORDER BY timestamp DESC LIMIT 1", (user_id,))
    row=sdb.fetchone()
    sdata.commit()
    return row[0] if row and row[0] is not None else 5
def save_prog(user_id, level, score, speed):
    sdb.execute("INSERT INTO user_score (user_id, level, score, speed) VALUES (%s, %s, %s, %s)", (user_id, level, score, speed))
    sdata.commit()
def save_score(username, score):
    sdb.execute("SELECT score FROM user_score WHERE username = %s", (username,))
    result = sdb.fetchone()

    if result is None:
        sdb.execute("INSERT INTO user_score (username, score) VALUES (%s, %s)", (username, score))
    else:
        current_score = result[0]
        if score > current_score:
            sdb.execute("UPDATE user_score SET score = %s WHERE username = %s", (score, username))
    
    sdata.commit()

def delete_scores_for_users(username):
    # user_id=iinput("secified username: ")
    sdb.execute("SELECT id FROM users WHERE username=%s",(username,))
    user_id=sdb.fetchone()
    if user_id:
        user_id=user_id[0]
        sdb.execute("DELETE FROM user_score WHERE user_id=%s",(user_id,) )
        sdata.commit()
Width = 600
Height = 600
screen = pygame.display.set_mode((Width, Height))  
def get_username_input():
    input_box = pygame.Rect(Width//2 - 150, Height//2 - 30, 300, 50)
    color_inactive = pygame.Color('gray')
    color_active = pygame.Color('white')
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if len(text) > 0:
                            done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 20:
                            text += event.unicode

        screen.fill(BLACK)
        title = font.render("input your nic", True, WHITE)
        screen.blit(title, (Width//2 - title.get_width()//2, Height//2 - 100))

        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+10))

        pygame.display.flip()
        clock.tick(30)
    return text
# цвета
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CELL = 20  
DARGDRAY = (10, 10, 10)  
score = 0 
level = 0  
speed = 5  

snake_body_img = pygame.image.load('sn.jpg')
snake_body_img = pygame.transform.scale(snake_body_img, (CELL, CELL))  


font = pygame.font.SysFont("Arial",30)

paused=False
# рисования сетки
def grid():
    for i in range(Height // 2):  #  по вертикали
        for j in range(Width // 2):  # по горизонтали
            pygame.draw.rect(screen, DARGDRAY, (i * CELL, j * CELL, CELL, CELL), 1)  # рисуем сетку
# рисования шахматной сетки
def chess_grid():
    colors = [DARGDRAY, BLACK]  # список цветов
    for i in range(Height // 2):
        for j in range(Width // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))  # чередующиеся цвета

def draw_text():
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)  
    screen.blit(score_text, (10, 10))  

class Point:
    def __init__(self, x, y):
        self.x = x  
        self.y = y 
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]  # snake's body
        self.dx = 1  
        self.dy = 0  

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):  
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx  
        self.body[0].y += self.dy  

    def draw(self):
        head = self.body[0] 
        screen.blit(snake_body_img, (head.x * CELL, head.y * CELL))  # body color
        # Отображаем тело змеи
        for segment in self.body[1:]:
            screen.blit(snake_body_img, (segment.x * CELL, segment.y * CELL))  # Рисуем тело с изображением
    def check_collision(self, food):
        global score, level, speed
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:  
            score += food.points 
            score = max(score, 0) 
            if food.color==RED: 
                if score // 10 < level: 
                    level -= 1
                    print(level)
                    screen.fill(RED) 
                    pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                    pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)
                    level_down = font.render("LEVEL DOWN!", True, (0, 0, 0)) 
                    screen.blit(level_down, (Width // 2 - 110, Height // 2 - 30))
                    pygame.display.flip()
                    pygame.time.delay(500) 
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  
            food.update_food(self)  # Update food with new random properties

            if score // 10 > level:  
                level += 1
                speed += 2  # Увеличиваем скорость игры
                
                screen.fill(GREEN)
                pygame.draw.rect(screen, BLACK, (Width // 2 - 215, Height // 2 - 45 - 40, 450, 150), 0, 20)
                pygame.draw.rect(screen, WHITE, (Width // 2 - 190, Height // 2 - 20 - 40, 400, 100), 0, 10)  # next level background
                next_level_text = font.render("NEXT LEVEL!", True, (0, 0, 0)) # налпись о повышении уровня, когда уровень повышается
                screen.blit(next_level_text, (Width // 2 - 110, Height // 2 - 30))
                pygame.display.flip()
                pygame.time.delay(500)  # Pause before continuing the game

    def check_wall_collision(self):
        head = self.body[0]
        # Проверяем, не столкнулась ли змея с границами экрана
        return head.x < 0 or head.x >= Width // CELL or head.y < 0 or head.y >= Height // CELL

    def check_self_collision(self):
        head = self.body[0]
        # Проверяем, не столкнулась ли змея с собой
        return any(segment.x == head.x and segment.y == head.y for segment in self.body[1:])



class Food:
    def __init__(self):
        self.pos = Point(0, 0)
        
        self.points, self.color = self.random_food_properties()  
        self.spawn_time = None  
        self.spawn(None)  
    def random_food_properties(self):

        food_type = random.choice(["green", "red", "yellow"])
        if food_type == "green":
            return 5, GREEN  # 5 points for green food
        elif food_type == "red":
            return -2, RED  # -2 points for red food
        elif food_type == "yellow":
            return 2, YELLOW  # 2 point for yellow food

    def spawn(self, snake):
        while True:
            new_x = random.randint(0, Width // CELL - 3)
            new_y = random.randint(0, Height // CELL - 3)
         
            if snake and any(segment.x == new_x and segment.y == new_y for segment in snake.body):
                
                continue
            self.pos = Point(new_x, new_y)
            self.spawn_time = pygame.time.get_ticks() # записываем время появления еды
            break

    def draw(self):
     
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL), 0, 20)
    
    def update_food(self, snake):
 
        self.points, self.color = self.random_food_properties()  
        self.spawn(snake)  
    
clock = pygame.time.Clock()
food = Food()
snake = Snake()

nup=False
ndown=False
nright=True
nleft=False
running = True
username = get_username_input()
user_id = customer(username)
level = level_current(user_id)
score=score_current(user_id)
speed=speed_current(user_id)
def welcome(username, level):
    screen.fill(BLACK)
    msg = font.render(f"username: {username}", True, WHITE)
    lvl = font.render(f"cur level: {level}", True, WHITE)
    sc=font.render(f"cur score: {score}", True, WHITE)
    screen.blit(msg, (Width // 2 - msg.get_width() // 2, Height // 2 - 50))
    screen.blit(lvl, (Width // 2 - lvl.get_width() // 2, Height // 2 + 10))
    screen.blit(sc, (Width // 2 - lvl.get_width() // 2, Height // 2 + 40))
    pygame.display.flip()
    pygame.time.delay(2000)
welcome(username, level)
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False # выход из игры при закрытии окна
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                paused = not paused  # переключаем паузу
                if paused:
                    save_prog(user_id, level, score, speed)
                    print("paused")
            if event.key == pygame.K_ESCAPE:  # Выход из игры при нажатии ESC
                running = False
            if event.key == pygame.K_RIGHT and not nleft:
                nright = True
                snake.dx = 1
                nup = False
                ndown = False
                nleft = False
                snake.dy = 0
            elif event.key == pygame.K_LEFT and not nright:
                nleft=True
                nup=False
                ndown=False
                nright=False
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and not nup:
                nleft=False
                nup=False
                ndown=True
                nright=False
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and not ndown:
                nleft=False
                nup=True
                ndown=False
                nright=False
                snake.dx = 0
                snake.dy = -1
    if paused:
        screen.fill(BLACK)
        pause_text = font.render("PAUSED", True, WHITE)
 
        screen.blit(pause_text, (Width // 2 - pause_text.get_width() // 2, Height // 2 - 30))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_prog(user_id, level, score, speed)

                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    paused = False
                    waiting = False
            clock.tick(10)
 
    chess_grid()
    snake.move()
   

    if snake.check_wall_collision() or snake.check_self_collision():
        screen.fill(WHITE) 

        lose_text = font.render("lose", True, (0, 0, 0))
        screen.blit(lose_text, (Width//2 -110, Height//2-30))
        pygame.display.update()
          
        time.sleep(3)
        pygame.quit() 
        save_prog(user_id, level, score, speed)
        print(f" уровень {level}, счёт {score}")
        username=input("specified username: ")
        delete_scores_for_users(username)
        sys.exit()
    snake.check_collision(food)

    if pygame.time.get_ticks() - food.spawn_time > 5000:  
        food.update_food(snake)


    snake.draw()
    food.draw()
    draw_text()


    pygame.display.flip()

    clock.tick(speed)
# username=input("specified username: ")
# delete_scores_for_users(username)
pygame.quit()  
sys.exit()
sdata.close()
sdb.close()