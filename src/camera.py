import numpy as np
from transformations import rot_x, rot_y, rot_z
from config import HVA, VVA

class Camera:
    def __init__(self, position, rotation_speed = 0.01, movement_speed = .1, local_HVA = HVA, local_VVA = VVA):
        self.rotation_speed = rotation_speed
        self.movement_speed = movement_speed
        self.HVA = local_HVA
        self.VVA = local_VVA
        self.position = np.array(position, dtype=np.float64)
        self.ort_j = np.array(- self.position / np.linalg.norm(self.position))
        self.ort_k = np.array([0, 0, 1], dtype=np.float64)
        self.ort_i = np.cross(self.ort_k, self.ort_j)

    def rotate(self, up_down, left_right):
        rotation_matrix = (
            rot_y(up_down * self.rotation_speed) @
            rot_z(left_right * self.rotation_speed)
        )

        self.ort_i = rotation_matrix @ self.ort_i
        self.ort_j = rotation_matrix @ self.ort_j
        self.ort_k = rotation_matrix @ self.ort_k

    def move(self, forward_back, left_right, up_down):
        self.position += self.ort_j * forward_back * self.movement_speed
        self.position += self.ort_i * left_right * self.movement_speed
        self.position += self.ort_k * up_down * self.movement_speed
