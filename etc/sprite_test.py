import pygame
import sys

# Initialize Pygame
pygame.init()

# Load the image
image = pygame.image.load("assets/player.jpg")

# Create a Pygame window
window_width = 800
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))

# Define the initial rectangle size and position
rect_width = 100
rect_height = 100
rect_x = 0
rect_y = 0

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Set the scrolling speed (4 times per second)
scroll_speed = 4
scroll_distance = 100  # Pixels to scroll each step

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        rect_width -= 1
    if keys[pygame.K_RIGHT]:
        rect_width += 1
    if keys[pygame.K_UP]:
        rect_height -= 1
    if keys[pygame.K_DOWN]:
        rect_height +=1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the rectangle position
    rect_x += rect_width

    # If the rectangle is beyond the image width, reset it to the beginning
    if rect_x >= image.get_width():
        rect_x = 0
        rect_y += rect_height
        if rect_y >= image.get_height():
            rect_y = 0

    # Crop the portion of the image based on the rectangle position and size
    try:
        cropped_image = image.subsurface((rect_x, rect_y, rect_width, rect_height))
        # Display the cropped portion on the screen
        screen.blit(cropped_image, (0, 0))
    except:
        print("foo")


    pygame.display.flip()

    # Limit the frame rate
    clock.tick(20)  # 4 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
