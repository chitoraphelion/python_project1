import numpy as np
import pygame

from camera import Camera
from object import Object
from config import *
from typing import Tuple

def relative_coordinates(vertice: np.ndarray, camera: Camera) -> np.ndarray:
    """
    Преобразует координаты вершины в относительные координаты по отношению к камере.

    :param vertice: Глобальные координаты вершины
    :param camera: Камера с позицией и ориентацией
    :return: Координаты вершины относительно камеры
    """
    vertice = -vertice - camera.position
    to_rel_coord_matrix = np.transpose(np.array([camera.ort_i, camera.ort_j, camera.ort_k]))
    return np.dot(vertice, to_rel_coord_matrix)

def pygame_coordinates(vertices: np.ndarray, camera: Camera,
                       local_HVA: float = HVA, local_VVA: float = VVA) -> Tuple[np.ndarray, np.ndarray]:
    """
    Преобразует вершины в координаты для отображения в Pygame.

    :param vertices: Массив вершин объекта
    :param camera: Камера с позиции и ориентацией
    :param local_HVA: Горизонтальный угол зрения
    :param local_VVA: Вертикальный угол зрения
    :return: Кортеж из двух массивов с координатами x и y для Pygame
    """
    number_of_vertices = len(vertices)
    x_pygame = np.zeros(number_of_vertices, dtype=int)
    y_pygame = np.zeros(number_of_vertices, dtype=int)

    for i in range(number_of_vertices):
        vertice_global = vertices[i]
        vertice = relative_coordinates(vertice_global, camera)

        if NEAR < vertice[1] < FAR:
            x = vertice[0] / vertice[1]
            y = vertice[2] / vertice[1]

            if abs(x) < local_HVA and abs(y) < local_VVA:
                x_pygame[i] = int((x + 0.5) * WIDTH)
                y_pygame[i] = int((-y + 0.5) * HEIGHT)

    return x_pygame, y_pygame

def draw_object(x_pygame: np.ndarray, y_pygame: np.ndarray,
                faces: np.ndarray, surface: pygame.Surface) -> None:
    """
    Рисует объект на экране на основе его вершин и граней.

    :param x_pygame: Массив x координат вершин для Pygame
    :param y_pygame: Массив y координат вершин для Pygame
    :param faces: Массив граней объекта, каждая из которых содержит индексы вершин
    :param surface: Поверхность Pygame для рисования
    """
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
