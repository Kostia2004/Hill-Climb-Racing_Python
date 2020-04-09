import pygame
import sys
from Racquet import Racquet

pygame.init()                           #initialization 

def main():   
    root = pygame.display.set_mode((600, 400)) #create window
    pygame.display.set_caption("Pong")  #title of window

    #first racket initialization:
    RacquetA = Racquet((255, 255, 255), 10, 80)
    RacquetA.rect.x = 20
    RacquetA.rect.y = 160

    #second racket initialization:
    RacquetB = Racquet((255, 255, 255), 10, 80)
    RacquetB.rect.x = 570
    RacquetB.rect.y = 160

    #list that will contain all the sprites to use in game:
    all_sprites_list = pygame.sprite.Group()
 
    # Add the paddles to the list of sprites
    all_sprites_list.add(RacquetA)
    all_sprites_list.add(RacquetB)
    
    clock = pygame.time.Clock()         #clock object initialization

    FPS = 80                            #frame rate

    while True:                         #main program cycle
        for i in pygame.event.get():    #scrolling event list
            if i.type == pygame.QUIT:
                pygame.quit()           #program stop
                sys.exit()              #close window

        #clear the screen to black: 
        root.fill((0,0,0))
        
        #Draw the net:
        pygame.draw.line(root, (255, 255, 255), [299, 0], [299, 400], 1)

        #Draw game objects from the list of sprites
        all_sprites_list.draw(root) 

        # Go ahead and update the screen:
        pygame.display.flip()

        clock.tick(FPS)                 #frame rate setting


if __name__=="__main__":
    main()
