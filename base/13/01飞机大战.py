import pygame
import time
from pygame.locals import *


def main():
    max_width = 320
    max_height = 568
    # 创建一个窗口,用来显示内容
    screen = pygame.display.set_mode((max_width, max_height), 0, 32)
    # screen = pygame.display.set_mode((480,852),0,32)
    # 创建一个和窗口大小的图片,,用来充当背景图
    background = pygame.image.load('./feiji/bg.png')

    hero = pygame.image.load('./feiji/hero/hero-0.png')
    # 吧背景图片放在窗口中显示
    x = 160
    y = 470
    hero_width = 67
    hero_height = 82
    while True:
        # 舍得需要显示的背景图
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        # 更新需要显示的内容
        pygame.display.update()
        (x, y) = bing_key(x, y)
        # print(x,y)
        # x -= 1

        # if x >= (max_width - hero_width):
        #   x -=1
        # elif x <= 0:
        #   x +=1

        time.sleep(0.01)


def bing_key(x, y):
    step = 10
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                x -= step
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                x += step

            if event.key == K_w or event.key == K_UP:
                print('up')
                y -= step

            elif event.key == K_x or event.key == K_DOWN:
                print('down')
                y += step

            elif event.key == K_SPACE:
                print('space')


if __name__ == '__main__':
    main()
