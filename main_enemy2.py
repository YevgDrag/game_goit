import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 300
WIDTH = 400
COLOR_WHITE = (255, 255, 255)
PLAYER_SIZE = (20, 20)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
ENEMY_SIZE = (5, 40)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [0, -1]
player_move_left = [-1, 0]


enemy = pygame.Surface(ENEMY_SIZE)
enemy.fill(COLOR_BLUE)
enemy_rect = enemy.get_rect()
enemy_speed = [0, 1]
enemy_move = [-1, 0]

playing = True

while playing:
    FPS.tick(220)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    main_display.fill(COLOR_BLACK)
    
    enemy_rect = enemy_rect.move(enemy_speed)
    
    keys = pygame.key.get_pressed()
    
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
        
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)
                
    if keys[K_UP] and player_rect.top >= 0:
        player_rect = player_rect.move(player_move_up)
        
        
    if keys[K_LEFT] and player_rect.left >= 0:
        player_rect = player_rect.move(player_move_left)
        
    
    if enemy_rect.bottom >= HEIGHT:
        enemy_speed = [0, -1]
           
    # if player_rect.right >= WIDTH:
    #     player_speed = random.choice(([-1, 1], [-1, -1]))
    
    if enemy_rect.top <= 0:
        enemy_speed = [0, 1]
            
    # if player_rect.left < 0:
    #     player_speed = random.choice(([1, 1], [-1, 1]))
                
    main_display.blit(player, player_rect)
    
    main_display.blit(enemy, enemy_rect)
        
    pygame.display.flip()