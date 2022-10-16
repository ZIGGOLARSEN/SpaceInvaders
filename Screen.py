import pygame
from constants import *
from Object import Bullet, Enemy, Player

class Screen:
    SCREEN_WIDTH = SCREEN_WIDTH
    SCREEN_HEIGHT = SCREEN_HEIGHT
    bullets = []
    enemies = []
    enemies_count = NUMBER_OF_ENEMIES

    def __init__(self, title, icon, game_over_img, background_img):  
        self.title = title
        self.icon = icon
        self.game_over_img = game_over_img
        self.background_img = background_img


    def setup(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.score = 0
        self.over = False
        
        pygame.display.set_caption(self.title)
        pygame.display.set_icon(self.icon)
        
        self.enemies = []
        self.initiate_enemies()
        
        if hasattr(self, 'player'): 
            delattr(self, 'player')
        self.player = Player(player_img)


    # handling events
    def handle_key_events(self, event):
        if event.type == pygame.KEYDOWN: 
            self.player.move(event.key)
            
            if event.key == pygame.K_SPACE:
                bullet = Bullet(bullet_img, self.player.x, self.player.y)
                self.bullets.append(bullet)

        if event.type == pygame.KEYUP: self.player.stop()

    def handle_quit(self, event):
        if event.type == pygame.QUIT: self.running = False


    # Screen updates
    def update(self):
        self.player.update_coords(self.player.x_change, self.player.y_change, self.screen)
        
        self.update_enemies()

        for bullet in self.bullets:
            bullet.move()
            bullet.update_coords(bullet.x_change, bullet.y_change, self.screen)

            if bullet.delete(): self.bullets.remove(bullet)

        self.colision()

        pygame.display.update()

    def colision(self):
        for bullet in self.bullets:
            for enemy in self.enemies:
                dist = (((bullet.x + bullet.width/2) - (enemy.x + enemy.width/2))**2 + (bullet.y - (enemy.y + enemy.height))**2)**0.5
                if dist <= 20:
                    self.enemies.remove(enemy)
                    self.enemies.append(Enemy(enemy_img))
                    self.bullets.remove(bullet)
                    self.score += 1
                    break
        
        for enemy in self.enemies:
            dist = (((enemy.x + enemy.width/2) - (self.player.x + self.player.width/2))**2 + ((enemy.y + enemy.height) - self.player.y)**2)**0.5
            if dist <= 20: self.game_over()


    # rendering enemies     
    def initiate_enemies(self):
        for _ in range(self.enemies_count):
            self.enemies.append(Enemy(enemy_img))

    def display_enemies(self):
        for enemy in self.enemies:
            enemy.move()
            enemy.handle_boundries()
    
    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update_coords(enemy.x_change, enemy.y_change, self.screen)

    
    # Score
    def display_score(self):
        score = self.font.render(f'Score: {self.score}', True, (255,255,255))
        self.screen.blit(score, (10,10))


    # Game over
    def check_game_over(self):
        for enemy in self.enemies:
            if enemy.y >= SCREEN_HEIGHT - enemy.height: self.game_over()

    def game_over(self):
        self.over = True 
        x = (SCREEN_WIDTH - self.game_over_img.get_width())/2
        y = (SCREEN_HEIGHT- self.game_over_img.get_height())/2 - 50

        self.screen.blit(self.game_over_img, (x,y))
        for enemy in self.enemies:
            enemy.stop()
        self.player.stop()
        self.bullets = []



    def start(self):
        self.setup()
        self.running = True
        
        while self.running:
            self.screen.blit(self.background_img, (0,0))

            self.display_enemies()

            self.display_score()

            for event in pygame.event.get():
                self.handle_quit(event)
                
                if not self.over:
                    self.handle_key_events(event)
                
                else: 
                    if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_r: self.setup()
            
            self.player.handle_boundries()
            
            self.check_game_over()
            self.update()
