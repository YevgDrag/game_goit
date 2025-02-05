import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 500
WIDTH = 800
COLOR_WHITE = (255, 255, 255)
PLAYER_SIZE = (20, 20)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)


main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface(PLAYER_SIZE)
player.fill(COLOR_WHITE)
player_rect = player.get_rect()

player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [0, -1]
player_move_left = [-1, 0]

def create_bonus():
    BONUS_SIZE = (15, 15)
    bonus = pygame.Surface(BONUS_SIZE)
    bonus.fill(COLOR_RED)
    bonus_rect = pygame.Rect(random.randint(0, WIDTH), 0, *BONUS_SIZE)
    bonus_move = [0, 1]
    return [bonus, bonus_rect, bonus_move]


def create_enemy():
    ENEMY_SIZE = (30, 30)
    enemy = pygame.Surface(ENEMY_SIZE)
    enemy.fill(COLOR_BLUE)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *ENEMY_SIZE)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, random.randint(1000, 3500))

bonuses = []
enemies = []

playing = True

while playing:
    FPS.tick(220)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
                
    main_display.fill(COLOR_BLACK)
    
    
    keys = pygame.key.get_pressed()
    
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)
        
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)
                
    if keys[K_UP] and player_rect.top >= 0:
        player_rect = player_rect.move(player_move_up)
        
    if keys[K_LEFT] and player_rect.left >= 0:
        player_rect = player_rect.move(player_move_left)
    
    
    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
         
                   
    main_display.blit(player, player_rect)
    
    
    print(len(enemies))
        
    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
        