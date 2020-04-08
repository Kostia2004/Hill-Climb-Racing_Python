import pygame
import sys
from tkinter import *

pygame.init()                           #initialization 

def main():   
    root = pygame.display.set_mode((700, 500)) #create window
    pygame.display.set_caption("Pong")  #title of window
    
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
        pygame.draw.line(root, (255, 255, 255), [349, 0], [349, 500], 5)

        # Go ahead and update the screen:
        pygame.display.flip()

        clock.tick(FPS)                 #frame rate setting


if __name__=="__main__":
    main()
