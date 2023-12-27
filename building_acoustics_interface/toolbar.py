import pygame as pg
import pygame_gui

class Toolbar:
    def __init__(self, manager, width, height):
       
        self.manager = manager
        self.WIDTH = width
        self.HEIGHT = height
        self.environment_settings = ["Ilaria", "Huiqing", "Someone else"]
        self.materials = ["wood", "metal", "earth"]
        self.graphs = ["one", "two", "three"]
        self.numerical = ["reverb", "decibel", "bang"]
        self.emitters = ["10", "10", "10"]
        self.receivers = ["0", "0", "0"]

        self.file_button = pygame_gui.elements.UIButton(pg.Rect((0, 0), (100, 50)), 
                                                        text='File', 
                                                        manager=self.manager)    
        self.file_dialog = pygame_gui.windows.UIFileDialog(pg.Rect((0,0), (400, 300)), 
                                                           manager=self.manager, 
                                                           visible=False)
        
        self.environment_menu = pygame_gui.elements.UIDropDownMenu(self.environment_settings, 
                                                            self.environment_settings[0], 
                                                            pg.Rect((100, 0), (100, 50)), 
                                                            manager=self.manager)
        self.materials_menu = pygame_gui.elements.UIDropDownMenu(self.materials, 
                                                            self.materials[0], 
                                                            pg.Rect((200, 0), (100, 50)), 
                                                            manager=self.manager)
        self.graph_results_menu = pygame_gui.elements.UIDropDownMenu(self.graphs, 
                                                            self.graphs[0], 
                                                            pg.Rect((300, 0), (100, 50)), 
                                                            manager=self.manager)
        self.numbers_result_menu = pygame_gui.elements.UIDropDownMenu(self.numerical, 
                                                            self.numerical[0], 
                                                            pg.Rect((400, 0), (100, 50)), 
                                                            manager=self.manager)
        self.pos_emitters = pygame_gui.elements.UIDropDownMenu(self.emitters, 
                                                            self.emitters[0], 
                                                            pg.Rect((500, 0), (100, 50)), 
                                                            manager=self.manager)
        self.pos_receivers = pygame_gui.elements.UIDropDownMenu(self.receivers, 
                                                            self.receivers[0], 
                                                            pg.Rect((600, 0), (100, 50)), 
                                                            manager=self.manager)

        #self.text_line = pygame_gui.elements.UITextEntryLine(pg.Rect((700, 200), (100, 50)), manager=self.manager)
        #self.selection = pygame_gui.elements.UISelectionList(pg.Rect((1000, 100), (100, 50)), names, manager=self.manager)