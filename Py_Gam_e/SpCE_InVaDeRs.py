import pygame
import os
import time
import random
pygame.font.init()

#SIZE OF THE GAME WINDOW
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH,  HEIGHT))
pygame.display.set_caption("Space Invaders")

#Import Images/ Load  Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets1", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets1", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets1", "pixel_ship_blue_small.png"))

#PLAYER/ USER SHIP
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets1", "pixel_ship_yellow.png"))

# Lasers/ Bullets
RED_LASER= pygame.image.load(os.path.join("assets1", "pixel_laser_red.png"))
GREEN_LASER= pygame.image.load(os.path.join("assets1", "pixel_laser_green.png"))
BLUE_LASER= pygame.image.load(os.path.join("assets1", "pixel_laser_blue.png"))
YELLOW_LASER= pygame.image.load(os.path.join("assets1", "pixel_laser_yellow.png"))

#BACKGROUND
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets1", "background-black.png")), (WIDTH,HEIGHT))

#DEFINING THE ATTRIBUTES OF THE SHIPS
class Ship:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img,  (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__ (self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP = {

    }

    def __init__(selfself, x, y, color, helath=100):
        super().__init__(x, y, health)

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    player_vel = 5 # movement speed of player

    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        '''refreshes screen'''
        WIN.blit(BG, (0,0))
        #draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (0,55,205))
        level_label = main_font.render(f"Level: {level}", 1, (0,205,55))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event .type == pygame.QUIT:
                run = False

#checks if any keys have been pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x + player_vel > 0: # move left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: #mive right
            player.x += player_vel
        if keys[pygame.K_w] and  player.y + player_vel > 0: #move up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #move down
            player.y += player_vel

main()