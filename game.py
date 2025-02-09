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
        pass
class  Player:
class  Enemy:

FramePerSec = pygame.time.Clock()
pygame.init()




