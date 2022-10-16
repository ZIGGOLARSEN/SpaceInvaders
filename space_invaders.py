import pygame

from Screen import Screen
from constants import *


pygame.init()


screen = Screen('Space Invaders', player_img, game_over_img, background_img)


screen.start()