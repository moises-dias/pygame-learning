
class PlayerSprite:
    def __init__(self, sprite_sheet):
        self.sprite_sheet = sprite_sheet
        self.offset_x = 50
        self.offset_y = 80

    def get_image(self):
        cropped_image = self.sprite_sheet.subsurface((0, 0, 100, 100))
        return cropped_image

    # def clear_images(self):
    #     self.images.clear()

