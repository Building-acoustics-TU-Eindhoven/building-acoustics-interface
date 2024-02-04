import pygame as pg
import pygame_gui

class AbsCoeffWindow:
    def __init__(self, manager, width, height, parent_heigth, parent_width):
        self.manager = manager
        self.parent_heigth = parent_heigth
        self.parent_width = parent_width
        self.width = width
        self.height = height
        self.window = self.create_window()

    def create_window(self):
        window_orientation = pg.Rect(((self.parent_width / 2) - self.width / 2, (self.parent_heigth / 2) - self.height / 2), (self.width, self.height))
        window = pygame_gui.elements.UIWindow(window_orientation, 
                                              manager=self.manager, 
                                              window_display_title="Absorbtion coefficient settings")
        self.add_labels(window)
        self.add_textboxes(window)
        self.add_buttons(window)
        return window

    def add_labels(self, window):
        pygame_gui.elements.UILabel(pg.Rect((50, 100), (200, 50)), 
                                    text="Absorbtion Coefficients: ",
                                    container = window.get_container(),
                                    manager=self.manager)
    
    def add_textboxes(self, window):
        self.textbox = pygame_gui.elements.UITextEntryLine(pg.Rect((275, 100), (250, 50)),
                                            manager=self.manager,
                                            container=window.get_container())
    
    def add_buttons(self, window):
        self.save_abs_coeff_button = pygame_gui.elements.UIButton(pg.Rect((500, 190), (100, 50)), 
                                                        text='Save', 
                                                        manager=self.manager,
                                                        container=window.get_container()) 
    
    def get_saved_coeff(self):
        return self.textbox.get_text().split(",")
        
    def kill_window(self):
        self.window.kill()

   