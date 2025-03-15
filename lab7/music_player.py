import pygame
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
pygame.init()
pygame.mixer.init(frequency=44100, size=-16,channels=2,buffer=4096)
root=Tk()
root.geometry("516x700+340+10")
root.title("Assel's favorite songs")
root.config(bg="#f0adde")
root.resizable(False,False)
mixer.init()
lower_frm=Frame(root,bg="#000000", width=516 , height=200)
lower_frm.place(x=0,y=00)
frmcount=32
frms=[PhotoImage(file=os.path.join(os.path.dirname(__file__), 'gifsss.mp4'), format='gif -index %i' % i) for i in range(frmcount)]
def update(ind):
    frame= frms[ind]
    ind+=1
    if ind== frmcount:
        ind=0
        lbl.config(image=frame)
        root.after(40,update, ind)
try:
    pygame.mixer.music.load('first.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(0)
except pygame.error as e:
    print("Ошибка загрузки музыки ")
# done= False
# while not done:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             done= True

#     pygame.display.flip()

