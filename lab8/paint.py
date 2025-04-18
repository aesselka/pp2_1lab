import pygame 
import sys

pygame.init()

W, H = 800,600
b_size = 1 #начальный размер кисти
#загружаем изоб для панели инструментов 
collist = pygame.image.load('pp.png')
collist = pygame.transform.scale(collist, (200, 600))
clock = pygame.time.Clock()
#список обьектов на экране
objects = []
draw_circle_mod = False# режим рисования круга
draw_rect_mod = True # режим рисования рект 
draw_erase_mode = False  # режим стирания
colors = [
    pygame.Color('white'),   
    pygame.Color('red'),     
    pygame.Color('blue'),    
    pygame.Color('green'),   
    pygame.Color('yellow'),  
    pygame.Color('black')    # Background color (black)
]

risuiu = False # переменная для отслеживания состояния рисования

cur_col = colors[0]  # start with white
bord_col = colors[5]  # background color black
#создаем экран
screen = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #выход из игры
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed() # чек нажатые клавиши
    curssor = pygame.mouse.get_pos() # гет позицию курсора
    cursor = pygame.mouse.get_pressed() # гет статуус кнопок мыши
    screen.fill(colors[5])  # Очистка экрана, черный фон
#отрисовываем все обьекты
    for obj in objects:
        if obj[0] == "rect": # если обьект - рект
            _, pos, w, h, color, size = obj
            pygame.draw.rect(screen, color, (pos[0], pos[1], w, h), size)
        elif obj[0] == "circle": # если обьект -круг
            _, center, radius, color, size = obj
            pygame.draw.circle(screen, color, center, radius, size)
        elif obj[0] == "erase": # если обьект -стерка
            _, pos, size = obj
            pygame.draw.circle(screen, colors[5], pos, size)#рисуем белон пятно

    # draw mode rychag
    if pressed[pygame.K_o]:
        draw_circle_mod = True
        draw_rect_mod = False
        draw_erase_mode = False
    if pressed[pygame.K_r]:
        draw_circle_mod = False
        draw_rect_mod = True
        draw_erase_mode = False

    # retrangle drawing
    if draw_rect_mod:
        if cursor[0] and not risuiu: #если нажата левая кнопка мыши и рисование не начато
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu: #если отпустили кнопку мыши
            end_pos = curssor
            x1, y1 = start_pos
            x2, y2 = end_pos

            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            objects.append(("rect", (left, top), width, height, cur_col, b_size)) #objects.append(("rect", (left, top), width, height, cur_col, b_size))  #
            risuiu = False

        if risuiu: # если рисуем рект 
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            pygame.draw.rect(screen, cur_col, (left, top, width, height), b_size)

    # drawing circle 
    if draw_circle_mod:
        if cursor[0] and not risuiu: #если нажата левая кнопка мыши и рисовнаие не начато
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu: # если отпустили кнопку мыши
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pygame.draw.circle(screen, cur_col, center, radius, b_size)

            objects.append(("circle", center, radius, cur_col, b_size)) # добаляем круг в список обьектов
            risuiu = False

        if risuiu: #если рисуме круг
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pygame.draw.circle(screen, cur_col, center, radius, b_size)

    # eraser mode
    if draw_erase_mode:
        if cursor[0]:  # if pressed key 0
            pygame.draw.circle(screen, colors[5], curssor, b_size)  # eraser circle
            objects.append(("erase", curssor, b_size)) #добавляем еразер в лист обьектов

# увеличение и уменьшение размера кисти
    if pressed[pygame.K_UP] and b_size < 100:
        b_size += 1
        
    if pressed[pygame.K_DOWN] and b_size > 1:
        b_size -= 1

    # draw the curssor
    pygame.draw.circle(screen, bord_col, curssor, b_size + 2) # обводка курсора
    pygame.draw.circle(screen, cur_col, curssor, b_size) # сам курсор

    # Key mappings for color change
    if pressed[pygame.K_a]:
        cur_col = colors[0]  # W
    if pressed[pygame.K_b]:
        cur_col = colors[1]  # R
    if pressed[pygame.K_c]:
        cur_col = colors[2]  # B
    if pressed[pygame.K_d]:
        cur_col = colors[3]  # G
    if pressed[pygame.K_e]:
        cur_col = colors[4]  # Y

    # perekluchenya na rezhim ctiranya (0)
    if pressed[pygame.K_0]:
        draw_erase_mode = True
        draw_circle_mod = False
        draw_rect_mod = False
        bord_col = colors[0] # цвет фона для стирания 
        cur_col = colors[5] # use black for eraser
#выводим панель инструментов
    screen.blit(collist, (600, 0))
    clock.tick(200) # органичения частот кадров
    pygame.display.update()
