import pygame as pg
import pygame_gui

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


class GraphDisplay:
    def __init__(self, manager):
        self.manager = manager
        self.getPlots()
        self.processPlots(self.fig)
        self.graph = pygame_gui.elements.UIImage(pg.Rect((800, 0), (300, 300)), self.processed_plot, manager= self.manager)

    def processPlots(self, plot):
        canvas = agg.FigureCanvasAgg(plot)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        self.processed_plot = pg.image.fromstring(raw_data, size, "RGB")
    
    def getPlots(self):
        self.fig = plt.figure(figsize=[4, 4], # Inches
                   dpi=100,        # 100 dots per inch, so the resulting buffer is 400x400 pixels
                   )
        ax = self.fig.gca()
        ax.plot([1, 2, 4])
    
