from door_sprite import DoorSprite

class Door1:
    def __init__(self, spriteflyweight):
        self.square = [(530, 230), (530, 320), (580, 320), (580, 230)]
        self.isometric_square = [(300, 380), (210, 425), (260, 450), (350, 405)]
        self.sprite = DoorSprite(spriteflyweight)

    def update(self):
        pass
