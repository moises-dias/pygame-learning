
class PlayerSprite:
    # condições:
    # imagem de 800*1600
    # 8 frames por tipo de movimento
    # 8 colunas e 16 linhas
    # as primeiras 8 linhas devem ser: S,O,E,N,SO,NO,SE,NE idle
    # as ultimas 8 linhas devem ser: S,O,E,N,SO,NO,SE,NE andando
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        self.offset_x = 50
        self.offset_y = 80
        self.frame_w = 100
        self.frame_h = 100
        self.direction = "S"
        self.walking = False
        self.tick_count = 0
        self.tick_per_frame = 5
        self.current_frame = 0
        self.max_frame = 8

        self.direction_dict_sprite = {
            "S": 0,
            "O": 1,
            "E": 2,
            "N": 3,
            "SO": 4,
            "NO": 5,
            "SE": 6,
            "NE": 7,
        }

    def get_image(self):
        cropped_image = self.sprite_sheet.subsurface(
            (
                self.current_frame * self.frame_w, 
                (self.direction_dict_sprite[self.direction] * self.frame_h) + (8 * self.walking * self.frame_h), 
                self.frame_w, 
                self.frame_h
            )
        )
        return cropped_image

    def update(self, direction, walking):
        self.tick_count += 1

        # TODO nao mudar current_frame e tick_count se mudar de direcao sem parar de andar?
        if self.direction != direction:
            self.direction = direction
        
        if self.walking != walking:
            self.walking = walking
            self.tick_count = 0
            self.current_frame = 0

        elif self.tick_count >= self.tick_per_frame:
            self.tick_count = 0
            self.current_frame += 1
            if self.current_frame >= self.max_frame:
                self.current_frame = 0
