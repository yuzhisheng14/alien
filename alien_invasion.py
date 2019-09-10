import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # 初始化背景
    pygame.init()
    # 设置窗口标题
    pygame.display.set_caption("Alien Invasion")
    # 加载窗口设置
    ai_settings = Settings()
    # 设置窗口尺寸
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 创建飞船
    ship = Ship(screen, ai_settings)
    # 创建子弹编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()
    # 创建外星人
    gf.create_fleet(ai_settings, screen, aliens, ship)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_ship(ship)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)

run_game()