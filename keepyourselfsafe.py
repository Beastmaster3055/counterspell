# import the pygame module 
import pygame 
import time

# Define the background colour 
# using RGB color coding. 
background_colour = (234, 212, 252) 
  
# Define the dimensions of 
# screen object(width,height) 
screen = pygame.display.set_mode((800,600)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Buckshot roulette') 

# Update the display using flip 
pygame.display.flip() 

player = pygame.Rect(200,200,50,50)
surface = pygame.Rect(0,400,800,200)

# Variable to keep our game loop running 
running = True
yvelocity = 0
xvelocity = 0
# game loop 
while running: 
    screen.fill(background_colour)
    time.sleep(.01)
    if player.colliderect(surface) == False:
        yvelocity += 1
    else:
        yvelocity = 0
        if key[pygame.K_w] == True:
            yvelocity = -20
    player.move_ip(xvelocity,yvelocity)
    if xvelocity < 0:
        xvelocity += .25
    elif xvelocity > 0:
        xvelocity -= .25
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,0,0),surface)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and xvelocity > -10:
        xvelocity -= .5
    if key[pygame.K_d] == True and xvelocity < 10:
        xvelocity += .5
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()