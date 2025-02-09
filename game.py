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

class  Game:
    def __init__(self):

        pygame.init()
        self.SPEED_UP= pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPEED_UP, 1000)
        self.clock = pygame.time.Clock()
        size = width,height = (Constant.SCREEN_WIDTH,Constant.SCREEN_HEIGHT)    #窗口大小

        pygame.display.set_caption("躲避逆行")      #窗口名字
        self.screen = pygame.display.set_mode(size)    #渲染窗口
        self.font_big = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.game_over = self.font_big.render("Damnnnn!", True, Constant.BLACK)  # 设置字体
        self.background = pygame.image.load("AnimatedStreet.png")     #加载背景





    def run(self):
        player = Player()
        enemy = Enemy()  # 定义玩家对象

        enemies = pygame.sprite.Group()
        enemies.add(enemy)  # 定义敌人精灵组

        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(enemy)  # 将所有精灵放到一个组中
        pygame.mixer.Sound("background.wav").play(-1)   #游戏一开始音乐开始循环
        while True:

            self.screen.blit(self.background, (0, 0))
            scores = self.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            self.screen.blit(scores, (10, 10))
            for entity in all_sprites:      #对所有实体使用move方法移动，图像绘制
                entity.move()
                self.screen.blit(entity.image, entity.rect)
            for event in pygame.event.get():
                if event.type == self.SPEED_UP:
                    Constant.SPEED+=0.5
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if pygame.sprite.spritecollideany(player, enemies):
                pygame.mixer.Sound('crash.wav').play()      #撞击声
                time.sleep(1)   #背景音乐延迟一秒

                self.screen.fill(Constant.RED)
                self.screen.blit(self.game_over, (30, 250))     #显示游戏结束
                scores = self.font_big.render(str(Constant.SCORE), True, Constant.YELLOW)
                self.screen.blit(scores, (165, 350))
                pygame.display.update()         #刷新
                for entity in all_sprites:
                    entity.kill()                #删除敌人
                time.sleep(2)
                pygame.quit()
                sys.exit()
            pygame.display.update()
            self.clock.tick(Constant.FPS)

class  Player(pygame.sprite.Sprite):
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
            Constant.SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Constant.SCREEN_WIDTH - 40), 0)

if __name__ == '__main__':
    game = Game()
    game.run()






