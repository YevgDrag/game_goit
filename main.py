import random
import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT


pygame.mixer.init()
pygame.init()


FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_PINK = (255, 0, 255)

FONT = pygame.font.SysFont('Verdana', 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load("C:/Projects/game_goit/img/background.png"), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 1


# PLAYER_SIZE = (40, 40)
# player = pygame.Surface(PLAYER_SIZE)
player = pygame.transform.scale(pygame.image.load('C:/Projects/game_goit/goose/1-1.png').convert_alpha(), (12, 50))
# player.fill(COLOR_PINK)
player_rect = pygame.Rect(100, 300, *player.get_size())

IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

def create_bonus():
    # BONUS_SIZE = (30, 30)
    # bonus = pygame.Surface(BONUS_SIZE)
    # bonus.fill(COLOR_RED)
    bonus = pygame.transform.scale(pygame.image.load('C:/Projects/game_goit/img/bonus.png').convert_alpha(), (50, 80))
    bonus_rect = pygame.Rect(random.randint(400, 750), 0, *bonus.get_size())
    bonus_move = [0, 1]
    return [bonus, bonus_rect, bonus_move]

# sound = pygame.mixer.Sound('C:/Projects/Game/other/sound.wav')

def create_enemy():
    ENEMY_SIZE = (30, 30)
    # enemy = pygame.Surface(ENEMY_SIZE)
    # enemy.fill(COLOR_BLUE)
    enemy = pygame.image.load('C:/Projects/game_goit/img/enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(WIDTH, random.randint(20, 650), *enemy.get_size())
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, random.randint(1000, 3500))

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 100)

# PLAY_SOUND = pygame.USEREVENT + 4
# pygame.time.set_timer(PLAY_SOUND, 1)

bonuses = []
enemies = []

score = 0

image_index = 0

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
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0
        # if event.type == PLAY_SOUND:
        #     sound.play()
                
    # main_display.fill(COLOR_BLACK)
    bg_X1 -= bg_move
    bg_X2 -= bg_move
    
    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width() 
    
    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))
    
    
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
        
        if player_rect.colliderect(enemy[1]):
            playing = False
        
    for bonus in bonuses:
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        
        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.pop(bonuses.index(bonus)) 
    
    
    
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))
                   
    main_display.blit(player, player_rect)
    
    # print(len(bonuses))
    # print(len(enemies))
    
    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
            
    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
        