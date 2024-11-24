# import the pygame module 
import pygame 
import time

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 1020
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
  
# Set the caption of the screen 
pygame.display.set_caption("Shadow's Path") 

player = pygame.Rect(400,SCREEN_HEIGHT/2-150,50,50)
shadow = pygame.Rect(400,SCREEN_HEIGHT/2+100,50,50)
platform1 = pygame.Rect(0,SCREEN_HEIGHT/2-100,800,200)
platform2 = pygame.Rect(900,SCREEN_HEIGHT/2-100,200,200)

# Variable to keep our game loop running 
running = True
yvelocity = 0
xvelocity = 0
camx = 0
player.move_ip(0,yvelocity)
# game loop 
while running: 
    # velocity and movement
    key = pygame.key.get_pressed()
    screen.fill(background_colour)
    time.sleep(.01)
    if platform2.colliderect(player) == False and platform1.colliderect(player) == False:
        yvelocity += 1
    else:
        yvelocity = 0
        if key[pygame.K_w] == True:
            yvelocity = -20
    camx += xvelocity
    platform1.x = -camx
    platform2.x = 900-camx
    player.y += yvelocity
    if xvelocity < 0:
        xvelocity += .25
    elif xvelocity > 0:
        xvelocity -= .25
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,0,0),shadow)
    pygame.draw.rect(screen,(50,50,50),platform1)
    pygame.draw.rect(screen,(50,50,50),platform2)
    if key[pygame.K_a] == True and xvelocity > -10:
        xvelocity -= .5
    if key[pygame.K_d] == True and xvelocity < 10:
        xvelocity += .5
    if key[pygame.K_r] == True or player.y > 800:
        yvelocity = 0
        xvelocity = 0
        player.x = 400
        player.y = SCREEN_HEIGHT/2-150
    # now draw the shadow to be mirrored of the player
    shadow.x = player.x
    shadow.y = SCREEN_HEIGHT/2+((SCREEN_HEIGHT/2)-player.y)-50
    # generate obstacles?
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()