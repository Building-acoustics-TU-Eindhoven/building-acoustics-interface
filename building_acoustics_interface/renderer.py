from object_3d import *
from camera import *
from projection import *
import pygame as pg
import pygame_gui


class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1200, 700
        self.H_WIDTH, self.H_HEIGHT = 800 // 2, 600 // 2
        self.FPS = 60
        self.window_surface = pg.display.set_mode(self.RES)
        self.background = pg.Surface((800, 600))
        self.manager = pygame_gui.UIManager(self.RES)

        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pg.Rect((350, 275), (100, 50)),
                                             text='Say Hello',
                                             manager=self.manager)

        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.get_object_from_file(r"C:\Users\20212466\OneDrive - TU Eindhoven\Documents\uni dingen\Year 3\student jobs Y3\accoustic ui project\UI repo\building-acoustics-interface\building_acoustics_interface\resources\tank.obj")

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.background.fill(pg.Color('darkslategray'))
        self.object.draw()

    def run(self):
        while True:
            time_delta = self.clock.tick(60)/1000.0
            self.draw()
            self.camera.control()
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
            self.window_surface.blit(self.background, (0, 100))
            self.manager.draw_ui(self.window_surface)



if __name__ == '__main__':
    app = SoftwareRender()
    app.run()