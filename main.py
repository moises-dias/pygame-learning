import pygame
import sys
# from room_1 import Room1
from player import Player
from sprite_flyweight import SpriteFlyweight
from room_factory import RoomFactory

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

sprite_flyweight = SpriteFlyweight()
room_factory = RoomFactory()

room = room_factory.create_room("room1", sprite_flyweight)
player = Player(
    room.starting_position, 
    room.isometric_starting_position, 
    room.starting_direction,
    sprite_flyweight
)

leaving_room = False
entering_room = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # print(pygame.mouse.get_pos()) # 330, 440

    left = 0
    right = 0
    up = 0
    down = 0

    # TODO cancelar movimento se o jogador estiver mudando de fase (transition = true?) e falar walking = false
    if not (leaving_room or entering_room):
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
        player.walk(up, down, left, right, room.floor.squares)
    else:
        player.walking = False

    player.update()
    room.update(player.pos)

    if room.next_room is not None and keys[pygame.K_SPACE] and not leaving_room:
        leaving_room = True
        player.walking = False
        radius = 0
        print("move")

    screen.fill((0, 0, 0)) 
    screen.blit(room.map_image, room.map_image_rect)

    for img_info in room.to_draw:
        screen.blit(img_info["img"], img_info["pos"])

    screen.blit(player.sprite.get_image(), player.get_sprite_position())


    pygame.draw.polygon(screen, (0, 255, 0), player.get_isometric_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.isometric_pos, 5)

    pygame.draw.polygon(screen, (0, 0, 255), player.get_position_square(), 2)
    pygame.draw.circle(screen, (0, 0, 0), player.pos, 5)

    for bbox in room.floor.squares:
        pygame.draw.polygon(screen, (0, 0, 255), bbox, 2)  
    for bbox in room.floor.isometric_squares:
        pygame.draw.polygon(screen, (0, 255, 0), bbox, 2) 
 
    for door in room.doors:
        pygame.draw.polygon(screen, (255, 255, 0), door.square, 2)  
        pygame.draw.polygon(screen, (255, 255, 0), door.isometric_square, 2)  
    

    # TODO precisa criar o transition surf toda vez?
    if leaving_room:
        transition_surf = pygame.Surface(screen.get_size())
        transition_surf.set_colorkey((255, 255, 255))
        pygame.draw.circle(transition_surf, (255, 255, 255), player.isometric_pos, (100 - radius) * 8)
        
        radius += 1
        print(radius)
        screen.blit(transition_surf, (0, 0))
        if radius == 100:
            print("end")
            radius = 0
            leaving_room = False
            room = room_factory.create_room(room.next_room, sprite_flyweight)
            player.reset_position(
                room.starting_position,
                room.isometric_starting_position,
                room.starting_direction
            )
            entering_room = True
            # TODO Aqui, deixar tudo preto menos o jogador
            # levar a sprite do jogador até a nova posicao (enqnt ta td preto)
            # e só entao fazer o fade pra mostrar a fase
    
    # TODO precisa criar o transition surf toda vez?
    elif entering_room:
        transition_surf = pygame.Surface(screen.get_size())
        transition_surf.set_colorkey((255, 255, 255))
        pygame.draw.circle(transition_surf, (255, 255, 255), player.isometric_pos, (radius) * 8)
        
        radius += 1
        print(radius)
        screen.blit(transition_surf, (0, 0))
        if radius == 100:
            print("end")
            entering_room = False


    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
