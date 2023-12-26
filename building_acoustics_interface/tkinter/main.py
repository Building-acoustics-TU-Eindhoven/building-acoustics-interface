import tkinter as tk
from toolbar import *
from graphDisplay import *
from resultsDisplay import *
#from renderer import *
#import os
#import platform
#from object_3d import *
#from camera import *
#from projection import *
#import pygame as pg

# root window
class window():
    def __init__(self):
        #main window
        self.root = tk.Tk() 
        self.root.title("Acoustic UI")
        self.root.configure(background='#9b9b9b')
        screenHeight = self.root.winfo_screenheight()
        screenWidth = self.root.winfo_screenwidth()
        self.root.geometry("{}x{}+0+0".format(screenWidth, screenHeight))
        self.root.state('zoomed')
        self.root.resizable(False, False)

        #sub windows
        self.toolbar = Toolbar(self.root)
        self.graph_display = graphDisplay(self.root)
        self.results_display = resultsDisplay(self.root)
        #self.renderer = Frame(self.root, width=750, height=750, highlightbackground='#595959', highlightthickness=2)
        #self.embed = Frame(self.renderer, width=748, height=748,)
        #self.renderer.pack(side="left")
        #self.embed.pack()

        #this embeds the pygame window
        #os.environ['SDL_WINDOWID'] = str(self.embed.winfo_id())
        #sytem = platform.system()
        #if sytem == "windows":
        #    os.environ['SDL_VIDEODRIVER'] == 'windib'
        #elif sytem == "Linux":
        #    os.environ['SDL_VIDEODRIVER'] = 'x11'

        #self.root.update_idletasks()
        self.root.mainloop()

ui = window()