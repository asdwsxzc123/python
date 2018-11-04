# -*-encode=utf-8
import time
import random
import pygame
from pygame.locals import *

# 抽取基类


class BasePlane(object):
    def __init__(self, x, y, screen_temp, image_temp, step):
        self.screen = screen_temp
        self.step = step
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_temp)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)
    def destroy(self):
        pass

class HeroPlane(BasePlane):
    def __init__(self, x, y, screen_temp):
        BasePlane.__init__(self, x, y, screen_temp, './feiji/hero/hero-0.png',10)
        #  super.__init__(x,y,screen_temp)

    def move_left(self):
        self.x -= self.step

    def move_right(self):
        self.x += self.step

    def move_up(self):
        self.y -= self.step

    def move_down(self):
        self.y += self.step

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(BasePlane):
    """ 敌机的类 """

    def __init__(self, x, y, screen_temp):
        BasePlane.__init__(self, x, y, screen_temp,
                           './feiji/enemy/enemy-0.png', 2)
        self.width = 46
        self.height = 64
        self.direction = 'right'  # 存储子弹是否越界

    def move(self):
        if self.direction == 'right':
            self.x += self.step
        elif self.direction == 'left':
            self.x -= self.step
        if (320 - self.x - self.width < 0):
            self.direction = 'left'
        elif (self.x <= 0):
            self.direction = 'right'

        # self.y += self.step
    def fire(self):
        if random.randint(1, 100) == 8 or random.randint(1, 100) == 58:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Screen(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def setScreen(self):
        return pygame.display.set_mode((self.width, self.height), 0, 32)


class BaseBullet(object):
    def __init__(self, screen_temp, x, y, image_temp):
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_temp)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+30,
                            y - 10, './feiji/bullet.png')

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x+20,
                            y + 74, './feiji/bullet.png')

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 500:
            return True
        else:
            return False


def Key_bind(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('quit')
            exit()
        # keydown
        if event.type == 2:
            print(event.key)
            if event.key == 276:
                print('left')
                hero_temp.move_left()
            elif event.key == 275:
                print('right')
                hero_temp.move_right()
            elif event.key == 273:
                print('up')
                hero_temp.move_up()
            elif event.key == 274:
                print('DOWN')
                hero_temp.move_down()
            elif event.key == 32:
                print('space')
                hero_temp.fire()
            elif event.key == 98:
                print('destroy')
                hero_temp.detroy()
            elif event.key == 99:
                print('exit')
                exit()


def main():
    screen = Screen(320, 568).setScreen()
    background = pygame.image.load('./feiji/bg.png')
    hero = HeroPlane(160, 470, screen)
    enemy = EnemyPlane(160, 0, screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        Key_bind(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
