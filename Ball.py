import pygame
import random
 
class Ball(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height, sc):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent

        self.image = pygame.Surface([width, height])
        self.image.fill((0,0,0))
        self.image.set_colorkey((0,0,0))
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        
        self.velocity = [random.randint(3,7),random.randint(-9,9)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-8,8)
