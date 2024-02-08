from camera import *
from projection import *
from fileParser import *
import pygame as pg

class SoftwareRender:
    def __init__(self, drawing_surface, file_path):
        self.WIDTH, self.HEIGHT = 800, 600 
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.drawing_surface = drawing_surface
        self.file_path = file_path
        self.receivers = []
        self.emitters = []
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = FileParser(self, self.file_path).object

    def draw(self):
        self.drawing_surface.fill(pg.Color('white'))
        self.object.draw()