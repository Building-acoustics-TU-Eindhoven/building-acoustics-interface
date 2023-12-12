from tkinter import *
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)



class graphDisplay:
    def __init__(self, root):
        screenWidth = root.winfo_screenwidth()
        width = 7
        height = 4
        fig = getFig(width, height)
            
        frame = LabelFrame(root, text="Graph results")
        frame.place(x=screenWidth - width * 100, y=0)
       
        canvas = FigureCanvasTkAgg(fig, master=frame)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)


def getFig(width, height):
    #example plot
    plt.rcParams['figure.figsize'] = [width,height]
    fig = Figure()
    t = np.arange(0, 3, .01)
    ax = fig.add_subplot()
    ax.plot(t, 2 * np.sin(2 * np.pi * t))
    ax.set_xlabel("time [s]")
    ax.set_ylabel("f(t)")
    return fig