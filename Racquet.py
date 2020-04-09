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
    def move(self, pix, destination):
        if destination==1:
            self.rect.y-=pix
            if self.rect.y<=0:
                self.rect.y=0
        if destination==0:
            self.rect.y+=pix
            if self.rect.y>320:
                self.rect.y=320
