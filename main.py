import pygame
import sys

pygame.init() #initialization 
 
pygame.display.set_mode((600, 400)) #create window

while True:                         #main program cycle
    for i in pygame.event.get():    #scrolling event list
        if i.type == pygame.QUIT:
            pygame.quit()           #program stop
            sys.exit()              #close window
