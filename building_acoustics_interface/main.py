from tkinter import *
from toolbar import *
from graphDisplay import *
from resultsDisplay import *

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
root.mainloop()