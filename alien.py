import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.img_rect = self.image.get_rect()

        self.img_rect.x = self.img_rect.width
        self.img_rect.y = self.img_rect.height

        self.x = float(self.img_rect.x)
        self.y = float(self.img_rect.y)

    def draw_alien(self):
        self.screen.blit(self.image, self.img_rect)
