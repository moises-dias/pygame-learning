import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

squares_1 = [
[(530, 180), (530, 380), (580, 380), (580, 180)],
[(390, 180), (390, 380), (430, 380), (430, 180)],
[(430, 330), (430, 380), (530, 380), (530, 330)],
[(430, 180), (430, 230), (530, 230), (530, 180)],
[(460, 110), (460, 180), (520, 180), (520, 110)],
[(350, 30), (350, 110), (630, 110), (630, 30)],
[(350, -170), (350, 30), (460, 30), (460, -170)],
[(530, -170), (530, 30), (630, 30), (630, -170)],
[(460, -170), (460, -80), (530, -80), (530, -170)]
]


isometrics = [
[(350, 355), (150, 455), (200, 480), (400, 380)],
[(210, 285), (10, 385), (50, 405), (250, 305)],
[(100, 380), (50, 405), (150, 455), (200, 430)],
[(250, 305), (200, 330), (300, 380), (350, 355)],
[(350, 285), (280, 320), (340, 350), (410, 315)],
[(320, 190), (240, 230), (520, 370), (600, 330)],
[(520, 90), (320, 190), (430, 245), (630, 145)],
[(700, 180), (500, 280), (600, 330), (800, 230)],
[(630, 145), (540, 190), (610, 225), (700, 180)]
]

square_point = (560, 290)
walker_x = square_point[0]
walker_y = square_point[1]
new_walker_x_v = 0
new_walker_y_v = 0
new_walker_x_h = 0
new_walker_y_h = 0

isometric_point = (270, 425)
isometric_walker_x = isometric_point[0]
isometric_walker_y = isometric_point[1]
isometric_new_walker_x = 0
isometric_new_walker_y = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
image = pygame.image.load("assets/isometric.jpg")
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

 

    # pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    # pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)

    square_point_to_draw = (walker_x, walker_y)
    pygame.draw.circle(screen, (0, 0, 0), square_point_to_draw, 15)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    pygame.draw.circle(screen, (0, 0, 0), (isometric_walker_x, isometric_walker_y), 15)
    for v in squares_1:
        pygame.draw.polygon(screen, (0, 0, 255), v, 2)   
        # pygame.draw.polygon(screen, (0, 0, 0), v)
    

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
