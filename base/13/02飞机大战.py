import pygame
import time
from pygame.locals import *


class HeroPlane(object):
    def __init__(self):
        self.x = 160
        self.y = 470
        self.step = 10
        self.image = pygame.image.load('./feiji/hero/hero-0.png')

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def move_left(self):
        self.x -= self.step
    def move_right(self):
        self.x += self.step
    def move_up(self):
        self.y -= self.step
    def move_down(self):
        self.y += self.step
hero = HeroPlane()
def main():
    max_width = 320
    max_height = 568
    # 创建一个窗口,用来显示内容
    screen = pygame.display.set_mode((max_width, max_height), 0, 32)
    background = pygame.image.load('./feiji/bg.png')

    hero_width = 67
    hero_height = 82
    
    while True:
        # 舍得需要显示的背景图
        screen.blit(background, (0, 0))
        hero.display(screen)
        # 更新需要显示的内容
        pygame.display.update()
        bing_key(hero.x, hero.y)
        time.sleep(0.01)


def bing_key(x, y):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()

            if event.key == K_w or event.key == K_UP:
                print('up')
                hero.move_up()

            elif event.key == K_x or event.key == K_DOWN:
                print('down')
                hero.move_down()

            elif event.key == K_SPACE:
                print('space')
    return x, y


if __name__ == '__main__':
    main()
