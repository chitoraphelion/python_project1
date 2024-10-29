from math import tan, atan, pi

#Конфигурация окна
WIDTH = 1200
HEIGHT = 800
BACKGROUND_COLOR = (0, 0, 0)
LINE_COLOR = (255, 255, 255)
FPS = 60

#Параметры камеры
HVA = tan((120 * (pi / 180)) / 2)
VVA = HVA * HEIGHT / WIDTH

HVA_angle = 120 * (pi / 180)
VVA_angle = 2 * atan(VVA)

NEAR = .1
FAR = 100
