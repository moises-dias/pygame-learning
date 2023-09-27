import pygame
import sys
from floor_1 import Floor1
from stage_1 import Stage1
from player import Player

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
image = pygame.image.load("assets/simple_isometric.png")

image_rect = image.get_rect()

floor = Floor1()
stage = Stage1(floor)
player = Player(stage.starting_position, stage.isometric_starting_position)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    left = 0
    right = 0
    up = 0
    down = 0

    if keys[pygame.K_LEFT]:
        left = 1
    if keys[pygame.K_RIGHT]:
        right = 1
    if keys[pygame.K_UP]:
        up = 1
    if keys[pygame.K_DOWN]:
        down = 1
    
    player.walk(up, down, left, right, stage.floor.squares)


    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)


    pygame.draw.polygon(screen, (0, 255, 0), player.get_isometric_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.isometric_pos, 5)

    pygame.draw.polygon(screen, (0, 0, 255), player.get_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.pos, 5)

    for bbox in stage.floor.squares:
        pygame.draw.polygon(screen, (0, 0, 255), bbox, 2)  
    for bbox in stage.floor.isometric_squares:
        pygame.draw.polygon(screen, (0, 255, 0), bbox, 2)  
    

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
