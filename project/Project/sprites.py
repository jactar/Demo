# sprite classes for game

import pygame as pg
from pygame.sprite import Sprite
import random
from settings import *
from time import sleep

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((17,73))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*11/12, HEIGHT/2)
        self.vx = 0
        self.vy = 0
        self.falling = False
        self.max_velocity = -25
        self.up = pg.K_UP
        self.down = pg.K_DOWN
    def wall1_collision(self):
        if self.rect.y >= HEIGHT - 5 or self.rect.y <= 5:
            self.vy = -self.vy

    def update(self):
        self.vy = 0
        self.vx = 0
        # self.gravity()
        keys = pg.key.get_pressed()
        if keys[self.up]:
            self.vy = -7.5
        if keys[self.down]:
            self.vy = 7.5
        self.wall1_collision
        # if keys[pg.K_UP] and self.falling == False:
        #     self.jump()  

        # self.rect.x += self.vx
        self.rect.y += self.vy
    def gravity(self):
        if self.rect.x < HEIGHT-40:
            self.falling = True
            self.vx -= 10
        elif self.rect.x >= HEIGHT: 
            self.falling = False
            self.vx = 120
            self.rect.x = HEIGHT-10


    # def borders(self):
    #     if self.rect.x == WIDTH:
    #         self.vx = 0
    def jump(self):
        self.vx = -85
    
class Object(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((5,HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*6/12, HEIGHT/2)

class Ball(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((10,10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.falling = False
        self.velocity = VELOCITY
        self.vx = self.velocity
        self.vy = 0
    def wall_collision(self):
        if self.rect.y >= HEIGHT - 5 or self.rect.y <= 5:
            self.vy = -self.vy
    def pass_paddles(self):
        if self.rect.x >= WIDTH - 5 or self.rect.x <= 5:
            self.rect.center = (WIDTH/2, HEIGHT/2)
            self.vx = 2.5
            self.vy = 0
    def update(self):
        self.wall_collision()
        self.pass_paddles()
        self.rect.x += self.vx
        self.rect.y += self.vy