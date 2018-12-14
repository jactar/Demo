#This file was created by Ricardo Pedrayes and Jacob Tarango
'''
Sources
pygame.org
'''

from settings import *
from sprites import *
import random
from random import randint
import pygame as pg
''' 
**********Gameplay ideas:
The paddles work with the up and down arrow for the right player,
and W and S keys for player 2
The ball moves with a speed of 2.5 at the start going right with no vy
once the ball hits the paddle it speeds up and starts moving with a
random vy
once the ball goes past the paddle and hits the left or right boundries
the ball will return to the center of the screen and start from beginning
**********Cosmetics
None
**********Bugs
after around 12 hits, the ball gets stuck in a paddle and will
fly out and go through the other paddle
Paddles will be able to go through the top and bottom of the screen
if they are too close to the edges from the bouncing of the wall collision
function
**********Gameplay fixes
Ball will now reset in the middle fo the screen as soon as it 
leaves the screen on either end, moving at a slow speed kind 
of like a restart method
Added borders for the paddles on the top and bottom of the screen
**********Features
Great, world class coding, with flawless gameplay.
'''
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
        # putting sprites into groups
        self.players = pg.sprite.Group()
        self.balls = pg.sprite.Group()
        # Creating the different players
        self.player_1 = Player()
        self.player_2 = Player()
        # adding the line
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
        # Updating the sprites
        self.players.update()
        self.balls.update()
        
        # Collide ball and paddle
    def collide(self):
            hit = pg.sprite.spritecollideany(self.ball, self.players, False)
            if hit:
                if abs(self.ball.vx) <= 10.74:
                    self.ball.vx = -self.ball.vx + (-.2 * self.ball.vx)
                elif abs(self.ball.vx) > 10.74:
                    self.ball.vx = -self.ball.vx
                self.ball.vy = self.ball.vy + randint(-2,2)
                print(self.ball.vx)

                

        # update things
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
        # listening for events
    def draw(self):
        # setting background black and putting sprites on screen
        self.screen.fill(BLACK)
        self.players.draw(self.screen)
        self.balls.draw(self.screen)
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