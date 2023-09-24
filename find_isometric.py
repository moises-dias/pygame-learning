import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image with Lines")

# Load the image
image = pygame.image.load("isometric_test.png")  # Replace "your_image.png" with your image file path
image_rect = image.get_rect()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Lines to be drawn
draw_lines = False
line1_start = line1_end = line2_start = line2_end = (0, 0)

x1 = 100
x2 = 400
y1 = 200
y2 = 400



walker_x = x1
walker_y = y1
new_walker_x = 0
new_walker_y = 0


clock = pygame.time.Clock()

vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]

angle = math.radians(45)
sin_angle = math.sin(angle)
cos_angle = math.cos(angle)

vertices_2 = []
for x, y in vertices:
    new_x = 2*(x * cos_angle - y * sin_angle)/math.sqrt(2)
    new_y = 2*(x * sin_angle + y * cos_angle)/math.sqrt(2)
    vertices_2.append((new_x, new_y))
vertices_2 = [(x + 500, 100 + y/2) for x, y in vertices_2]
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                x1 -= 10
            elif event.key == pygame.K_w:
                y1 -= 10
            elif event.key == pygame.K_e:
                x2 += 10
            elif event.key == pygame.K_r:
                y2 += 10
            elif event.key == pygame.K_a:
                x1 += 10
            elif event.key == pygame.K_s:
                y1 += 10
            elif event.key == pygame.K_d:
                x2 -= 10
            elif event.key == pygame.K_f:
                y2 -= 10
            
            vertices = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
            vertices_2 = []
            for x, y in vertices:
                new_x = 2*(x * cos_angle - y * sin_angle)/math.sqrt(2)
                new_y = 2*(x * sin_angle + y * cos_angle)/math.sqrt(2)
                vertices_2.append((new_x, new_y))
            vertices_2 = [(x + 500, 100 + y/2) for x, y in vertices_2]

    # Clear the screen
    screen.fill(white)

    # Blit the image onto the screen
    screen.blit(image, image_rect)
    pygame.draw.polygon(screen, (255, 0, 255), vertices, 2)
    pygame.draw.polygon(screen, (255, 0, 255), vertices_2, 2)

    # Draw the lines if draw_lines is True



    # Update the screen
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
