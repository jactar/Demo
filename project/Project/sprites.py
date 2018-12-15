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
        if self.rect.y >= HEIGHT - 10 or self.rect.y <= 10:
            self.vy = -self.vy
        # If it gets within a certain distance of the Height on both sides, it bounces back but it glitches
    def update(self):
        self.vy = 0
        self.vx = 0
        # self.gravity()
        keys = pg.key.get_pressed()
        if keys[self.up]:
            self.vy = -7
        if keys[self.down]:
            self.vy = 7
        if keys[pg.K_BACKSPACE]:
            pg.quit()
        #The controls to the game including how to exit
        self.wall1_collision()
        

        self.rect.y += self.vy


    # def borders(self):
    #     if self.rect.x == WIDTH:
    #         self.vx = 0
    
class Object(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((5,HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH*6/12, HEIGHT/2)
        #Adds in the middle line of the game

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
        #Adds in the ball into the game with its starting point and speed
    def wall_collision(self):
        if self.rect.y >= HEIGHT - 5 or self.rect.y <= 5:
            self.vy = -self.vy
        #It bounces back into the game if it hits any of the sides of the screen
    def pass_paddles(self):
        if self.rect.x >= WIDTH - 5 or self.rect.x <= 5:
            self.rect.center = (WIDTH/2, HEIGHT/2)
            self.vx = 2.5
            self.vy = 0
        #If it passes the paddles, it will bounce back to the other side
    def scoring(self):
        self.score = 0
        self.score2 = 0
        if self.rect.x >= WIDTH - 5:
            self.score += 1
            print(self.score)
        if self.rect.x <= 5:
            self.score2 += 0
            print(self.score2)
    def update(self):
        self.wall_collision()
        self.pass_paddles()
        self.rect.x += self.vx
        self.rect.y += self.vy
        #updates everything for the game
    #def scoring(self):