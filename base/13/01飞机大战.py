import pygame
import time
def main():
  # 创建一个窗口,用来显示内容
  screen = pygame.display.set_mode((320,568),0,32)
  # screen = pygame.display.set_mode((480,852),0,32)
  # 创建一个和窗口大小的图片,,用来充当背景图
  background = pygame.image.load('./feiji/background.png')
  
  # 吧背景图片放在窗口中显示
  while True:
    # 舍得需要显示的背景图
    screen.blit(background,(0,0))

    # 更新需要显示的内容
    pygame.display.update()

    time.sleep(0.01)

if __name__ == '__main__':
  main()