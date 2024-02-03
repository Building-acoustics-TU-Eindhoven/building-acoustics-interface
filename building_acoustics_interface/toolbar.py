import pygame as pg
import pygame_gui

from receiverWindow import ReceiverWindow
from emittersWindow import EmitterWindow
class Toolbar:
    def __init__(self, manager, width, height):
       
        self.manager = manager
        self.main_WIDTH = width
        self.main_HEIGHT = height
        self.file_dialog_width = 600
        self.file_dialog_height = 500
        self.receiver_window = None
        self.emitter_window = None
        self.environment_settings = ["Ilaria", "Huiqing", "Someone else"]
        self.materials = ["wood", "metal", "earth"]
        self.graphs = ["one", "two", "three"]
        self.numerical = ["reverb", "decibel", "bang"]

        self.file_button = pygame_gui.elements.UIButton(pg.Rect((0, 0), (100, 50)), 
                                                        text='File', 
                                                        manager=self.manager) 
        
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
        
        self.button_emitters = pygame_gui.elements.UIButton(pg.Rect((500, 0), (100, 50)), 
                                                            text ="Emitters",
                                                            manager=self.manager)
        
        self.button_receivers = pygame_gui.elements.UIButton(pg.Rect((600, 0), (100, 50)), 
                                                        text='Receivers', 
                                                        manager=self.manager) 
        
        self.button_calculate = pygame_gui.elements.UIButton(pg.Rect((700, 0), (100, 50)), 
                                                        text='Calculate', 
                                                        manager=self.manager) 
        
    def create_file_dialog(self):
        self.file_dialog =  pygame_gui.windows.UIFileDialog(pg.Rect(((self.main_WIDTH / 2) - self.file_dialog_width / 2 , 
                                                            (self.main_HEIGHT / 2) - self.file_dialog_height / 2 ),
                                                        (self.file_dialog_width, self.file_dialog_height)),
                                                        manager=self.manager)
        return self.file_dialog
    
    def create_receiver_pos_window(self):
        self.receiver_window =  ReceiverWindow(self.manager, 650, 300, self.main_HEIGHT, self.main_WIDTH)
        return self.receiver_window
    
    def kill_receiver_pos_window(self):
        self.receiver_window.kill_window()
        self.receiver_window = None

    def create_emitter_window(self):
        self.emitter_window = EmitterWindow(self.manager, 650, 300, self.main_HEIGHT, self.main_WIDTH)
        return self.emitter_window

    def kill_emitter_window(self):
        self.emitter_window.kill_window()
        self.emitter_window = None