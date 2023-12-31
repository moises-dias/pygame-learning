import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

floors_squares = [
[(530, 220), (530, 330), (760, 330), (760, 220)],
[(620, 80), (620, 220), (760, 220), (760, 80)],
[(660, 40), (660, 80), (760, 80), (760, 40)],
]
npcs_squares = [
[(620, 40), (620, 80), (660, 80), (660, 40)],
]
door_squares = [
[(530, 230), (530, 320), (580, 320), (580, 230)]
]


isometrics = [
[(310, 375), (200, 430), (430, 545), (540, 490)],
[(540, 350), (400, 420), (540, 490), (680, 420)],
[(620, 350), (580, 370), (680, 420), (720, 400)],
[(580, 330), (540, 350), (580, 370), (620, 350)],
[(300, 380), (210, 425), (260, 450), (350, 405)]
]


border = 15
square_point = (690, 160)
walker_x = square_point[0]
walker_y = square_point[1]

isometric_point = (530, 425)
isometric_walker_x = isometric_point[0]
isometric_walker_y = isometric_point[1]


# gerando o isometric do personagem na tela
# [(530, 180), (530, 380), (580, 380), (580, 180)] up-left, down-left, down-right, up-right
square_reference = [(-border, -border), (-border, border), (border, border), (border, -border)]

angle = math.radians(45)
sin_angle = math.sin(angle)
cos_angle = math.cos(angle)
sqrt_2 = math.sqrt(2)

isometric_reference = []
for x, y in square_reference:
    new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
    new_y = (x * sin_angle + y * cos_angle)/sqrt_2
    isometric_reference.append((round(new_x), round(new_y)))

print(isometric_reference)

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
    
    new_walker_x = (right - left) * velocity + (down - up) * velocity
    new_walker_y = (left - right) * velocity + (down - up) * velocity
    isometric_new_walker_x = 2 * (right - left) * velocity
    isometric_new_walker_y = (down - up) * velocity

    if left == 1 or right == 1:
        new_walker_x *= velocity_reducer
        new_walker_y *= velocity_reducer
        isometric_new_walker_x *= velocity_reducer
        isometric_new_walker_y *= velocity_reducer

    for sq1 in floors_squares:
        x1 = sq1[0][0]
        y1 = sq1[0][1]
        x2 = sq1[2][0]
        y2 = sq1[2][1]


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

        for sq1 in floors_squares:
            x1 = sq1[0][0]
            y1 = sq1[0][1]
            x2 = sq1[2][0]
            y2 = sq1[2][1]

            if  not (x1 <= walker_x <= x2 and y1 <= walker_y <= y2):
                continue

            if  x1 <= walker_x + new_walker_x <= x2 or y1 <= walker_y + new_walker_y <= y2:
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

                if  x1 <= walker_x + new_walker_x <= x2 and y1 <= walker_y + new_walker_y <= y2:

                    walker_x += new_walker_x
                    walker_y += new_walker_y
                    isometric_walker_x += isometric_new_walker_x
                    isometric_walker_y += isometric_new_walker_y
                break     


    for sq1 in door_squares:
        x1 = sq1[0][0]
        y1 = sq1[0][1]
        x2 = sq1[2][0]
        y2 = sq1[2][1]

        if  x1 <= walker_x + new_walker_x <= x2 and y1 <= walker_y + new_walker_y <= y2:
            print("open door")

    for sq1 in npcs_squares:
        x1 = sq1[0][0]
        y1 = sq1[0][1]
        x2 = sq1[2][0]
        y2 = sq1[2][1]

        if  x1 <= walker_x + new_walker_x <= x2 and y1 <= walker_y + new_walker_y <= y2:
            print("talk to npc")

    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

 

    # pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    # pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)

    square_point_to_draw = (walker_x, walker_y)

    # [(0, -15), (-30, 0), (0, 15), (30, 0)]
    isometric_position_vertices = []
    for v in isometric_reference:
        isometric_position_vertices.append((isometric_walker_x + v[0], isometric_walker_y + v[1]))
    pygame.draw.polygon(screen, (0, 255, 0), isometric_position_vertices, 2)

    square_position_vertices = [(walker_x - border, walker_y - border), (walker_x - border, walker_y + border), (walker_x + border, walker_y + border), (walker_x + border, walker_y - border)]
    pygame.draw.polygon(screen, (0, 0, 255), square_position_vertices, 2)
    pygame.draw.circle(screen, (0, 0, 0), square_point_to_draw, 5)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    pygame.draw.circle(screen, (0, 0, 0), (isometric_walker_x, isometric_walker_y), 5)
    for v in floors_squares:
        pygame.draw.polygon(screen, (0, 0, 255), v, 2)   
    for v in npcs_squares:
        pygame.draw.polygon(screen, (255, 0, 255), v, 2)   
    for v in door_squares:
        pygame.draw.polygon(screen, (255, 0, 0), v, 2)   
    

    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
