import pygame

from object.object import Object
from camera.camera import Camera
from support_files.rendering import draw_object, pygame_coordinates
from support_files.config import *

# Инициализация Pygame и экрана
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.font.init()
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Инициализация камеры и объекта
scale = 1.0
camera = Camera(position=[-5.0, -5.0, 0.0])
object = Object('assets/guitar.obj', scale)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    object.rotate()

    keys = pygame.key.get_pressed()

    # Управление камерой (WASD для перемещения, QE для подъема/спуска)
    if keys[pygame.K_w]:
        camera.move(forward_back=1, left_right=0, up_down=0)
    if keys[pygame.K_s]:
        camera.move(forward_back=-1, left_right=0, up_down=0)
    if keys[pygame.K_a]:
        camera.move(forward_back=0, left_right=-1, up_down=0)
    if keys[pygame.K_d]:
        camera.move(forward_back=0, left_right=1, up_down=0)
    if keys[pygame.K_q]:
        camera.move(forward_back=0, left_right=0, up_down=-1)
    if keys[pygame.K_e]:
        camera.move(forward_back=0, left_right=0, up_down=1)

    # Управление поворотом камеры (стрелки)
    if keys[pygame.K_UP]:
        camera.rotate(up_down=-1, left_right=0)
    if keys[pygame.K_DOWN]:
        camera.rotate(up_down=1, left_right=0)
    if keys[pygame.K_LEFT]:
        camera.rotate(up_down=0, left_right=-1)
    if keys[pygame.K_RIGHT]:
        camera.rotate(up_down=0, left_right=1)

    # Отрисовка объекта
    x_pygame, y_pygame = pygame_coordinates(object.vertices, camera)
    draw_object(x_pygame, y_pygame, object.faces, screen)

    # Отображение FPS
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
