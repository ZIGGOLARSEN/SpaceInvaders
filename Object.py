import pygame
import random
from constants import *

class Object:
    x_change = 0
    y_change = 0

    def __init__(self, image):
        self.image = image
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.x = (SCREEN_WIDTH-self.width)/2
        self.y = SCREEN_HEIGHT - self.height - 50
    

    def display_on_screen(self,screen):
        screen.blit(self.image, (self.x, self.y))
    

    def update_coords(self, x_change, y_change, screen):
        self.x += x_change
        self.y += y_change
        self.display_on_screen(screen)
    

    def handle_boundries(self):
        if self.x >= SCREEN_WIDTH-self.width: self.x = SCREEN_WIDTH - self.width
        
        if self.x <= 0: self.x = 0
        
        if self.y >= SCREEN_HEIGHT-self.height: self.y = SCREEN_HEIGHT - self.height
        
        if self.y <= 0: self.y = 0


    def stop(self):
        self.x_change = 0
        self.y_change = 0



class Player(Object):
    def __init__(self, image):
        super().__init__(image)
    
        self.speed = PLAYER_SPEED
    

    def move(self, key):
        if key == pygame.K_LEFT: self.x_change = -self.speed
    
        if key == pygame.K_RIGHT: self.x_change = self.speed



class Enemy(Object):
    def __init__(self, image):
        super().__init__(image)
        
        self.speed = ENEMY_SPEED
        self.x_change = self.direction() * self.speed
        
        self.display_randomly()
    
    def direction(self):
        return random.choice([-1,1])

    def display_randomly(self):
        self.x = random.randint(100, SCREEN_WIDTH - self.width - 100)
        self.y = random.randint(0, int((SCREEN_HEIGHT-self.height)/2))
    

    def move(self):
        if self.x <= 0 or self.x >= SCREEN_WIDTH-self.width: 
            self.x_change = -self.x_change
            self.y_change = 40
        else:
            self.y_change = 0


class Bullet(Object):
    def __init__(self, image, x, y):
        super().__init__(image)
        self.speed = BULLET_SPEED
        self.x = x + self.width/2
        self.y = y - self.height
    
    def delete(self):
        if self.y <=0: return True
        
        return False 

    def move(self):
        self.y_change = -self.speed
