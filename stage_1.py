import pygame

from floor_1 import Floor1

class Stage1:
    def __init__(self):
        self.floor = Floor1()
        self.starting_position = [690, 160]
        self.isometric_starting_position = [530, 425]

        self.map_image = pygame.image.load("assets/simple_isometric.png")
        self.map_image_rect = self.map_image.get_rect()
