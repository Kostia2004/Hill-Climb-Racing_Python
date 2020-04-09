from pygame import *

class Racquet(sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        #background:
        self.image = Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))

        #racquet:
        draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
