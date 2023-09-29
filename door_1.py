from door_sprite import DoorSprite
import math
class Door1:
    def __init__(self, spriteflyweight):
        self.square = [(530, 230), (530, 320), (580, 320), (580, 230)]
        self.isometric_square = [(300, 380), (210, 425), (260, 450), (350, 405)]
        self.sprite = DoorSprite(spriteflyweight.get_image("assets/arrows.png"))
        # TODO onde deixar a instrucao abaixo? padronizar um alpha?
        self.sprite.sprite_sheet.set_colorkey((255, 255, 255))
        self.sprite_position = [190, 330]
        self.current_angle = 0

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