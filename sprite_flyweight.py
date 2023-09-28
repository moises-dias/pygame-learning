import pygame

class SpriteFlyweight:
    images = {}

    def get_image(self, image_path):
        if image_path in self.images:
            return self.images[image_path]

        image = pygame.image.load(image_path)
        self.images[image_path] = image
        return image

    def clear_images(self):
        self.images.clear()

