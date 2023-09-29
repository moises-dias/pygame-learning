from room_1 import Room1
from room_2 import Room2

class RoomFactory:
    def __init__(self):
        self.room_mapping = {
            "room1": Room1,
            "room2": Room2
        }

    def create_room(self, room_name, sprite_flyweight):

        return self.room_mapping[room_name](sprite_flyweight)