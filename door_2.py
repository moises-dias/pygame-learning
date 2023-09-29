from door_sprite import DoorSprite
import math
class Door2:
    def __init__(self, spriteflyweight):
        self.square = [(620, -40), (620, 0), (640, 0), (640, -40)]
        self.isometric_square = [(660, 290), (620, 310), (640, 320), (680, 300)]
        self.sprite = DoorSprite("SE", spriteflyweight.get_image("assets/arrows.png"))
        # TODO onde deixar a instrucao abaixo? padronizar um alpha?
        self.sprite.sprite_sheet.set_colorkey((255, 255, 255))
        self.sprite_position = [650, 300]
        self.current_angle = 0
        self.next_room = "room1"

        #TODO se isso for existir, deixar na main ou numa classe pai, pra ser chamado uma vez só, e nao instanciar em toda porta
        self.sine_values = []
        for angle in range(360):
            radians = math.radians(angle)
            sine_value = math.sin(radians)
            self.sine_values.append(sine_value)

    def update(self):
        # TODO se for usar só de 10 em 10 colocar só esses na lista, e não todos
        self.current_angle = (self.current_angle + 10) % 360
        self.sprite_position = [
            self.sprite_position[0] + self.sine_values[self.current_angle] * 0.8, 
            self.sprite_position[1] + self.sine_values[self.current_angle] * 0.4 
        ]