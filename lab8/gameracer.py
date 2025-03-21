import pygame, sys
from pygame.locals import *
import random

pygame.init()

width, height = 600, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Game")
road = pygame.image.load('road.jpg')
racer_back = pygame.transform.scale(road, (width, height))
fps = pygame.time.Clock()

crash_music = pygame.mixer.Sound('crash.wav')
wi_img = pygame.image.load('win.jpg')
win_img=pygame.transform.scale(wi_img, (500,400))
enemy_img = pygame.image.load('Enemy.png')
player_img = pygame.image.load('Player.png')
co_img = pygame.image.load('coin.png')
coins_img=pygame.transform.scale(co_img ,(50,50))

player_speed = 5
enemy_speed = 6
coin_speed = 3
coins_num = 0
target_coins =5


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coins_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(100, 500),random.randint(-100,-20))

    def move(self):
        self.rect.move_ip(0, coin_speed)
        if self.rect.top > height:
            self.rect.center = (random.randint(100, 500), random.randint(-100,-20))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        self.rect.move_ip(0, enemy_speed)
        if self.rect.top > height:
            self.rect.center = (random.randint(100, 500), -20)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        self.pressed_keys = pygame.key.get_pressed()
        # if self.pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if self.pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)
        if self.pressed_keys[K_LEFT] and self.rect.left>27:
            self.rect.move_ip(-5, 0)
        if self.pressed_keys[K_RIGHT] and self.rect.right<width-27:
            self.rect.move_ip(5, 0)

Player1 = Player()
Enemy1 = Enemy()

coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

all_sprites.add(Player1)
all_sprites.add(Enemy1)

coin = Coins()
coins.add(coin)
all_sprites.add(coin)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

done = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == inc_speed:
            enemy_speed += 1
            coin_speed += 1
            player_speed+=1

    Player1.move()
    Enemy1.move()

    for coin in coins:
        coin.move()

    if pygame.sprite.collide_rect(Player1, Enemy1):
        crash_music.play()
        font = pygame.font.SysFont(None, 75)
        screen.fill((255,255,255))
        text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(text, ((width // 3)-50, (height // 3)+50))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()


    collected_coins = pygame.sprite.spritecollide(Player1, coins, True)

    if collected_coins:
        new_coin=Coins()
        coins.add(new_coin)
        all_sprites.add(new_coin)


    coins_num += len(collected_coins)

    if coins_num >= target_coins:
        screen.blit(win_img, (50,150))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0))  
    screen.blit(racer_back, (0, 0))  
    all_sprites.draw(screen) 

    pygame.display.update()
    fps.tick(60) 
