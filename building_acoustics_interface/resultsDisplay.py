import pygame as pg
import pygame_gui

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg


class ResultDisplay:
    def __init__(self, manager, background):
        self.manager = manager
        self.surface = background
        self.my_font = pg.font.SysFont(None, 30)
        self.cell_height = 50
        self.cell_width = 150
    
    def updateTable(self, wanted_results, results):
        i = 0
        for wanted in wanted_results:
            red = (255, 0, 0)
            box = pg.Rect(800, 500 + i * self.cell_height, self.cell_width, self.cell_height) 
            text = self.my_font.render(wanted, True, red)
            pg.draw.rect(self.surface, pg.Color('black'), box, 2) 
            textRect = text.get_rect()
            textRect.center = box.center
            self.surface.blit(text, textRect)

            red = (255, 0, 0)
            box = pg.Rect(800 + self.cell_width, 500 + i * self.cell_height, self.cell_width, self.cell_height) 
            text = self.my_font.render(str(results.get(wanted)[0][0]), True, red)
            pg.draw.rect(self.surface, pg.Color('black'), box, 2) 
            textRect = text.get_rect()
            textRect.center = box.center
            self.surface.blit(text, textRect)
            i = i + 1