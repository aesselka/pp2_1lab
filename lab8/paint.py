import pygame
import time
import sys

pygame.init()

# Настройки экрана
width,heigth=600,600
screen=pygame.display.set_mode((width,heigth))
pygame.display.set_caption("Paint")
clock=pygame.time.Clock()
er=pygame.image.load('eraser.jpg')
er_img=pygame.transform.scale(er, (50,50))
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
colors=[red,green,blue,black]

brush_size=5
drawing=False
cr_tool='circle'
cr_color=black
tools=["circle","line","rect","eraser"]
font_style = pygame.font.SysFont("Times New Roman", 25)

#draw circle
def draw_circle(x,y):
    pygame.draw.circle(screen, cr_color,(x,y), brush_size)

#draw rect
def draw_rect(x,y):
    pygame.draw.rect(screen,cr_color, (x-brush_size,y-brush_size), brush_size)

#draw line
def draw_line(x,y,start_pos):
    pygame.draw.line(screen, cr_color,start_pos, (x,y), brush_size)

def main():
    global drawing, cr_tool, cr_color, brush_size
    start_pos=None
    while True:
        #draw panel instrumentov
        pygame.draw.rect(screen, black, (width - 160, 0, 160, heigth))
        pygame.draw.rect(screen, white, (width - 160, 0, 160, 50))  # panel 
        pygame.draw.rect(screen, white, (width - 160, 50, 160, 50))  # setevaya panel

        # draw button
        pygame.draw.circle(screen, red, (width - 130, 25), 15)
        pygame.draw.rect(screen, green, (width - 100, 10, 30, 30))
        pygame.draw.line(screen, blue, (width - 60, 10), (width - 60, 40), 3)

        # panel choose color
        pygame.draw.rect(screen, red, (width - 130, 55, 30, 30))
        pygame.draw.rect(screen, green, (width - 100, 55, 30, 30))
        pygame.draw.rect(screen, blue, (width - 70, 55, 30, 30))
        pygame.draw.rect(screen, black, (width - 40, 55, 30, 30))
        
        #current tool
        text=font_style.render(f"tool: {cr_tool}", True,black)
        #draw

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            #nazhatii mishy

            if event.type==pygame.MOUSEBUTTONDOWN:
                drawing=True
                start_pos=pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                drawing=False
                start_pos=None

            #vybor instumentov and color
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()

                #choose tools
                if width- 160 <= mouse_pos[0] <= width - 130 and 0 <= mouse_pos[1] <= 50:
                    cr_tool = "circle"
                elif width - 130 <= mouse_pos[0] <= width - 100 and 0 <= mouse_pos[1] <= 50:
                    cr_tool = "rect"
                elif width - 100 <= mouse_pos[0] <= width - 70 and 0 <= mouse_pos[1] <= 50:
                    cr_tool = "line"
                elif width - 70 <= mouse_pos[0] <= width - 40 and 0 <= mouse_pos[1] <= 50:
                    cr_tool = "eraser"

                #choose colors
                if width - 130 <= mouse_pos[0] <= width - 100 and 55 <= mouse_pos[1] <= 85:
                    cr_color = red
                elif width - 100 <= mouse_pos[0] <= width - 70 and 55 <= mouse_pos[1] <= 85:
                    cr_color = green
                elif width - 70 <= mouse_pos[0] <= width - 40 and 55 <= mouse_pos[1] <= 85:
                    cr_color = blue
                elif width - 40 <= mouse_pos[0] <= width - 10 and 55 <= mouse_pos[1] <= 85:
                    cr_color = black


        if drawing:
            mouse_pos=pygame.mouse.get_pos()
            if cr_tool== "circle":
                draw_circle(mouse_pos[0], mouse_pos[1])
            elif cr_tool=="rect":
                draw_rect(mouse_pos[0], mouse_pos[1])
            elif cr_tool=="line":
                draw_line(mouse_pos[0],mouse_pos[1],start_pos)
            elif cr_tool=="eraser":
                pygame.draw.circle(screen,white, mouse_pos,brush_size)
            

        pygame.display.update()
        clock.tick(60)
main()