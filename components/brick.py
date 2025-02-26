import pygame
import sys
sys.path.append(r"pythonProject")
import __main__


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y):  # 矩形的四个参数
        super().__init__()
        # pygame.sprite.Sprite.__init__(self)
        self.image = __main__.IMAGES['brick1']
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_left(self):
        return self.rect.left

    def update_right(self):
        return self.rect.right

    def update_top(self):
        return self.rect.top

    def update_bottom(self):
        return self.rect.bottom