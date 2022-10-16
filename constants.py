import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

PLAYER_SPEED = .3
ENEMY_SPEED = .35
BULLET_SPEED = 1.2

NUMBER_OF_ENEMIES = 4



background_img = pygame.image.load(r'.\images\background_img.jpg')
game_over_img = pygame.image.load('.\images.\game-over.png')

player_img= pygame.image.load('.\images\space-invaders.png')
enemy_img = pygame.image.load(r'.\images\alien.png')
bullet_img = pygame.image.load(r'.\images\bullet.png')
