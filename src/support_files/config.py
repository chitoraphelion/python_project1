from math import tan, atan, pi

# Конфигурация окна
WIDTH: int = 1200
HEIGHT: int = 800
BACKGROUND_COLOR: tuple[int, int, int] = (0, 0, 0)
LINE_COLOR: tuple[int, int, int] = (255, 255, 255)
FPS: int = 60

# Параметры камеры
HVA: float = tan((120 * (pi / 180)) / 2)
VVA: float = HVA * HEIGHT / WIDTH

HVA_angle: float = 120 * (pi / 180)
VVA_angle: float = 2 * atan(VVA)

NEAR: float = 0.1
FAR: float = 100.0
