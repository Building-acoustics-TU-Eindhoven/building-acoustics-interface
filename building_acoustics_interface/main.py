from tkinter import *

# root window
root = Tk()
root.title('Acoustic UI')
screenHeight = root.winfo_screenheight()
screenWidth = root.winfo_screenwidth()
root.geometry("{}x{}+0+0".format(screenWidth, screenHeight))
root.state('zoomed')
root.mainloop()