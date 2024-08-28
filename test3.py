import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()
player_animation_clock = pygame.time.Clock()


HEIGHT = 800
WIDTH = 1200
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_PINK = (255, 0, 255)

FONT = pygame.font.SysFont('Verdana', 20)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load("C:/Projects/Game/other/background.png"), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 1

PLAYER_SIZE = (40, 40)
# player = pygame.Surface(PLAYER_SIZE)
player_images = [
    pygame.transform.scale(pygame.image.load('C:/Projects/Game/Goose/1-1.png').convert_alpha(), (120, 50)),
    pygame.transform.scale(pygame.image.load('C:/Projects/Game/Goose/1-2.png').convert_alpha(), (120, 50)),
    pygame.transform.scale(pygame.image.load('C:/Projects/Game/Goose/1-3.png').convert_alpha(), (120, 50)),
    pygame.transform.scale(pygame.image.load('C:/Projects/Game/Goose/1-4.png').convert_alpha(), (120, 50)),
    pygame.transform.scale(pygame.image.load('C:/Projects/Game/Goose/1-5.png').convert_alpha(), (120, 50)),
]
# player.fill(COLOR_PINK)
current_frame = 0

# player_rect = pygame.Rect(100, 300, *player_images.get_size())
player_rect = pygame.Rect(100, 300, *PLAYER_SIZE)

player_move_down = [0, 4]
player_move_right = [4, 0]
player_move_up = [0, -4]
player_move_left = [-4, 0]

def create_bonus():
    # BONUS_SIZE = (30, 30)
    # bonus = pygame.Surface(BONUS_SIZE)
    # bonus.fill(COLOR_RED)
    bonus = pygame.image.load('C:/Projects/Game/other/bonus.png').convert_alpha()
    bonus_rect = pygame.Rect(random.randint(400, 750), 0, *bonus.get_size())
    bonus_move = [0, 1]
    return [bonus, bonus_rect, bonus_move]


def create_enemy():
    ENEMY_SIZE = (30, 30)
    # enemy = pygame.Surface(ENEMY_SIZE)
    # enemy.fill(COLOR_BLUE)
    enemy = pygame.image.load('C:/Projects/Game/other/enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(WIDTH, random.randint(200, 650), *enemy.get_size())
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, random.randint(1000, 3500))

bonuses = []
enemies = []
score = 0
playing = True


while playing:
    FPS.tick(220)
    player_animation_clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
                
                
                
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
    
    player_image = player_images[current_frame]
    current_frame = (current_frame + 1) % len(player_images)
                   
    main_display.blit(player_image, player_rect)
    
    # print(len(bonuses))
    # print(len(enemies))
    
    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))
            
    for bonus in bonuses:
        if bonus[1].bottom > HEIGHT:
            bonuses.pop(bonuses.index(bonus))
        