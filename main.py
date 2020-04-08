import pygame
import sys

pygame.init()                           #initialization 

def main():   
    pygame.display.set_mode((600, 400)) #create window

    clock = pygame.time.Clock()         #clock object initialization

    FPS = 80                            #frame rate

    while True:                         #main program cycle
        for i in pygame.event.get():    #scrolling event list
            if i.type == pygame.QUIT:
                pygame.quit()           #program stop
                sys.exit()              #close window
        clock.tick(FPS)                 #frame rate setting
if __name__=="__main__":
    main()
