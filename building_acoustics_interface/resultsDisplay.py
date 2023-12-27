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
        self.wanted_results = ["reverb", "decibel", "goodness"]
        self.my_font = pg.font.SysFont(None, 30)
        self.cell_height = 50
        self.cell_width = 150
        self.getResults()
        self.createTable()
        #self.table = pygame_gui.elements.UIImage(pg.Rect((800, 500), (150, 50)), self.text_surface, manager= self.manager)
        

    def getResults(self):
        self.results = ["s", "s", "s"]
    
    def createTable(self):
        i = 0
        for wanted in self.wanted_results:
            red = (255, 0, 0)
            box = pg.Rect(800, 500 + i * self.cell_height, self.cell_width, self.cell_height) 
            text = self.my_font.render(wanted, True, red)
            pg.draw.rect(self.surface, pg.Color('black'), box, 2) 
            textRect = text.get_rect()
            textRect.center = box.center
            self.surface.blit(text, textRect)

            red = (255, 0, 0)
            box = pg.Rect(800 + self.cell_width, 500 + i * self.cell_height, self.cell_width, self.cell_height) 
            text = self.my_font.render(self.results[i], True, red)
            pg.draw.rect(self.surface, pg.Color('black'), box, 2) 
            textRect = text.get_rect()
            textRect.center = box.center
            self.surface.blit(text, textRect)
            i = i + 1
        
        #self.text_surface = self.my_font.render(self.results[0], True, (0, 0, 0))