import pygame as pg
import pygame_gui
from pygame.locals import *

from renderer import *
from toolbar import *
from graphDisplay import *
from resultsDisplay import *
from FVM import *


class GUI:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 700
        self.FPS = 60
        self.window_surface = pg.display.set_mode(self.RES, DOUBLEBUF)
        self.manager = pygame_gui.UIManager(self.RES)
        self.background_surface = pg.Surface((self.WIDTH, self.HEIGHT))
        self.background_surface.fill(pg.Color('darkgrey'))

        self.toolbar = Toolbar(self.manager, self.WIDTH, self.HEIGHT)
        self.graph_display = GraphDisplay(self.manager, 600, 650, 600, 50)
        self.render_surface = pg.Surface((600, 650))
        self.render_surface.fill(pg.Color('darkgrey'))
        #self.num_display = ResultDisplay(self.manager, self.background_surface)
        self.calculator = FVM()
        self.clock = pg.time.Clock()
        self.rendering = False

        self.receivers = []
        self.emitters = []
        self.abs_coeff = []
        self.file = ""

    def run(self):
        while True:
            time_delta = self.clock.tick(60)/1000.0
            if self.rendering:
                self.renderer.emitters = self.emitters
                self.renderer.receivers = self.receivers
                self.renderer.draw()
                self.renderer.camera.control()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.toolbar.file_button:
                        self.toolbar.create_file_dialog()
                    elif event.ui_element == self.toolbar.button_receivers:
                        self.toolbar.create_receiver_pos_window()
                    elif self.toolbar.receiver_window != None:
                        if event.ui_element == self.toolbar.receiver_window.save_pos_receiver_button:
                            self.receivers.append(self.toolbar.receiver_window.get_saved_pos() + [1])
                            self.toolbar.kill_receiver_pos_window()
                    elif event.ui_element == self.toolbar.button_emitters:
                         self.toolbar.create_emitter_window()
                    elif self.toolbar.emitter_window != None:
                        if event.ui_element == self.toolbar.emitter_window.save_pos_emitter_button:
                            self.emitters.append(self.toolbar.emitter_window.get_saved_pos() + [1])
                            self.toolbar.kill_emitter_window()
                    elif event.ui_element == self.toolbar.button_calculate:
                        if (self.emitters and self.receivers and self.abs_coeff):
                            self.calculator.start(self.emitters, self.receivers, self.abs_coeff, self.file)
                            self.graph_display.updateDisplay(["decay SPL", "Normalized decay SPL", "Energy density", "Schroeder decay"], self.calculator.get_results())
                        else:
                            print("not inputted receiver, emitter or absorbtion coeffficient")
                    elif event.ui_element == self.toolbar.button_absorb_coeff:
                        self.toolbar.create_absorb_coeff_window()
                    elif self.toolbar.abs_coeff_window != None:
                        if event.ui_element == self.toolbar.abs_coeff_window.save_abs_coeff_button:
                            self.abs_coeff = self.toolbar.abs_coeff_window.get_saved_coeff()
                            self.toolbar.kill_abs_coeff_window()

                if event.type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                    if event.ui_element == self.toolbar.file_dialog:
                        self.file = event.text
                        self.renderer = SoftwareRender(self.render_surface, self.file)
                        self.rendering = True

                self.manager.process_events(event)
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            self.manager.update(time_delta)
            self.window_surface.blit(self.background_surface, (0, 0))
            self.window_surface.blit(self.render_surface, (0, 100))
            self.manager.draw_ui(self.window_surface)

if __name__ == '__main__':
    app = GUI()
    app.run()