
from pygame import *
from random import randint
from time import time as timer  

font.init()
font1 = font.SysFont('Times New Roman', 35)
lose1 = font1.render(
    'PLAYER ' + input('Введите имя пользователя:') + ' LOSE', True, (238, 210, 2)
)
lose2 = font1.render(
    'PLAYER ' + input('Введите имя пользователя:') + ' LOSE', True, (238, 210, 2)
)
w = 700
h = 500
window = display.set_mode((w, h))
display.set_caption('Ping-Pong')
bg = transform.scale(image.load('table.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
     
            
player1 = Player('tennis_racket copy_left.png', 2, 400, 60, 85, 10)
player2 = Player('tennis_racket_right.png', 640, 400, 60, 85, 10)
ball = GameSprite('tennis_ball.png', 350, 250, 40, 40, 7)

clock = time.Clock()
FPS = 60
game = True
finish = False

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg, (0, 0))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > h - 40 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True 
        window.blit(lose1, (200, 200))
    if ball.rect.x > 650:
        finish = True 
        window.blit(lose2, (200, 200))
    
    player2.update_l()
    player1.update_r()
    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
