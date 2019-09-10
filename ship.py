import pygame

class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.img_rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        self.img_rect.centerx = self.screen_rect.centerx
        self.img_rect.bottom = self.screen_rect.bottom

        self.center = float(self.img_rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def moving(self):
        if self.moving_right and self.img_rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.img_rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.img_rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.img_rect)
