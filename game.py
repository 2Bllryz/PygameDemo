#调用库
import pygame
import sys
from pygame.locals import *
import random
import time



class Constant: #全局变量类
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600   #设置窗口大小

    FPS = 60    #设置图像的帧速率

    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)  #定义颜色

    SPEED = 5
    SCORE = 0   #初始化速度，分数

    font_big = pygame.font.SysFont("微软雅黑", 60)
    font_small = pygame.font.SysFont("Verdana", 20)
    game_over = font_big.render("出车祸啦！", True, BLACK)   #设置字体

class  Game:
    def __init__(self):

        pygame.init()
        SPEED_UP= pygame.USEREVENT + 1
        pygame.time.set_timer(SPEED_UP, 1000)
        clock = pygame.time.Clock()
        size = width,height = (Constant.SCREEN_WIDTH,Constant.SCREEN_HEIGHT)

        pygame.display.set_caption("躲避逆行")      #窗口名字
        screen = pygame.display.set_mode(size)    #窗口大小
        background = pygame.image.load("AnimatedStreet.png")     #加载背景
        pass
    def run(self):
        pygame.mixer.Sound("background.wav").play(-1)   #游戏一开始音乐开始循环
        while True:
            screen.blit(background, (0, 0))
            scores = Constant.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            screen.blit(scores, (10, 10))
class  Player:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < Constant.SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
class  Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()      #调用父类的__init__方法初始化对象
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,Constant.SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, Constant.SPEED)
        if (self.rect.bottom > Constant.SCREEN_HEIGHT):
            Constant.SPEED += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Constant.SCREEN_WIDTH - 40), 0)

clock = pygame.time.Clock()
pygame.init()




