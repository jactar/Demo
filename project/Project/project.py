#This file was created by Ricardo Pedrayes and Jacob Tarango

from settings import *
from sprites import *
import random
from random import randint
import pygame as pg

class Game:
    def __init__(self):
        # init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        # init pygame and create...
    def new(self):
        self.players = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        self.player_1 = Player()
        self.player_2 = Player()
        self.Linea = Object()
        # adding ball
        self.ball = Ball()

        # Player 2 controls and other info
        self.player_2.up = pg.K_w
        self.player_2.down = pg.K_s
        self.player_2.rect.center = (WIDTH/12, HEIGHT/2)

        self.players.add(self.player_1)
        self.players.add(self.player_2)
        self.balls.add(self.ball)
        self.balls.add(self.Linea)
        self.run()
        # create new player object
    def run(self):
        self.playing = True
        # game loop
        while self.playing:
            self.clock.tick(FPS)
            self.collide()
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.players.update()
        self.balls.update()
        
        # Collide ball and paddle
    def collide(self):
            hit = pg.sprite.spritecollideany(self.ball, self.players, False)
            if hit:
                self.ball.vx = -self.ball.vx * 1.12
                self.ball.vy = self.ball.vy
            # if hit = True:
            #     self.vx = -vx
                

        # update thingsw
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        # listening for events
    def draw(self):
        self.screen.fill(BLACK)
        self.players.draw(self.screen)
        self.balls.draw(self.screen)
        
        # self.draw.rect(self.screen, self.WHITE, self.central_line)
        # self.screen.draw.line(screen,WHITE,(0,0),(0,10),5)
        # self.screen.line(draw.image, (0,0), (0,9), width=1)
        # self.screen.line(self.screen, WHITE, (30, 180), (30, 240), (4))
        # self.draw.line(screen,WHITE,(0,0),(0,10),(5))
        #double buffer
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()



while g.running:
    g.new()
    g.show_go_screen()

pg.quit()