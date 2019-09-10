import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''响应按下'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def update_ship(ship):
    ship.moving()


def update_bullets(bullets):
    for bullet in bullets.copy():
        bullet.moving()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_aliens_number_row(screen_height, alien_height, ship_height):
    available_space_row = screen_height - alien_height * 3 - ship_height
    aliens_number_row = int(available_space_row / (alien_height * 2))
    return aliens_number_row


def get_aliens_number_column(screen_width, alien_width):
    get_aliens_number_column = screen_width - alien_width * 2
    aliens_number_column = int(get_aliens_number_column / (alien_width * 2))
    return aliens_number_column


def create_alien(ai_settings, screen, aliens, aliens_number_row, aliens_number_column, aliens_number):
    column_id = 0
    row_id = 0
    for number in range(aliens_number):
        alien = Alien(screen, ai_settings)
        if column_id < aliens_number_column:
            column_id += 1
        else:
            column_id = 1
            row_id += 1
        # 取得外星人宽度
        alien_width = alien.img_rect.width
        alien.x = alien_width + (column_id - 1) * alien_width * 2
        alien.img_rect.x = alien.x
        # 取得外星人长度
        alien_height = alien.img_rect.height
        alien.y = alien_height + row_id * alien_height * 2
        alien.img_rect.y = alien.y
        # 加入队列
        aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(screen, ai_settings)
    aliens_number_row = get_aliens_number_row(ai_settings.screen_height, alien.img_rect.height, ship.img_rect.height)
    aliens_number_column = get_aliens_number_column(ai_settings.screen_width, alien.img_rect.width)
    aliens_number = aliens_number_row * aliens_number_column
    create_alien(ai_settings, screen, aliens, aliens_number_row, aliens_number_column, aliens_number)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    # 填充屏幕颜色
    screen.fill(ai_settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    for alien in aliens.sprites():
        alien.draw_alien()
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 最近绘制屏幕可见
    pygame.display.flip()

