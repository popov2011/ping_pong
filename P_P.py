
from pygame import *
from random import randint
from time import time as timer  

font.init()
font1 = font.Font(None, 36)
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
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed 
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed
     
            
player1 = Player('tennis_racket copy_left.png', 2, 400, 60, 85, 10)
player2 = Player('tennis_racket_right.png', 640, 400, 60, 85, 10)
ball = GameSprite('tennis_ball.png', 350, 250, 40, 40, 5)

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(bg, (0, 0))
    player2.update_l()
    player1.update_r()
    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)
