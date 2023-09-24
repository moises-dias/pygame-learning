import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Unfilled Triangle Drawing")

# Define the triangle's properties (vertices)

x1 = 200
x2 = 400
y1 = 200
y2 = 400

isometric_x_distance = 2*(x2-x1) + 50
# isometric_x_distance = 0

walker_x = x1 + (x2-x1)/2
walker_y = y1 + (y2-y1)/2
new_walker_x = 0
new_walker_y = 0

isometric_walker_x = isometric_x_distance  + (x2-x1)
isometric_walker_y = y1 + (y2-y1)/2
isometric_new_walker_x = 0
isometric_new_walker_y = 0

clock = pygame.time.Clock()




vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
vertices_2 = []
vertices_2.append((x1, y1))
vertices_2.append((x1 - (x2-x1), y2 - (y2-y1)/2))
vertices_2.append((x1, y2))
vertices_2.append((x2, y2 - (y2-y1)/2))

vertices_2 = [(x + isometric_x_distance, y) for x, y in vertices_2]


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
        new_walker_x = walker_x - 2
        isometric_new_walker_x = isometric_walker_x - 2
        isometric_new_walker_y = isometric_walker_y - 1
    if keys[pygame.K_RIGHT]:
        new_walker_x = walker_x + 2
        isometric_new_walker_x = isometric_walker_x + 2
        isometric_new_walker_y = isometric_walker_y + 1
    if keys[pygame.K_UP]:
        new_walker_y = walker_y - 2
        isometric_new_walker_x = isometric_walker_x + 2
        isometric_new_walker_y = isometric_walker_y - 1
    if keys[pygame.K_DOWN]:
        new_walker_y = walker_y + 2
        isometric_new_walker_x = isometric_walker_x - 2
        isometric_new_walker_y = isometric_walker_y + 1

    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and x1 <= new_walker_x <= x2:
        walker_x = new_walker_x
        isometric_walker_x = isometric_new_walker_x
        isometric_walker_y = isometric_new_walker_y
    if (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and y1 <= new_walker_y <= y2:
        walker_y = new_walker_y
        isometric_walker_x = isometric_new_walker_x
        isometric_walker_y = isometric_new_walker_y
    
    

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
