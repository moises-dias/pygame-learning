import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

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

    left = 0
    right = 0
    up = 0
    down = 0

    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        left = 1
    if keys[pygame.K_RIGHT]:
        right = 1
    if keys[pygame.K_UP]:
        up = 1
    if keys[pygame.K_DOWN]:
        down = 1

    if (up + down + left + right) == 1:
        if left == 1:
            if not (x1 <= walker_x - velocity):
                if (walker_y + velocity <= y2):
                    down += 1   
            elif not (walker_y + velocity <= y2):
                if (x1 <= walker_x - velocity):
                    up += 1

        elif right == 1:
            if not (walker_x + velocity <= x2):
                if (y1 <= walker_y - velocity):
                    up += 1   
            elif not (y1 <= walker_y - velocity):
                if (walker_x + velocity <= x2):
                    down += 1

        elif up == 1:
            if not (x1 <= walker_x - velocity):
                if (y1 <= walker_y - velocity):
                    right += 1   
            elif not (y1 <= walker_y - velocity):
                if (x1 <= walker_x - velocity):
                    left += 1

        elif down == 1:
            if not (walker_y + velocity <= y2):
                if (walker_x + velocity <= x2):
                    right += 1   
            elif not (walker_x + velocity <= x2):
                if (walker_y + velocity <= y2):
                    left += 1

    if (right - left) != 0:
        new_walker_x_h = (right - left) * velocity
        new_walker_y_h = (left - right) * velocity
        isometric_new_walker_x = 2 * (right - left) * velocity
    if (up - down) != 0:
        new_walker_x_v = (down - up) * velocity
        new_walker_y_v = (down - up) * velocity
        isometric_new_walker_y = (down - up) * velocity

    if  x1 <= walker_x + new_walker_x_h + new_walker_x_v <= x2 and y1 <= walker_y + new_walker_y_h + new_walker_y_v <= y2:
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

    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)
    pygame.draw.circle(screen, (0, 0, 0), square_point_to_draw, 15)
    pygame.draw.circle(screen, (0, 0, 0), (isometric_walker_x, isometric_walker_y), 15)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    for v in squares:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    
    pygame.draw.polygon(screen, (0, 255, 0), square_to_draw, 2)  


    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
