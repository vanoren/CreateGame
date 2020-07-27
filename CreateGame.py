from tkinter import *

def window(size, name):
    global window_game
    window_game = Tk()
    window_game.geometry(size)
    window_game.title(name)
    window_game.mainloop()