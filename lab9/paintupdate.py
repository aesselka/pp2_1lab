import pygame
import sys

pygame.init()

W, H = 800, 600
b_size = 1

collist = pygame.image.load('pp.png')
collist = pygame.transform.scale(collist, (200, 600))
clock = pygame.time.Clock()
#список объектов для рисования (будут храниться все нарисованные элементы)
objects = []
#флаги для разных режимов рисования
draw_circle_mod = False
draw_rect_mod = True # по умолчанию выбран режим рисования прямоугольников
draw_erase_mode = False  
mode = "Rectangle"
draw_rhomb_mod = False
draw_rt_mod = False
draw_et_mod = False
draw_square_mod = False
#список цветов 
colors = [
    pygame.Color('white'),   
    pygame.Color('red'),     
    pygame.Color('blue'),    
    pygame.Color('green'),   
    pygame.Color('yellow'),  
    pygame.Color('black')    # Background color (black)
]
#переменная для отслеживания состояния рисования
risuiu = False

cur_col = colors[0]  # start with white
bord_col = colors[5]  # background color black
#создаем экран с указанными размерами
screen = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# проверка на выход из программы
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed() # получаем нажатые клавиши
    curssor = pygame.mouse.get_pos() #получаем текущие координаты мыши
    cursor = pygame.mouse.get_pressed() #првоеряем нажаты ли кнопки мыши
    screen.fill(colors[5])   #очищаем жкран заполянем черным фоном

    # Перерисовываем все объекты
    for obj in objects:
        if obj[0] == "rect": # если объект - прямоугольник
            _, pos, w, h, color, size = obj
            pygame.draw.rect(screen, color, (pos[0], pos[1], w, h), size)
        elif obj[0] == "circle": 
            _, center, radius, color, size = obj
            pygame.draw.circle(screen, color, center, radius, size)
        elif obj[0] == "erase":
            _, pos, size = obj
            pygame.draw.circle(screen, colors[5], pos, size)
        elif obj[0] == "romb":
            _, points, color, size = obj
            pygame.draw.polygon(screen, color, points, size)
        elif obj[0] == "equilateral triangle":
            _, points, color, size = obj
            pygame.draw.polygon(screen, color, points, size)
        elif obj[0] == "right triangle":
            _, points, color, size = obj
            pygame.draw.polygon(screen, color, points, size)
        elif obj[0] == "square":
            _, points, length, color, size = obj
            pygame.draw.rect(screen, color, (points, (length, length)), size)

    # draw mode rychag
    if pressed[pygame.K_o]:
        draw_circle_mod = True
        draw_rect_mod = False
        draw_erase_mode = False
        draw_rhomb_mod = False
        draw_rt_mod = False
        draw_et_mod = False
        draw_square_mod = False
    if pressed[pygame.K_r]:
        draw_circle_mod = False
        draw_rect_mod = True
        draw_erase_mode = False
        draw_rhomb_mod = False
        draw_rt_mod = False
        draw_et_mod = False
        draw_square_mod = False
    if pressed[pygame.K_h]:  # rhomb
        mode = "Rhomb"
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_rhomb_mod = True
        draw_rt_mod = False
        draw_et_mod = False
        draw_square_mod = False
    if pressed[pygame.K_t]:  # right triangle
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_rhomb_mod = False
        draw_rt_mod = True
        draw_et_mod = False
        draw_square_mod = False
    if pressed[pygame.K_q]:  # equilateral triangle
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_rhomb_mod = False
        draw_rt_mod = False
        draw_et_mod = True
        draw_square_mod = False
    if pressed[pygame.K_l]:  # square
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_rhomb_mod = False
        draw_rt_mod = False
        draw_et_mod = False
        draw_square_mod = True

    # Rectangle drawing
    if draw_rect_mod:
        if cursor[0] and not risuiu: # если нажата левая кнопка мыши и рисование еще не начато
            risuiu = True
            start_pos = curssor# сохраняем начальную позицию
        elif not cursor[0] and risuiu:# если кнопка мыши отпущена
            end_pos = curssor # сохраняем конечную позицию
            x1, y1 = start_pos
            x2, y2 = end_pos

            left = min(x1, x2) # вычисляем координаты левого верхнего угла прямоугольника
            top = min(y1, y2)
            width = abs(x2 - x1) # вычисляем ширину и высоту
            height = abs(y2 - y1)

            objects.append(("rect", (left, top), width, height, cur_col, b_size)) # добавляем объект в список
            risuiu = False

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            pygame.draw.rect(screen, cur_col, (left, top, width, height), b_size)

    # Drawing circle 
    if draw_circle_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pygame.draw.circle(screen, cur_col, center, radius, b_size)

            objects.append(("circle", center, radius, cur_col, b_size))
            risuiu = False

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pygame.draw.circle(screen, cur_col, center, radius, b_size)

    # Right triangle
    if draw_rt_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            points = [
                ((x1 + x2) // 2, y1),
                (x2, y2),
                (x1, y2)
            ]

            objects.append(("right triangle", points, cur_col, b_size))
            risuiu = False

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            points = [
                ((x1 + x2) // 2, y1),
                (x2, y2),
                (x1, y2)
            ]
            pygame.draw.polygon(screen, cur_col, points, b_size)

    # Equilateral triangle
    if draw_et_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2, y2 = end_pos
            points = [
                (x1, y1),
                (x2, y2),
                (x1, y2)
            ]
            objects.append(("equilateral triangle", points, cur_col, b_size))
            risuiu = False
        if risuiu:
            x1, y1 = start_pos
            end_pos = curssor
            x2, y2 = end_pos
            points = [
                (x1, y1),
                (x2, y2),
                (x1, y2)
            ]
            pygame.draw.polygon(screen, cur_col, points, b_size)
#rhomb
    if draw_rhomb_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1,y1 = start_pos
            x2,y2 = end_pos
            size = min(abs(x2 - x1), abs(y2 - y1)) // 2
            points = [
                (x1, y1 - size), 
                (x1 + size, y1),
                (x1, y1 + size), 
                (x1 - size, y1)
            ]
            
            objects.append(("rhomb",points,cur_col,b_size))
            risuiu = False

        if risuiu:
            
            x1, y1 = start_pos
            end_pos = curssor
            x2, y2 = end_pos
            size = min(abs(x2 - x1), abs(y2 - y1)) // 2  # get the size of rhomb
            points = [
                (x1, y1 - size), 
                (x1 + size, y1),
                (x1, y1 + size), 
                (x1 - size, y1)
            ]
            pygame.draw.polygon(screen,cur_col,points,b_size)

    # Square
    if draw_square_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2, y2 = end_pos
            length = max(abs(x2 - x1), abs(y2 - y1))
            left = x1 if x2 >= x1 else x1 - length
            top = y1 if y2 >= y1 else y1 - length
            objects.append(("square", (left, top), length, cur_col, b_size))
            risuiu = False

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            length = max(abs(x2 - x1), abs(y2 - y1))
            left = x1 if x2 >= x1 else x1 - length
            top = y1 if y2 >= y1 else y1 - length

            pygame.draw.rect(screen, cur_col, (left, top, length, length), b_size)

    # Eraser mode
    if draw_erase_mode:
        if cursor[0]:  # if pressed key 0
            pygame.draw.circle(screen, colors[5], curssor, b_size)  # eraser circle
            objects.append(("erase", curssor, b_size))
  # увеличение/уменьшение размера кисти
    if pressed[pygame.K_UP] and b_size < 100:
        b_size += 1 # увеличение кисти

    if pressed[pygame.K_DOWN] and b_size > 1:
        b_size -= 1  # уменьшение кисти

    # Draw cursor
    pygame.draw.circle(screen, bord_col, curssor, b_size + 2)
    pygame.draw.circle(screen, cur_col, curssor, b_size)


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
        draw_rhomb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = False
        bord_col = colors[0]
        cur_col = colors[5]  # use black for eraser
        
    screen.blit(collist, (600, 0)) # отображаем панель инструментов
    clock.tick(200) # ограничиваем частоту обновлений экрана
    pygame.display.update()