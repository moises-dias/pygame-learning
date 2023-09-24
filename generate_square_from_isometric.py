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
desired = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]


clock = pygame.time.Clock()

angle = math.radians(-45)
sin_angle = math.sin(angle)
cos_angle = math.cos(angle)

# isometric_vertices = [(490, 285), (200, 430), (430, 545), (720, 400)]
isometric_vertices = [(750.0, 250.0), (450.0, 400.0), (750.0, 550.0), (1050.0, 400.0)]


square_vertices = []
for x, y in isometric_vertices:

    x = x*math.sqrt(2)
    y = y*math.sqrt(2)
    new_x = (x/2 * cos_angle - y * sin_angle)
    new_y = (x/2 * sin_angle + y * cos_angle)
    square_vertices.append((new_x, new_y))

square_vertices = [(x,  y + 300) for x, y in square_vertices]
print(square_vertices)


font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black to clear the screen

    # Draw the unfilled triangle

    for i, (x, y) in enumerate(square_vertices, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  # Render the vertex number
        text_rect = text_surface.get_rect(center=(x, y - 15))  # Position the number above the vertex
        screen.blit(text_surface, text_rect)

    for i, (x, y) in enumerate(isometric_vertices, start=1):
        text_surface = font.render(str(i), True, (255, 255, 255))  # Render the vertex number
        text_rect = text_surface.get_rect(center=(x, y - 15))  # Position the number above the vertex
        screen.blit(text_surface, text_rect)


    pygame.draw.polygon(screen, (255, 0, 0), isometric_vertices, 2)
    pygame.draw.polygon(screen, (255, 0, 0), square_vertices, 2)
    pygame.draw.polygon(screen, (255, 255, 255), desired, 2)

    # Update the display
    pygame.display.flip()

    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
