import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
img_name = "simple_isometric"
img_extension = "png"
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

upper_left_vertex_drag = True

square_type = "floor"
final_types = []
final_squares = []
final_isometrics = []

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

        elif pygame.mouse.get_pressed()[0]:  # Left mouse button pressed
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print("foo")
            
            # Round the mouse position to the nearest multiple of 10
            if square_type == "player":
                square_point = (round(mouse_x / 10) * 10, round(mouse_y / 10) * 10)
                x = square_point[0]
                y = square_point[1]
                new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
                new_y = (x * sin_angle + y * cos_angle)/sqrt_2
                isometric_point = (round(new_x), round(new_y))
            elif upper_left_vertex_drag:
                x1 = round(mouse_x / 10) * 10
                y1 = round(mouse_y / 10) * 10
            else:
                x2 = round(mouse_x / 10) * 10
                y2 = round(mouse_y / 10) * 10



            square_vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
            print(square_vertices)
            isometric_vertices = []
            for x, y in square_vertices:
                new_x = 2*(x * cos_angle - y * sin_angle)/sqrt_2
                new_y = (x * sin_angle + y * cos_angle)/sqrt_2
                isometric_vertices.append((round(new_x), round(new_y)))

            # print(isometric_vertices)

            # print(square_vertices)



        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                upper_left_vertex_drag = not upper_left_vertex_drag
            if event.key == pygame.K_1:
                square_type = "floor"
            elif event.key == pygame.K_2:
                square_type = "npc"
            elif event.key == pygame.K_3:
                square_type = "door"
            elif event.key == pygame.K_4:
                square_type = "player"
            elif event.key == pygame.K_n:
                if square_type == "player":
                    continue
                final_squares.append(square_vertices)
                final_isometrics.append(isometric_vertices)
                final_types.append(square_type)
                continue
            elif event.key == pygame.K_b:
                final_squares.pop()
                final_isometrics.pop()
                final_types.pop()
                continue
            



    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

    for i, (x, y) in enumerate(isometric_vertices, start=1):
        text_surface = font.render(str(i), True, (0, 0, 0))  
        text_rect = text_surface.get_rect(center=(x, y - 15)) 
        screen.blit(text_surface, text_rect)

    for i, (x, y) in enumerate(square_vertices, start=1):
        text_surface = font.render(str(i), True, (0, 0, 0))  
        text_rect = text_surface.get_rect(center=(x, y - 15))  
        screen.blit(text_surface, text_rect)


    pygame.draw.polygon(screen, (255, 0, 0), isometric_vertices, 2)
    pygame.draw.polygon(screen, (255, 0, 0), square_vertices, 2)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)  
    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)

    for item_type, v in zip(final_types, final_squares):
        if item_type == "floor":
            color = (0, 255, 0)
        elif item_type == "npc":
            color = (255, 0, 255)
        elif item_type == "door":
            color = (0, 0, 255)
        pygame.draw.polygon(screen, color, v, 2)  
    for item_type, v in zip(final_types, final_isometrics):
        if item_type == "floor":
            color = (0, 255, 0)
        elif item_type == "npc":
            color = (255, 0, 255)
        elif item_type == "door":
            color = (0, 0, 255)
        pygame.draw.polygon(screen, color, v, 2)  

    if upper_left_vertex_drag:
        pygame.draw.circle(screen, (0, 0, 0), (x1, y1), 5)
    else:
        pygame.draw.circle(screen, (0, 0, 0), (x2, y2), 5)

    
    text_surface = font.render(square_type, True, (0, 0, 0))  
    text_rect = text_surface.get_rect(center=(100, 100)) 
    screen.blit(text_surface, text_rect)

    pygame.display.flip()

    clock.tick(60)


# salvar aqui num txt

file_path = f"assets/{img_name}.txt"

# Open the file in write mode
with open(file_path, "w") as file:

    file.write("squares\n")
    for item_type, item in zip(final_types, final_squares):
        file.write(item_type + " ")
        file.write(str(item) + "\n")

    file.write("\nisometrics\n")
    for item_type, item in zip(final_types, final_isometrics):
        file.write(item_type + " ")
        file.write(str(item) + "\n")

    file.write("\nsquare_point\n")
    file.write(str(square_point) + "\n")

    file.write("\nisometric_point\n")
    file.write(str(isometric_point) + "\n")


pygame.quit()
sys.exit()
