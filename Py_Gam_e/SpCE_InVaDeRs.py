import pygame
import os
import time
import random

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
BG  = pygame.image.load(os.path.join("assets1", "background-black.png"))

