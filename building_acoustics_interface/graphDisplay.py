import pygame as pg
import pygame_gui

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


class GraphDisplay:
    def __init__(self, manager, height, width, pos_x, pos_y):
        self.manager = manager
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
       
    def updateDisplay(self, wanted_results, results):
        i = 1
        for name in wanted_results:
            preprocess_plt = results[name].figure
            processed_plt = self.processPlots(preprocess_plt)
            if i == 1:
                pygame_gui.elements.UIImage(pg.Rect((self.pos_x + 20, self.pos_y + 20), (250, 250)), 
                                            processed_plt,
                                            manager= self.manager)
            elif i == 2:
                pygame_gui.elements.UIImage(pg.Rect((self.pos_x + 290, self.pos_y + 20), (250, 250)), 
                                            processed_plt, 
                                            manager= self.manager)
            elif i == 3:
                pygame_gui.elements.UIImage(pg.Rect((self.pos_x + 20, self.pos_y + 290), (250, 250)), 
                                            processed_plt, 
                                            manager= self.manager)
            else:
                pygame_gui.elements.UIImage(pg.Rect((self.pos_x + 290, self.pos_y + 290), (250, 250)), 
                                            processed_plt, 
                                            manager= self.manager)
            i = i + 1
            

    def processPlots(self, fig):
        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        processed_plot = pg.image.fromstring(raw_data, size, "RGB")
        return processed_plot