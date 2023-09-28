class DoorSprite:
    # condições:
    # imagem de 800*1600
    # 8 frames por tipo de movimento
    # 8 colunas e 16 linhas
    # as primeiras 8 linhas devem ser: S,O,E,N,SO,NO,SE,NE idle
    # as ultimas 8 linhas devem ser: S,O,E,N,SO,NO,SE,NE andando
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        self.offset_x = 0
        self.offset_y = 0
        self.frame_w = 90
        self.frame_h = 70
        self.direction = "NO"
        self.tick_count = 0

        # colocar aqui pra onde aponta a seta
        self.direction_dict_sprite = {
            "S": (50, 80, self.frame_w, self.frame_h),
            "O": (50, 80, self.frame_w, self.frame_h),
            "E": (50, 80, self.frame_w, self.frame_h),
            "N": (50, 80, self.frame_w, self.frame_h),
            "SO": (50, 80, self.frame_w, self.frame_h),
            "NO": (50, 80, self.frame_w, self.frame_h),
            "SE": (50, 80, self.frame_w, self.frame_h),
            "NE": (50, 80, self.frame_w, self.frame_h)
        }

    def get_image(self):
        #TODO testar *unpack aqui
        cropped_image = self.sprite_sheet.subsurface(
            (
                self.direction_dict_sprite[self.direction][0], 
                self.direction_dict_sprite[self.direction][1], 
                self.direction_dict_sprite[self.direction][2], 
                self.direction_dict_sprite[self.direction][3]
            )
        )
        return cropped_image

    def update(self):
        self.tick_count += 1
        # atualizar o offset aqui dependendo do tick? efeito da seta se mover
