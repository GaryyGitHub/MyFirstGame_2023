import pygame
import sys
sys.path.append(r"pythonProject")
import __main__


class BrickLong(pygame.sprite.Sprite):
    def __init__(self, x, y):  # 矩形的四个参数
        pygame.sprite.Sprite.__init__(self)
        self.image = __main__.IMAGES['brick2']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
