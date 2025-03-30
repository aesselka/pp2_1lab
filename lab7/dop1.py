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
fps=60
speedb=20
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
    if key[pygame.K_UP]:
        y-=speedb
    if key[pygame.K_DOWN]:
        y+=speedb
    if key[pygame.K_RIGHT]:
        x+=speedb
    if key[pygame.K_LEFT]:
        x-=speedb
    if x<radius:
        x=radius
    if x>width-radius:
        x=width-radius
    if y<radius:
        y=radius
    if y>height-radius:
        y=height-radius
    clock.tick(fps)
pygame.quit()