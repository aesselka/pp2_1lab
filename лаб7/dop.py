import pygame
import os 
import time
pygame.init()
height,width=677,677
screen=pygame.display.set_mode((677,677))
pygame.display.set_caption("Labirint")

labirint=pygame.image.load('labur.png')
clock=pygame.time.Clock()

radius=25
x=height//2
y=height//2
speedb=20
fps=60

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    screen.fill((255, 255, 255))
    screen.blit(labirint, (0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.flip()
    
    
    key=pygame.key.get_pressed()
    if key[pygame.K_UP] and y - radius - speedb >= 0:
        y-=speedb
    if key[pygame.K_DOWN] and y + radius + speedb <= height:
        y+=speedb
    if key[pygame.K_RIGHT] and x+radius+speedb<=width:
        x+=speedb
    if key[pygame.K_LEFT] and x-radius-speedb>=0:
        x-=speedb
    clock.tick(fps)
pygame.quit()
