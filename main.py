import pygame
import sys
from stage_1 import Stage1
from player import Player
from sprite_flyweight import SpriteFlyweight

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

sprite_flyweight = SpriteFlyweight()

stage = Stage1(sprite_flyweight)
player = Player(
    stage.starting_position, 
    stage.isometric_starting_position, 
    sprite_flyweight
)


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
    
    if (up + down + left + right) > 0:
        # player.walking = True
        player.walk(up, down, left, right, stage.floor.squares)
    else:
        player.walking = False

    player.update()
    stage.update(player.pos)
    # stage.update passando player position pra ver se entrou numa porta?

    screen.fill((0, 0, 0)) 
    screen.blit(stage.map_image, stage.map_image_rect)

    for img_info in stage.to_draw:
        screen.blit(img_info["img"], img_info["pos"])

    screen.blit(player.sprite.get_image(), player.get_sprite_position())


    pygame.draw.polygon(screen, (0, 255, 0), player.get_isometric_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.isometric_pos, 5)

    pygame.draw.polygon(screen, (0, 0, 255), player.get_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.pos, 5)

    for bbox in stage.floor.squares:
        pygame.draw.polygon(screen, (0, 0, 255), bbox, 2)  
    for bbox in stage.floor.isometric_squares:
        pygame.draw.polygon(screen, (0, 255, 0), bbox, 2) 
 
    for door in stage.doors:
        pygame.draw.polygon(screen, (255, 255, 0), door.square, 2)  
        pygame.draw.polygon(screen, (255, 255, 0), door.isometric_square, 2)  
    

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
