import pygame
import sys
from Racquet import Racquet
from Ball import Ball

pygame.init()                           #initialization 

Up = 1
Down = 0

score =[0, 0]

def main():   
    root = pygame.display.set_mode((600, 455)) #create window
    pygame.display.set_caption("Pong")  #title of window

    #list that will contain all the sprites to use in game:
    all_sprites_list = pygame.sprite.Group()
    
    #first racket initialization:
    RacquetA = Racquet((0, 255, 255), 10, 80)
    RacquetA.rect.x = 20
    RacquetA.rect.y = 187
    all_sprites_list.add(RacquetA)

    #second racket initialization:
    RacquetB = Racquet((255, 0, 255), 10, 80)
    RacquetB.rect.x = 570
    RacquetB.rect.y = 187
    all_sprites_list.add(RacquetB)

    #ball initialization:
    ball = Ball((255, 255, 255),10,10,root)
    ball.rect.x = 295
    ball.rect.y = 195
    all_sprites_list.add(ball)
    
    
    clock = pygame.time.Clock()         #clock object initialization

    FPS = 60                           #frame rate

    while True:                         #main program cycle
        for i in pygame.event.get():    #scrolling event list
            if i.type == pygame.QUIT:
                pygame.quit()           #program stop
                sys.exit()              #close window

        #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            RacquetA.move(5, Up)
        if keys[pygame.K_s]:
            RacquetA.move(5, Down)
        if keys[pygame.K_UP]:
            RacquetB.move(5, Up)
        if keys[pygame.K_DOWN]:
            RacquetB.move(5, Down)    
 
        # --- Game logic should go here
        all_sprites_list.update()

        #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=590:
            ball.velocity[0] = -ball.velocity[0]
            score[0]+=1
            print(score[0], '|', score[1]) 
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
            score[1]+=1
            print(score[0], '|', score[1]) 
        if ball.rect.y>=445:
            ball.rect.y=445
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<=55:
            ball.rect.y=55
            ball.velocity[1] = -ball.velocity[1] 

        #Detect collisions between the ball and the racquets
        if pygame.sprite.collide_mask(ball, RacquetA):
            ball.bounce(True)
        elif pygame.sprite.collide_mask(ball, RacquetB):
            ball.bounce(False)
        
        #clear the screen to black: 
        root.fill((0,0,0))
        
        #Draw the net:
        pygame.draw.line(root, (255, 255, 255), [299, 0], [299, 455], 1)
        pygame.draw.line(root, (255, 255, 255), [0, 55], [599, 55], 1)

        #Draw game objects from the list of sprites
        all_sprites_list.draw(root) 

        #Display scores:
        font = pygame.font.Font(None, 74)
        if score[0]<1000:
            text = font.render(str(score[0]), 1, (0, 255, 255))
            root.blit(text, (125,5))
        else:
            text = font.render(str(score[0]), 1, (0, 255, 255))
            root.blit(text, (75,5))
        if score[1]<1000:
            text = font.render(str(score[1]), 1, (255, 0, 255))
            root.blit(text, (425,5))
        else:
            text = font.render(str(score[1]), 1, (255, 0, 255))
            root.blit(text, (375,5))

        # Go ahead and update the screen:
        pygame.display.flip()

        clock.tick(FPS)                 #frame rate setting


if __name__=="__main__":
    main()
