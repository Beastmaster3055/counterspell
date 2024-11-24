# import the pygame module 
import pygame 
import time

# music stuff
import threading  # For background thread to play music
from pygame import mixer
pygame.mixer.init()

playlist = [
    "C:\Codingstuff\Counterspell\Game\Faultlines - Asher Fulero.mp3",
    "C:\Codingstuff\Counterspell\Game\Lake Jupiter - John Patitucci.mp3",
    "C:\Codingstuff\Counterspell\Game\AETHER - Density & Time.mp3",
    "C:\Codingstuff\Counterspell\Game\EBB - Density & Time.mp3",
    "C:\Codingstuff\Counterspell\Game\Maestro Tlakaelel - Jesse Gallagher.mp3"
]

def play_playlist():
    current_song_index = 0

    while True:
        try:
            # Load and play the current song
            pygame.mixer.music.load(playlist[current_song_index])
            pygame.mixer.music.play()

            # Wait until the current song finishes
            while pygame.mixer.music.get_busy():
                time.sleep(1)

            # Move to the next song, or loop back to the first
            current_song_index = (current_song_index + 1) % len(playlist)

        except pygame.error as e:
            print(f"Error loading or playing song: {e}")

music_thread = threading.Thread(target=play_playlist, daemon=True)
music_thread.start()

SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 1000

def GenerateLevel(level):
    global text_surface
    global text_surface2
    my_font = pygame.font.SysFont('Bokor', 30)
    hint = pygame.font.SysFont('Bokor', 30)
    if level == 1:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,0,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        text_surface = my_font.render("This is you and your shadow, he's evil, try to get rid of him.", False, (0, 0, 0))
        text_surface2 = hint.render("Maybe get him off of the platform, but he copies all of your moves.", False, (0,0,0))
    if level == 2:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        text_surface = my_font.render("Good job, you figured out how to use the void", False, (0, 0, 0))
        text_surface2 = hint.render("There are many different ways to desync the shadow's movements.", False, (0,0,0))
    if level == 3:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,0,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        text_surface = my_font.render("He will try to copy most moves, but can't restrict your movements.", False, (0, 0, 0))
        text_surface2 = hint.render("So when he does, he may fall by himself (definitely not a coding bug)", False, (0,0,0))
    if level == 4:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [1,1,1,1,1,0,1,0,1,1,1,1,0,1],
            [1,1,1,1,1,0,1,0,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        text_surface = my_font.render("Be careful when trying to get him, you may fall yourself.", False, (0, 0, 0))
        text_surface2 = hint.render("If he takes you with him, you still lose.", False, (0,0,0))
    if level == 5:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,1,1,1,1,2,1,2,1,1,1,1,0,1,2,1,0,1,1,2,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
        text_surface = my_font.render("FINAL LEVEL BECAUSE I'M RUNNING OUT OF TIME", False, (0, 0, 0))
        text_surface2 = hint.render("oh yeah don't touch the red stuff.", False, (0,0,0))
    if level == 6:
        platforms_map = [
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1]]
        text_surface = my_font.render("did you cheese the last level", False, (0, 0, 0))
        text_surface2 = hint.render("anyway thanks for playing, this was made by roger and ayaan, you can close this now!", False, (0,0,0))
    platforms_list = []
    kill_blocks = []
    for i in range(len(platforms_map)):
        for j in range(len(platforms_map[i])):
            if platforms_map[i][j] == 1:
                platforms_list.append(Obstacle(j*100,i*100,1))
            elif platforms_map[i][j] == 2:
                kill_blocks.append(Obstacle(j*100,i*100,1))
    return platforms_list,kill_blocks

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) 
        pygame.display.set_caption("Shadow's Path") 
        self.camx = -200

class Obstacle: # types = [1=platform,2=lava,3=spike,4=button,5=decoration]
    def __init__(self,x,y,id):
        self.info = pygame.Rect(x,y,100,100)
        self.ox = x # original x
        self.oy = y # original y
        self.id = id

class Character:
    def __init__(self,x,y):
        self.info = pygame.Rect(x,y,50,50)
        self.yvelocity = 0
        self.xvelocity = 0
        self.jumping = False

player = Character(400,SCREEN_HEIGHT/2-150)
shadow = Character(400,SCREEN_HEIGHT/2+100)
world = Game()
level = 1
level_generated = False

# GAME LOOP
running = True
while running: 
    # SETUP
    if level_generated == False:
        platforms_list,kill_blocks = GenerateLevel(level)
        level_generated = True
        player.yvelocity = 0
        player.xvelocity = 0
        player.info.y = SCREEN_HEIGHT/2-150

        shadow.yvelocity = 0
        shadow.xvelocity = 0
        shadow.info.y = SCREEN_HEIGHT/2+100
        world.camx = -200
    key = pygame.key.get_pressed()
    world.screen.fill((180,190,255))
    time.sleep(.01)

    # MOVEMENT
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        if player.xvelocity > -10:
            player.xvelocity -= 2
        if shadow.xvelocity > -10:
            shadow.xvelocity -= 2
    if key[pygame.K_d] or key[pygame.K_RIGHT]:
        if player.xvelocity < 10:
            player.xvelocity += 2
        if shadow.xvelocity < 10:
            shadow.xvelocity += 2

    if key[pygame.K_w] or key[pygame.K_SPACE] or key[pygame.K_UP]:
        if player.yvelocity == 0 and player.jumping == False:
            player.yvelocity = -20
            player.jumping = True
        if shadow.yvelocity == 0 and shadow.jumping == False:
            shadow.yvelocity = 20
            shadow.jumping = True

    player.yvelocity += 1
    shadow.yvelocity -= 1

    # COLLISIONS
    new_x = player.info.left + player.xvelocity
    new_y = player.info.top + player.yvelocity
    for platform in platforms_list:
        if platform.info.colliderect(new_x,player.info.y,player.info.width,player.info.height):
            if player.xvelocity != 0:
                player.xvelocity = 0
        if platform.info.colliderect(player.info.left,new_y,player.info.width,player.info.height):
            if player.yvelocity > 0:
                player.info.y += platform.info.top - player.info.bottom
                player.yvelocity = 0
                player.jumping = False
            elif player.yvelocity < 0:
                player.info.y += player.info.top - platform.info.bottom
                player.yvelocity = 0
        else:
            jumping = True

    # SHADOW COLLISIONS
    new_x = shadow.info.left + shadow.xvelocity
    new_y = shadow.info.top + shadow.yvelocity
    for platform in platforms_list:
        if platform.info.colliderect(new_x,shadow.info.y,shadow.info.width,shadow.info.height):
            if shadow.xvelocity != 0:
                shadow.xvelocity = 0
        if platform.info.colliderect(shadow.info.left,new_y,shadow.info.width,shadow.info.height):
            if shadow.yvelocity < 0:
                shadow.info.y += shadow.info.top - platform.info.bottom
                shadow.yvelocity = 0
                shadow.jumping = False
            elif shadow.yvelocity > 0:
                shadow.info.y += shadow.info.bottom - platform.info.top
                shadow.yvelocity = 0
        else:
            jumping = True

    # UPDATING PLATFORMS
    world.camx += player.xvelocity
    for platform in platforms_list:
        platform.info.x = platform.ox - world.camx
    for kill_block in kill_blocks:
        if player.info.colliderect(kill_block.info):
            world.camx = -200
            player.yvelocity = 0
            player.xvelocity = 0
            player.info.y = SCREEN_HEIGHT/2-150

            shadow.yvelocity = 0
            shadow.xvelocity = 0
            shadow.info.y = SCREEN_HEIGHT/2+100
        kill_block.info.x = kill_block.ox - world.camx

    # UPDATING PLAYER
    player.info.y += player.yvelocity

    # UPDATING SHADOW
    shadow.info.y += shadow.yvelocity

    # PLAYER X FRICTION
    if player.xvelocity < 0:
        player.xvelocity += 1
    elif player.xvelocity > 0:
        player.xvelocity -= 1
    
    # SHADOW X FRICTION
    if shadow.xvelocity < 0:
        shadow.xvelocity += 1
    elif shadow.xvelocity > 0:
        shadow.xvelocity -= 1
    
    # WIN CONDITION
    if shadow.info.y < -6400:
        level += 1
        level_generated = False

    # DRAWING PLAYERS
    pygame.draw.rect(world.screen,(255,0,0),player.info)
    pygame.draw.rect(world.screen,(0,0,0),shadow.info)
    # DRAWING PLATFORMS
    for platform in platforms_list:
        pygame.draw.rect(world.screen,(50,50,50),platform.info)
    for kill_block in kill_blocks:
        pygame.draw.rect(world.screen,(255,0,0),kill_block.info)
        
    # TEXT

    world.screen.blit(text_surface, (300-world.camx,100))
    world.screen.blit(text_surface2, (300-world.camx,150))
    
    # RESPAWN
    if key[pygame.K_r] == True or player.info.y > 800:
        world.camx = -200
        player.yvelocity = 0
        player.xvelocity = 0
        player.info.y = SCREEN_HEIGHT/2-150

        shadow.yvelocity = 0
        shadow.xvelocity = 0
        shadow.info.y = SCREEN_HEIGHT/2+100
   
    for event in pygame.event.get(): 
             
        if event.type == pygame.QUIT: 
            running = False

    pygame.display.update()