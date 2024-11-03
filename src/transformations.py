import numpy as np
from math import sin, cos

def rot_x(angle: float) -> np.ndarray:
    """
    Возвращает матрицу поворота вокруг оси X.

    :param angle: Угол поворота в радианах
    :return: Матрица поворота 3x3
    """
    c, s = cos(angle), sin(angle)
    return np.array([[1, 0, 0],
                     [0, c, -s],
                     [0, s, c]], dtype=float)

def rot_y(angle: float) -> np.ndarray:
    """
    Возвращает матрицу поворота вокруг оси Y.

    :param angle: Угол поворота в радианах
    :return: Матрица поворота 3x3
    """
    c, s = cos(angle), sin(angle)
    return np.array([[c, 0, s],
                     [0, 1, 0],
                     [-s, 0, c]], dtype=float)

def rot_z(angle: float) -> np.ndarray:
    """
    Возвращает матрицу поворота вокруг оси Z.

    :param angle: Угол поворота в радианах
    :return: Матрица поворота 3x3
    """
    c, s = cos(angle), sin(angle)
    return np.array([[c, -s, 0],
                     [s, c, 0],
                     [0, 0, 1]], dtype=float)
