import numpy as np
import pygame
from math import tan

from camera import Camera
from object import Object
from config import *


def relative_coordinates(vertice, camera):
    vertice = -vertice - camera.position
    to_rel_coord_matrix = np.transpose(np.array([camera.ort_i, camera.ort_j, camera.ort_k]))

    return np.dot(vertice, to_rel_coord_matrix)

def pygame_coordinates(vertices, camera, local_HVA=HVA, local_VVA=VVA):
    number_of_vertices = len(vertices)
    x_pygame = np.zeros(number_of_vertices, dtype=int)
    y_pygame = np.zeros(number_of_vertices, dtype=int)

    for i in range(number_of_vertices):
        vertice_global = vertices[i]
        vertice = relative_coordinates(vertice_global, camera)

        if NEAR < vertice[1] < FAR:
            x = vertice[0] / vertice[1]
            y = vertice[2] / vertice[1]

            if abs(x) < HVA and abs(y) < VVA:
                x_pygame[i] = int((x + 0.5) * WIDTH)
                y_pygame[i] = int((-y + 0.5) * WIDTH)

    return x_pygame, y_pygame

def draw_object(x_pygame, y_pygame, faces, surface):
    for face in faces:

        v0 = (x_pygame[int(face[0])], y_pygame[int(face[0])])
        v1 = (x_pygame[int(face[1])], y_pygame[int(face[1])])
        v2 = (x_pygame[int(face[2])], y_pygame[int(face[2])])

        if v0 != (0, 0) and v1 != (0, 0):
            pygame.draw.line(surface, LINE_COLOR, v0, v1, width=1)
        if v0 != (0, 0) and v2 != (0, 0):
            pygame.draw.line(surface, LINE_COLOR, v0, v2, width=1)
        if v1 != (0, 0) and v2 != (0, 0):
            pygame.draw.line(surface, LINE_COLOR, v1, v2, width=1)
