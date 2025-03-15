import pygame 
from tkinter import Tk,Button
pygame.mixer.init()
songs=["first.mp3" , "second.mp3" , "third.mp3"]
current_index=0

def play():
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_song():
    global current_index
    current_index=(current_index+1)%len(songs)
    play()
def pr_song():
    global current_index
    current_index=(current_index-1)%len(songs)
    play()

root=Tk()
root.title("Spotify")
root.geometry("200x150")
root.config(bg="#faaff6")

btn_play= Button(root, text="Play", width=10, command=play)
btn_stop= Button(root,text="Stop", width=10,command=stop)
btn_next=Button(root,text="Next", width=10, command=next_song)
btn_prev=Button(root,text="Prev", width=10, command=pr_song)

btn_play.pack(pady=5)
btn_stop.pack(pady=5)
btn_next.pack(pady=5)
btn_prev.pack(pady=5)
root.mainloop()