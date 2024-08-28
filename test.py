import pygame
from pygame.constants import QUIT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 300
WIDTH = 400
COLOR_WHITE = (255, 255, 255)
BALL_RADIUS = 10
COLOR_BLACK = (0, 0, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)
pygame.draw.circle(player, COLOR_WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

player_rect = player.get_rect()
player_speed = [1, 1]

playing = True

while playing:
    FPS.tick(220)
    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
            
    main_display.fill(COLOR_BLACK)
    
    player_rect = player_rect.move(player_speed)
    
    if player_rect.bottom >= HEIGHT or player_rect.top <= 0:
        player_speed[1] = -player_speed[1]
    
    if player_rect.right >= WIDTH or player_rect.left < 0:
        player_speed[0] = -player_speed[0]
                
    main_display.blit(player, player_rect)
    
    pygame.display.flip()

pygame.quit()
