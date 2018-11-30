#This file was created by Ricardo Pedrayes and Jacob Tarango

from settings import *
from sprites import *
import random
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
        self.all_sprites = pg.sprite.Group()
        self.player_1 = Player()
        self.player_2 = Player()
        # self.player_4 = Player
        # Player 2 controls and other info
        self.player_2.up = pg.K_w
        self.player_2.down = pg.K_s
        self.player_2.rect.center = (WIDTH/12, HEIGHT/2)
        # self.player_4.rect.center = (WIDTH/0, HEIGHT/0)

        self.all_sprites.add(self.player_1)
        self.all_sprites.add(self.player_2)
        # self.all_sprites.add(self.player_4)
        self.run()
        # create new player object
    def run(self):
        self.playing = True
        # game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # update things
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        # listening for events
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
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