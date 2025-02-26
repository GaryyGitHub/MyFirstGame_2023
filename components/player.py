import pygame
import sys
sys.path.append(r"pythonProject")
import __main__

pygame.init()

class Player:
    def __init__(self, x, y):
        self.frames = [0] * 3 + [1] * 3 + [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3
        self.idx = 0
        self.images = __main__.IMAGES['player']
        self.image = self.images[self.frames[self.idx]]
        self.rect = self.image.get_rect()  # 帧所在的矩形
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

# velocity 速度
        self.x_vel = 0
        self.max_x_vel = 9
        self.y_vel = 15
        self.gravity = 2
        self.x_vel_after_left = -10
        self.x_vel_after_right = 10

class Youth:
    def __init__(self, x, y):
        self.frames = [0] * 2 + [1] * 2 + [2] * 2 + [3] * 2 + [4] * 2 + [5] * 2
        self.idx = 0
        self.images = __main__.IMAGES['youth']
        self.image = self.images[self.frames[self.idx]]
        self.rect = self.image.get_rect()  # 帧所在的矩形
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # velocity 速度
        self.x_vel = 0
        self.max_x_vel = 9
        self.y_vel = 18
        self.gravity = 2
        self.x_vel_after_left = -10
        self.x_vel_after_right = 10


class Adult:
    def __init__(self, x, y):
        self.frames = [0] * 3 + [1] * 3 + [2] * 3 + [3] * 3
        self.idx = 0
        self.images = __main__.IMAGES['adult']
        self.image = self.images[self.frames[self.idx]]
        self.rect = self.image.get_rect()  # 帧所在的矩形
        self.rect.x = x
        self.rect.y = y
        self.rect.left = x
        self.rect.right = x + 20
        self.rect.top = y
        self.rect.bottom = y + 32
        # velocity 速度
        self.x_vel = 0
        self.max_x_vel = 9
        self.y_vel = 16
        self.gravity = 2
        self.x_vel_after_left = -10
        self.x_vel_after_right = 10


class Old:
    def __init__(self, x, y):
        self.frames = [0] * 3 + [1] * 3 + [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3
        self.idx = 0
        self.images = __main__.IMAGES['old']
        self.image = self.images[self.frames[self.idx]]
        self.rect = self.image.get_rect()  # 帧所在的矩形
        self.rect.x = x
        self.rect.y = y
        self.rect.left = x
        self.rect.right = x + 20
        self.rect.top = y
        self.rect.bottom = y + 32
        # velocity 速度
        self.x_vel = 0
        self.max_x_vel = 9
        self.y_vel = 13
        self.gravity = 2.5
        self.x_vel_after_left = -10
        self.x_vel_after_right = 10

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel