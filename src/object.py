import numpy as np
from obj_loader import parse_obj
from transformations import rot_x, rot_y, rot_z

class Object:
    def __init__(self, path, scale):
        self.vertices, self.faces = parse_obj(path, scale)
        self.position = np.array([0, 0, 0])
        self.rotation_speed = np.array([.01, 0.005, 0.001]) * 0
        self.movement_speed = np.array([0, 0, 0])

    def rotate(self):
        rotation_matrix = (
            rot_x(self.rotation_speed[0]) @
            rot_y(self.rotation_speed[1]) @
            rot_z(self.rotation_speed[2])
        )

        self.vertices = self.vertices @ rotation_matrix.T
