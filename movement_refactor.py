import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

squares_1 = [
    [(520, 40), (520, 330), (760, 330), (760, 40)],
    [(760, 40), (760, 170), (880, 170), (880, 40)]
]


isometrics = [
    [(480, 280), (190, 425), (430, 545), (720, 400)],
    [(720, 400), (590, 465), (710, 525), (840, 460)]
]

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
velocity_reducer = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_walker_x = 0
    new_walker_y = 0
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


    # se o resultado ta dentro de algum squares_1, seta os moves e vai pro proximo
    updated_1 = False
    for sq1 in squares_1:
        x1 = sq1[0][0]
        y1 = sq1[0][1]
        x2 = sq1[2][0]
        y2 = sq1[2][1]

        new_walker_x = (right - left) * velocity + (down - up) * velocity
        new_walker_y = (left - right) * velocity + (down - up) * velocity
        isometric_new_walker_x = 2 * (right - left) * velocity
        isometric_new_walker_y = (down - up) * velocity

        if  x1 <= walker_x + new_walker_x <= x2 and y1 <= walker_y + new_walker_y <= y2:

            walker_x += new_walker_x
            walker_y += new_walker_y
            isometric_walker_x += isometric_new_walker_x
            isometric_walker_y += isometric_new_walker_y

            updated_1 = True
            break

    # se nao atualizou é pq tentou sair dos limites
    # preciso checar se so uma direcao foi pressionada???????????
    if not updated_1 and (up + down + left + right) == 1:
        # se chegou ate aqui é uma ou as duas direcoes nao fica dentro de um quadrado andavel
        # se x nao esta em nenhum quadrado, e y nao esta em nenhum quadrado, nao anda
        # senao
        # se x em algum quadrado, anda em x
        # se y em algum quadrado, anda em y

        for sq1 in squares_1:
            x1 = sq1[0][0]
            y1 = sq1[0][1]
            x2 = sq1[2][0]
            y2 = sq1[2][1]

            if  not (x1 <= walker_x <= x2 and y1 <= walker_y <= y2):
                continue

            if  x1 <= walker_x + new_walker_x <= x2 or y1 <= walker_y + new_walker_y <= y2:
                print("X ou Y dentro")
                if x1 <= walker_x + new_walker_x <= x2:
                    if left == 1:
                        up = 1
                    elif right == 1:
                        down = 1
                    elif up == 1:
                        left = 1
                    elif down == 1:
                        right = 1
                elif y1 <= walker_y + new_walker_y <= y2:
                    if left == 1:
                        down = 1
                    elif right == 1:
                        up = 1
                    elif up == 1:
                        right = 1
                    elif down == 1:
                        left = 1

                up *= velocity_reducer
                down *= velocity_reducer
                left *= velocity_reducer
                right *= velocity_reducer

                new_walker_x = (right - left) * velocity + (down - up) * velocity
                new_walker_y = (left - right) * velocity + (down - up) * velocity
                isometric_new_walker_x = 2 * (right - left) * velocity
                isometric_new_walker_y = (down - up) * velocity

                walker_x += new_walker_x
                walker_y += new_walker_y
                isometric_walker_x += isometric_new_walker_x
                isometric_walker_y += isometric_new_walker_y
                break     
        
    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

 
    square_point_to_draw = (walker_x, walker_y)

    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)
    pygame.draw.circle(screen, (0, 0, 0), square_point_to_draw, 15)
    pygame.draw.circle(screen, (0, 0, 0), (isometric_walker_x, isometric_walker_y), 15)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    for v in squares_1:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)   
        # pygame.draw.polygon(screen, (0, 0, 0), v)
    

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
