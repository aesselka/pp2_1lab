import pygame 
import os
import time
height,widht=736,736
centre=(height//2, widht//2)
_image_library={}
def get_image(path):
    global _image_library
    image= _image_library.get(path)
    if image is None:
        canonicalized_path= path.replace('/', os.sep).replace('\\', os.sep)
       
        image = pygame.image.load(canonicalized_path)
        _image_library[path] =image
    return image

pygame.init()
screen=pygame.display.set_mode((736,736))
clock= pygame.time.Clock()
mickey_body = pygame.image.load('mickey_body.jpg')
mickey_body = pygame.transform.scale(mickey_body, (300, 300)) 
left_hand=pygame.image.load('left_hand.jpg')
right_hand=pygame.image.load('right_hand.png')
left_hand = pygame.transform.scale(left_hand, (100, 40)) 
right_hand = pygame.transform.scale(right_hand, (100,40)) 
MICKEY_X = (736 - 300) // 2  # По центру экрана
MICKEY_Y = (736 - 300) // 2  # По центру экрана
left_pos=[centre[0]-70, centre[1]-150]
right_pos=[centre[0]+70, centre[1]-150]
def blit_rotate_center(surf,image,pos,angle):
    rotated_image=pygame.transform.rotate(image,angle)
    new_rect=rotated_image.get_rect(center=pos)
    surf.blit(rotated_image,new_rect.topleft)
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    current_time=time.localtime()
    minute_angle= -((current_time.tm_min % 60) * 6)  # 6° за минуту
    second_angle = -((current_time.tm_sec % 60) * 6)  # 6° за секунду


    screen.fill((0,0,0))
    screen.blit(get_image('clock_face.jpg'), (0, 0))
    screen.blit(mickey_body, (MICKEY_X, MICKEY_Y))# mickey no hands
    blit_rotate_center(screen, right_hand, right_pos, minute_angle)  # Минутная стрелка
    blit_rotate_center(screen, left_hand, left_pos, second_angle) 

    pygame.display.flip()
    pygame.time.delay(1000)
    clock.tick(60)

pygame.quit()

