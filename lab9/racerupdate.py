import pygame, sys
from pygame.locals import *
import random
import time

pygame.init()

width, height = 600, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Game")
road = pygame.image.load('road.jpg')
racer_back = pygame.transform.scale(road, (width, height))
fps = pygame.time.Clock()#chastota kadrov

crash_music = pygame.mixer.Sound('crash.wav')
wi_img = pygame.image.load('win.jpg')
win_img=pygame.transform.scale(wi_img, (500,400))
enemy_img = pygame.image.load('Enemy.png')
player_img = pygame.image.load('Player.png')
co_img = pygame.image.load('coin.png')
coins_img=pygame.transform.scale(co_img ,(70,70))
silv_img=pygame.image.load('silver_coin.png')
silver_img=pygame.transform.scale(silv_img, (50,50))
bron_img=pygame.image.load('brcoin.png')
bronze_img=pygame.transform.scale(bron_img, (50,50))


WHITE=(255,255,255)
player_speed = 5
enemy_speed = 6
coin_speed = 3
coins_num = 0
target_coins =30
font_style = pygame.font.SysFont("Times New Roman", 25)

# функция для отображения сообщений
def message(msg, color, x0, y0):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x0, y0])
#dlya monet
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        coin_type=random.choice(["gold","silver","bronze"])
        if coin_type== "gold":
            self.image=coins_img
        if coin_type=="silver":
            self.image=silver_img
        if coin_type=="bronze":
            self.image=bronze_img
        self.rect=self.image.get_rect()
        # начальная позиция монеты
        self.rect.center=(random.randint(100,500),random.randint(-100,-20))

    def move(self):
        self.rect.move_ip(0,coin_speed) # монета двигается вниз
        if self.rect.top>height: # если монета выходит за экран, она удаляется
            self.kill()

#CLASS FOR ENEMY
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, enemy_speed) # враг двигается вниз
        if self.rect.top > height: # если враг выходит за экран, он появляется снова сверху
            self.rect.center = (random.randint(100, 500), -20)
#class for player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # начальная позиция игрока

    def move(self):
        self.pressed_keys = pygame.key.get_pressed() # проверяем нажатые клавиши
        # if self.pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if self.pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)
        if self.pressed_keys[K_LEFT] and self.rect.left>27:
            self.rect.move_ip(-5, 0)
        if self.pressed_keys[K_RIGHT] and self.rect.right<width-27:
            self.rect.move_ip(5, 0)
# создаем объекты игрока врага и монет
Player1 = Player()
Enemy1 = Enemy()
#group of sprite to make easy to uplavliyat
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(Player1) #ADD PLAYERS IN GROUP OF SPRITE
all_sprites.add(Enemy1)

#ustanovka taimera dlya increase speed
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

done = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == inc_speed:#increase speed every second
            enemy_speed += 1
            coin_speed += 1
            player_speed+=1
#движение
    Player1.move()
    Enemy1.move()

    # genearcia monet s sluchainym vyborom
    if random.randint(0, 100) < 2:  # posibilities of monet
        coin = Coins() # создаем монету
        coins.add(coin)
        all_sprites.add(coin)

    for coin in coins:
        coin.move() # двигаем монеты
#check stolknovenya player with enemy
    if pygame.sprite.collide_rect(Player1, Enemy1):
        crash_music.play() # воспроизводим звук столкновения
        font = pygame.font.SysFont(None, 75)
        screen.fill((255,255,255)) # экран заполняется белым цветом
        text = font.render("Game Over!", True, (255, 0, 0)) # выводим текст "Game Over!"
        screen.blit(text, ((width // 3)-50, (height // 3)+50))
        pygame.display.update()
        pygame.time.delay(2000) # задержка 2 секунды 
        pygame.quit()
        sys.exit()

#proverka sbora monet
    collected_coins = pygame.sprite.spritecollide(Player1, coins, True)
    if collected_coins:
        new_coin=Coins() # создаем новую монету
        coins.add(new_coin)
        all_sprites.add(new_coin)


    coins_num += len(collected_coins) #uvelichivaem schet
# если собрали нужное количество монет, выводим экран победы
    if coins_num >= target_coins:
        screen.blit(win_img, (50,150))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    # message("Score: " + str(coins_num), WHITE, 30, 10)
    # pygame.display.update()
    # fps.tick(100)
    # отрисовываем экран
    screen.fill((0, 0, 0))  
    screen.blit(racer_back, (0, 0))  
    all_sprites.draw(screen) 

    message("Score: " + str(coins_num), WHITE, 30, 10)
    pygame.display.update()

    pygame.display.update()
    fps.tick(60) 