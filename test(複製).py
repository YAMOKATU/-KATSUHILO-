#関数の定義
import pygame
import sys
import random
import math

# Pygameの初期化
pygame.init()

# 画面サイズとタイトルの設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("車ゲーム")

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# ゲームのフレームレート設定
clock = pygame.time.Clock()

class Car:
    def __init__(self):
        self.width = 30
        self.height = 60
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 2 * self.height
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#ゲームのアップデート
    def update(self):
        keys = pygame.key.get_pressed()#キーが押されているかの判断
#左右の矢印キーが押されたら右か左への判断プログラム       
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#壁の設定
class Wall:
    def __init__(self, x):
        self.width = 10
        self.height = 10
        self.x = x
        self.y = -self.height
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#ゲームのアップデート
    def update(self):
        self.y += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#HPのゲージ    
def create_HP():
    font = pygame.font.Font(None,20)
    text = font.render('HP',True,BLACK)
#HPゲージの色
    pygame.draw.rect(screen,BLACK,(50,50,200,15))
    pygame.draw.rect(screen,BLUE,(55,55,190,5))
    screen.blit(text,(50,30))

car = Car()
walls = []

def main():
    t = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))  #画面を白く塗りつぶす
        
        # ゲームの更新
        car.update()

        left = SCREEN_WIDTH / 3

        t += 1
        pre_left = left * math.sin((math.pi / 180) * t)
        wall_left, wall_right = Wall(pre_left), Wall(pre_left + SCREEN_WIDTH // 2)
        walls.append(wall_left)
        walls.append(wall_right)

        for wall in walls:
            wall.update()
            if wall.y >= SCREEN_HEIGHT:
                walls.remove(wall)
#衝突したことを知らせるプログラム
        for wall in walls:
            if car.rect.colliderect(wall.rect):
                print("衝突しました！")

        pygame.draw.rect(screen, BLACK, car.rect) #車の色

        for wall in walls:  #壁の色
            pygame.draw.rect(screen, BLACK, wall.rect)  

        create_HP()

        pygame.display.flip()
        clock.tick(60)  # FPSを60に設定

#ダメージ設定(未完成、未運用)
# class Player:
#     def __init__(self, hp):
#         self.hp = hp

#     def take_damage(self, damage):
#         self.hp -= damage
#         if self.hp < 0:
#             self.hp = 0  # HPがマイナスにならないようにする

#     def heal(self, amount):
#         self.hp += amount

# # プレイヤーのHPを100で初期化
# player = Player(100)

# # 何かにぶつかった時のダメージを設定
# damage_taken = 20

# # 何かにぶつかった場合、HPを減らす
# player.take_damage(damage_taken)

# # 現在のHPを表示
# print(f"現在のHP: {player.hp}")


if __name__ == "__main__":
    main()
