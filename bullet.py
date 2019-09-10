import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        # python2
        # super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen

        # 初始化子弹（矩形）
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)

        # 初始化子弹位置（相对于飞船的位置）
        self.rect.centerx = ship.img_rect.centerx
        self.rect.top = ship.img_rect.top

        # 子弹y坐标
        self.y = float(self.rect.y)

        # 初始化子弹颜色和速度
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        self.fire = False

    def moving(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)