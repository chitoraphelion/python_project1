import numpy as np
from transformations import rot_x, rot_y, rot_z
from config import HVA, VVA
from typing import Union

class Camera:
    def __init__(self, position: Union[list[float], np.ndarray], rotation_speed: float = 0.01,
                 movement_speed: float = 0.1, local_HVA: float = HVA, local_VVA: float = VVA):
        """
        Инициализация камеры с начальной позицией, скоростями и углами обзора.

        :param position: Начальная позиция камеры в пространстве
        :param rotation_speed: Скорость вращения камеры
        :param movement_speed: Скорость перемещения камеры
        :param local_HVA: Горизонтальный угол обзора камеры
        :param local_VVA: Вертикальный угол обзора камеры
        """
        self.rotation_speed = rotation_speed
        self.movement_speed = movement_speed
        self.HVA = local_HVA
        self.VVA = local_VVA
        self.position = np.array(position, dtype=np.float64)
        self.ort_j = np.array(-self.position / np.linalg.norm(self.position))
        self.ort_k = np.array([0, 0, 1], dtype=np.float64)
        self.ort_i = np.cross(self.ort_k, self.ort_j)

    def rotate(self, up_down: float, left_right: float) -> None:
        """
        Вращает камеру на основе указанных углов по вертикали и горизонтали.

        :param up_down: Угол вращения вверх-вниз
        :param left_right: Угол вращения влево-вправо
        """
        rotation_matrix = (
            rot_y(up_down * self.rotation_speed) @
            rot_z(left_right * self.rotation_speed)
        )

        self.ort_i = rotation_matrix @ self.ort_i
        self.ort_j = rotation_matrix @ self.ort_j
        self.ort_k = rotation_matrix @ self.ort_k

    def move(self, forward_back: float, left_right: float, up_down: float) -> None:
        """
        Перемещает камеру в пространстве по трём осям.

        :param forward_back: Перемещение вперёд-назад
        :param left_right: Перемещение влево-вправо
        :param up_down: Перемещение вверх-вниз
        """
        self.position += self.ort_j * forward_back * self.movement_speed
        self.position += self.ort_i * left_right * self.movement_speed
        self.position += self.ort_k * up_down * self.movement_speed
