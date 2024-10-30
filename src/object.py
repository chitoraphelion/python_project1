import numpy as np
from obj_loader import parse_obj
from transformations import rot_x, rot_y, rot_z
from typing import Tuple

class Object:
    def __init__(self, path: str, scale: float):
        """
        Инициализация объекта, загрузка .obj файла и установка начальных значений для позиции и скоростей.

        :param path: Путь к .obj файлу
        :param scale: Коэффициент масштабирования для модели
        """
        self.vertices, self.faces = parse_obj(path, scale)
        self.position: np.ndarray = np.array([0, 0, 0], dtype=float)
        self.rotation_speed: np.ndarray = np.array([0.01, 0.005, 0.001], dtype=float) * 0
        self.movement_speed: np.ndarray = np.array([0, 0, 0], dtype=float)

    def rotate(self) -> None:
        """
        Выполняет поворот объекта по осям X, Y и Z, используя матрицы поворота.
        """
        rotation_matrix: np.ndarray = (
            rot_x(self.rotation_speed[0]) @
            rot_y(self.rotation_speed[1]) @
            rot_z(self.rotation_speed[2])
        )

        self.vertices = self.vertices @ rotation_matrix.T
