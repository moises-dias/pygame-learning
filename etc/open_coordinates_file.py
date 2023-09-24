squares = []
isometrics = []
square_point = ()
isometric_point = ()

with open("output.txt", "r") as file: 
    current_section = None 

    for line in file:
        line = line.rstrip('\n')

        if line == "squares":
            current_section = "squares"
        elif line == "isometrics":
            current_section = "isometrics"
        elif line == "square_point":
            current_section = "square_point"
        elif line == "isometric_point":
            current_section = "isometric_point"
        elif line != "":
            if current_section == "squares":
                square_data = eval(line) 
                squares.append(square_data)
            elif current_section == "isometrics":
                isometric_data = eval(line)  
                isometrics.append(isometric_data)
            elif current_section == "square_point":
                square_point = eval(line) 
            elif current_section == "isometric_point":
                isometric_point = eval(line) 

print("squares:", squares)
print("isometrics:", isometrics)
print("square_point:", square_point)
print("isometric_point:", isometric_point)





import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
image = pygame.image.load("isometric_test.png")
image_rect = image.get_rect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill((0, 0, 0)) 
    screen.blit(image, image_rect)

 
    pygame.draw.circle(screen, (0, 255, 0), square_point, 5)
    pygame.draw.circle(screen, (0, 255, 0), isometric_point, 5)

    for v in isometrics:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  
    for v in squares:
        pygame.draw.polygon(screen, (0, 255, 0), v, 2)  


    pygame.display.flip()

    clock.tick(60)



pygame.quit()
sys.exit()
