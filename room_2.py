from floor_2 import Floor2
from door_2 import Door2

class Room2:
    def __init__(self, spriteflyweight):
        self.floor = Floor2()
        self.doors = [
            Door2(spriteflyweight)
        ]
        self.starting_position = [590, -30]
        self.isometric_starting_position = [620, 280]
        self.starting_direction = "NO"

        self.map_image = spriteflyweight.get_image("assets/isometric2.jpg")
        self.map_image_rect = self.map_image.get_rect()

        self.to_draw = []
        self.next_room = None

    #TODO colide com jogadores e portas
    def update(self, player_pos):
        self.to_draw = []
        self.next_room = None

        for door in self.doors:
            x1 = door.square[0][0]
            y1 = door.square[0][1]
            x2 = door.square[2][0]
            y2 = door.square[2][1]

            if  x1 <= player_pos[0] <= x2 and y1 <= player_pos[1] <= y2:
                
                door.update()
                self.to_draw.append({"img": door.sprite.get_image(), "pos": door.sprite_position})
                self.next_room = door.next_room
                break