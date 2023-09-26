import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
img_name = "isometric"
img_extension = "jpg"
image = pygame.image.load(f"assets/{img_name}.{img_extension}")
image_rect = image.get_rect()

angle = math.radians(45)
sin_angle = math.sin(angle)
cos_angle = math.cos(angle)
sqrt_2 = math.sqrt(2)

x1 = 520
x2 = 760
y1 = 40
y2 = 330

final_squares = []
final_isometrics = []
final_point_square = 0
final_point_isometric = 0

square_vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
isometric_vertices = []
for x, y in square_vertices:
    new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
    new_y = (x * sin_angle + y * cos_angle)/sqrt_2
    isometric_vertices.append((new_x, new_y))

square_point = square_vertices[0]
x = square_point[0]
y = square_point[1]
new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
new_y = (x * sin_angle + y * cos_angle)/sqrt_2
isometric_point = (new_x, new_y)

pressing_space = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pressing_space = False
                print("false")
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pressing_space = True
                print("true")
                continue
            elif event.key == pygame.K_w:
                y1 += 10 if pressing_space else -10
            elif event.key == pygame.K_a:
                x1 += 10 if pressing_space else -10
            elif event.key == pygame.K_s:
                y2 += -10 if pressing_space else 10
            elif event.key == pygame.K_d:
                x2 += -10 if pressing_space else 10
            elif event.key == pygame.K_UP:
                square_point = (square_point[0], square_point[1] - 10)
            elif event.key == pygame.K_DOWN:
                square_point = (square_point[0], square_point[1] + 10)
            elif event.key == pygame.K_LEFT:
                square_point = (square_point[0] - 10, square_point[1])
            elif event.key == pygame.K_RIGHT:
                square_point = (square_point[0] + 10, square_point[1])
            elif event.key == pygame.K_n:
                final_squares.append(square_vertices)
                final_isometrics.append(isometric_vertices)
                continue
            elif event.key == pygame.K_b:
                final_squares.pop()
                final_isometrics.pop()
                continue
            elif event.key == pygame.K_m:
                final_point_square = square_point
                final_point_isometric = isometric_point
                continue
            
            square_vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
            isometric_vertices = []
            for x, y in square_vertices:
                new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
                new_y = (x * sin_angle + y * cos_angle)/sqrt_2
                isometric_vertices.append((round(new_x), round(new_y)))

            print(isometric_vertices)
            x = square_point[0]
            y = square_point[1]
            new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
            new_y = (x * sin_angle + y * cos_angle)/sqrt_2
            isometric_point = (round(new_x), round(new_y))
            print(square_vertices)


    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

    for i, (x, y) in enumerate(isometric_vertices, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  
        text_rect = text_surface.get_rect(center=(x, y - 15)) 
        screen.blit(text_surface, text_rect)

    for i, (x, y) in enumerate(square_vertices, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  
        text_rect = text_surface.get_rect(center=(x, y - 15))  
        screen.blit(text_surface, text_rect)


    pygame.draw.polygon(screen, (255, 0, 0), isometric_vertices, 2)
    pygame.draw.polygon(screen, (255, 0, 0), square_vertices, 2)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)  
    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)

    for v in final_squares:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    for v in final_isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  


    pygame.display.flip()

    clock.tick(60)


# salvar aqui num txt

file_path = f"assets/{img_name}.txt"

# Open the file in write mode
with open(file_path, "w") as file:

    file.write("squares\n")
    for item in final_squares:
        file.write(str(item) + "\n")

    file.write("\nisometrics\n")
    for item in final_isometrics:
        file.write(str(item) + "\n")

    file.write("\nsquare_point\n")
    file.write(str(final_point_square) + "\n")

    file.write("\nisometric_point\n")
    file.write(str(final_point_isometric) + "\n")


pygame.quit()
sys.exit()
