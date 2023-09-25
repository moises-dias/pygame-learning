import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

squares = [[(520, 40), (520, 330), (760, 330), (760, 40)]]
x1 = squares[0][0][0]
y1 = squares[0][0][1]
x2 = squares[0][2][0]
y2 = squares[0][2][1]

isometrics = [[(480, 280), (190, 425), (430, 545), (720, 400)]]

square_point = (660, 200)
walker_x = square_point[0]
walker_y = square_point[1]
new_walker_x_v = 0
new_walker_y_v = 0
new_walker_x_h = 0
new_walker_y_h = 0

isometric_point = (460.0, 430.0)
isometric_walker_x = isometric_point[0]
isometric_walker_y = isometric_point[1]
isometric_new_walker_x = 0
isometric_new_walker_y = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
image = pygame.image.load("assets/simple_isometric.png")
image_rect = image.get_rect()

velocity = 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_walker_x_h = 0
    new_walker_y_h = 0
    new_walker_x_v = 0
    new_walker_y_v = 0
    isometric_new_walker_x = 0
    isometric_new_walker_y = 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        new_walker_x_h = -velocity
        new_walker_y_h = +velocity
        isometric_new_walker_x = -2*velocity
    if keys[pygame.K_RIGHT]:
        new_walker_x_h = +velocity
        new_walker_y_h = -velocity
        isometric_new_walker_x = 2 * velocity
    if keys[pygame.K_UP]:
        new_walker_x_v = -velocity
        new_walker_y_v = -velocity
        isometric_new_walker_y = -velocity
    if keys[pygame.K_DOWN]:
        new_walker_x_v = +velocity
        new_walker_y_v = +velocity
        isometric_new_walker_y = +velocity

    # squares = [[(520, 40), (520, 330), (760, 330), (760, 40)]]

    if not (x1 <= walker_x + new_walker_x_h <= x2 and y1 <= walker_y + new_walker_y_h <= y2):
        new_walker_x_h = 0
        new_walker_y_h = 0
        isometric_new_walker_x = 0
    if not (x1 <= walker_x + new_walker_x_v <= x2 and y1 <= walker_y + new_walker_y_v <= y2):
        new_walker_x_v = 0
        new_walker_y_v = 0
        isometric_new_walker_y = 0
    
    walker_x += new_walker_x_h
    walker_y += new_walker_y_h
    isometric_walker_x += isometric_new_walker_x
    walker_x += new_walker_x_v
    walker_y += new_walker_y_v
    isometric_walker_y += isometric_new_walker_y



        
    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

 
    square_to_draw = [(x, y) for x,y in squares[0]]
    square_point_to_draw = (walker_x, walker_y)
    # print(square_to_draw)

    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)
    pygame.draw.circle(screen, (0, 255, 255), square_point_to_draw, 5)
    pygame.draw.circle(screen, (0, 255, 255), (isometric_walker_x, isometric_walker_y), 5)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    for v in squares:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    
    pygame.draw.polygon(screen, (0, 255, 0), square_to_draw, 2)  


    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
