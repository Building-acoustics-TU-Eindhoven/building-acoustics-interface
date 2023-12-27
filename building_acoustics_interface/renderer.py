from object_3d import *
from camera import *
from projection import *
import pygame as pg

class SoftwareRender:
    def __init__(self, drawing_surface, file_path):
        self.WIDTH, self.HEIGHT = 800, 600 
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.drawing_surface = drawing_surface
        self.file_path = file_path
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.get_object_from_file(self.file_path)

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
        self.drawing_surface.fill(pg.Color('white'))
        self.object.draw()