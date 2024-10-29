import numpy as np
from math import sin, cos

def rot_x(angle):
    c, s = cos(angle), sin(angle)
    return np.array([[1, 0, 0],
                     [0, c, -s],
                     [0, s, c]])

def rot_y(angle):
    c, s = cos(angle), sin(angle)
    return np.array([[c, 0, s],
                     [0, 1, 0],
                     [-s, 0, c]])

def rot_z(angle):
    c, s = cos(angle), sin(angle)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]])
