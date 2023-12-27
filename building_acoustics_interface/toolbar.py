import pygame as pg
import pygame_gui

names = "whatsuppp"

class Toolbar:
    def __init__(self, manager, width, height):
        self.manager = manager
        self.WIDTH = width
        self.HEIGHT = height
        self.file_button = pygame_gui.elements.UIButton(pg.Rect((0, 0), (100, 50)), text='File', manager=self.manager)    
        self.file_dialog = pygame_gui.windows.UIFileDialog(pg.Rect((0,0), (400, 300)), manager=self.manager, visible=False)
        
        #self.drop_down = pygame_gui.elements.UIDropDownMenu(["one", "two"], "one", pg.Rect((800, 200), (100, 50)) ,manager=self.manager)
        #self.text_line = pygame_gui.elements.UITextEntryLine(pg.Rect((700, 200), (100, 50)), manager=self.manager)
        #self.selection = pygame_gui.elements.UISelectionList(pg.Rect((1000, 100), (100, 50)), names, manager=self.manager)