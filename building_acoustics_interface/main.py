from tkinter import *
from toolbar import *
from graphDisplay import *
from resultsDisplay import *
from renderer import *
import os
import platform

# root window
root = Tk()
root.title('Acoustic UI')
screenHeight = root.winfo_screenheight()
screenWidth = root.winfo_screenwidth()
root.geometry("{}x{}+0+0".format(screenWidth, screenHeight))
root.state('zoomed')
root.resizable(False, False)

toolbar = Toolbar(root)
graph_display = graphDisplay(root)
results_display = resultsDisplay(root)
pygame_frame = Frame(root, width=750, height=750, highlightbackground='#595959', highlightthickness=2)
embed = Frame(pygame_frame, width=748, height=748,)
pygame_frame.pack(side="left")
embed.pack()

#tihs embeds the pygame window
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
sytem = platform.system()
if sytem == "windows":
    os.environ['SDL_VIDEODRIVER'] == 'windib'
elif sytem == "Linux":
    os.environ['SDL_VIDEODRIVER'] = 'x11'

renderer = SoftwareRender()
root.update_idletasks()
root.mainloop()