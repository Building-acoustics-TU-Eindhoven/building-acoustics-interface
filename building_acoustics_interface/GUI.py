import pygame as pg
import pygame_gui

from renderer import *

class GUI:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 700
        self.FPS = 60
        self.window_surface = pg.display.set_mode(self.RES)
        self.manager = pygame_gui.UIManager(self.RES)
        self.renderer = SoftwareRender()
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=self.manager)    
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            time_delta = self.clock.tick(60)/1000.0
            self.renderer.draw()
            self.renderer.camera.control()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.hello_button:
                        print('Hello World!')

                self.manager.process_events(event)
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            self.manager.update(time_delta)
            self.window_surface.blit(self.renderer.background, (0, 100))
            self.manager.draw_ui(self.window_surface)

if __name__ == '__main__':
    app = GUI()
    app.run()