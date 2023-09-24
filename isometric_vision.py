import pygame
import sys
import math

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unfilled Triangle Drawing")

x1 = 100+200
x2 = 400+200
y1 = 200
y2 = 500

isometric_x_distance = 2*(x2-x1) + 50
# isometric_x_distance = 0

walker_x = x1
walker_y = y1
new_walker_x = 0
new_walker_y = 0


clock = pygame.time.Clock()

velocity = 4

vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

angle = math.radians(45)
sin_angle = math.sin(angle)
cos_angle = math.cos(angle)

vertices_2 = []
for x, y in vertices:
    new_x = 2*(x * cos_angle - y * sin_angle)/math.sqrt(2)
    new_y = 2*(x * sin_angle + y * cos_angle)/math.sqrt(2)
    vertices_2.append((new_x, new_y))


vertices_2 = [(x + isometric_x_distance, y/2) for x, y in vertices_2]


isometric_walker_x = vertices_2[0][0]
isometric_walker_y = vertices_2[0][1]
isometric_new_walker_x_h = 0
isometric_new_walker_y_h = 0
isometric_new_walker_x_v = 0
isometric_new_walker_y_v = 0


outline_color = (255, 0, 0)  # Red color (RGB)
outline_color_2 = (255, 0, 255)  # Red color (RGB)
outline_thickness = 2  # Thickness of the outline

font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        new_walker_x = -velocity
        isometric_new_walker_x_h = -velocity
        isometric_new_walker_y_h = -velocity * 0.5
    if keys[pygame.K_RIGHT]:
        new_walker_x = +velocity
        isometric_new_walker_x_h = +velocity
        isometric_new_walker_y_h = +velocity * 0.5
    if keys[pygame.K_UP]:
        new_walker_y = -velocity
        isometric_new_walker_x_v = +velocity
        isometric_new_walker_y_v = -velocity * 0.5
    if keys[pygame.K_DOWN]:
        new_walker_y = +velocity
        isometric_new_walker_x_v = -velocity
        isometric_new_walker_y_v = +velocity * 0.5

    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and x1 <= walker_x + new_walker_x <= x2:
        walker_x += new_walker_x
        isometric_walker_x += isometric_new_walker_x_h
        isometric_walker_y += isometric_new_walker_y_h
    if (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and y1 <= walker_y + new_walker_y <= y2:
        walker_y += new_walker_y
        isometric_walker_x += isometric_new_walker_x_v
        isometric_walker_y += isometric_new_walker_y_v
    
    

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black to clear the screen

    # Draw the unfilled triangle

    for i, (x, y) in enumerate(vertices, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  # Render the vertex number
        text_rect = text_surface.get_rect(center=(x, y - 15))  # Position the number above the vertex
        screen.blit(text_surface, text_rect)

    for i, (x, y) in enumerate(vertices_2, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  # Render the vertex number
        text_rect = text_surface.get_rect(center=(x, y - 15))  # Position the number above the vertex
        screen.blit(text_surface, text_rect)


    pygame.draw.polygon(screen, outline_color, vertices, outline_thickness)
    pygame.draw.polygon(screen, outline_color_2, vertices_2, outline_thickness)
    pygame.draw.circle(screen, (0, 255, 0), (walker_x, walker_y), 5)  # Red point at walker's position
    pygame.draw.circle(screen, (0, 255, 255), (isometric_walker_x, isometric_walker_y), 5)  # Red point at walker's position

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
