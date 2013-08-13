####################
#       __         #
# |\/| |  | |  | | #
# |  | |  | |  | | #
# |  | |__| |/\| . #
# v1.0 shareware   #
####################
# By        Orange #
#################################################################################
#                                                                               #
# You like mowing lawns?  Me neither!  But you'll love this!                    #
#                                                                               #
# Mow v1 shareware edition features lots of exciting features!                  #
#  o Mow lawns in the comfort of your own home!                                 #
#  o Lush realistic looking grass!                                              #
#    You can SMELL HOW FRESH IT THE GRASS CLIPPINGS ARE(results may vary)       #
#  o Realistic looking mower guy                                                #
#  o Based on a true story!                                                     #
#  o Screen shot feature lets you share your lawns with your friends!  Oh boy!  #
#  o And much much more!                                                        #
#                                                                               #
#   To purchase the full version of MOW!, Send $5(USD) to:                      #
#     246 Redvill View                                                          #
#     Fakeboro, OH                                                              #
#     09876                                                                     #
#                                                                               #
#   We offer MOW! as a 3.5" or 5.25" floppy diskette.  PLEASE SPECIFY!!!        #
#                                                                               #
#################################################################################
#
#   Objective:
#       Destroy all uncut grass
#   How?
#        Use your trusty lawn mower to decapitate the grass
#   HOW?!?
#       Arrow keys to move, jeez
#   Anything else?
#       Yeah.  F1 to take a picture.  F2 TO WIN(and not reset the grass)

import pygame
from pygame.locals import *

import sys
import os
import random

pygame.init()

#pygame.key.set_repeat(200,5) #lol makes it too easy

#For the alternationg captions
captions = ('Mow','By Orange',
            'Arrow keys to move',
            'Mow all the grass!',
            'F1 to take a screenshot',
            'F2 to reset lawn, or just mow it all',
            'You are on level LEVEL', #LEVEL gets replaced with the current level
            'Try to beat my high score of 3!')

cur_caption = 0 #What caption we are on
caption_delay = 200 #Delay variable
pygame.display.set_caption(captions[0]) #Set the caption to the first one

size = width,height = 512,512 #width=512, height=512.  size=(width,height)
fps = 60 #Frames per second

realscreen = pygame.display.set_mode(size) #The real screen the user sees
screen = pygame.Surface((256,256)) #The screen we draw to.  Gets doubled when put on real screen
clock  = pygame.time.Clock() #The clock for controlling FPS

#Loads an image from a string.  I don't want external files.
mowerright = pygame.image.fromstring('\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\x80\x00\xff\x80\x00\xff\x80\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\x80\x00\xff\x80\x00\xff\x80\x00\xff\x80\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\xff\x80\xff\xff\x80\xff\xff\x80\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\xff\x80\xff\xff\x80\xff\xff\x80\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\xff\x00\x00\xff\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\xff\xff\xff\x80\xff\xff\x80\xff\xff\x80\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\xff\x00\x00\xff\x00\xff\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x80\x00\x00\x80\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x80\x00\x00\x00\xff\x00\x80\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\xff\x00\x00\xff\x00\xc0\xc0\xc0\xff\xff\x80\x00\xff\x00\x00\xff\x00\xff\xff\x80\x00\xff\x00\x00\xff\x00\x00\xff\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xc0\xc0\xc0\xc0\xc0\xc0\x00\xff\x00\xff\xff\x80\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00',(16,16),'RGB')
mowerright.set_colorkey((0,255,0)) #Set transparency
mowerleft  = pygame.transform.flip(mowerright,1,0) #Flip the image for the other way

mower = [mowerleft,mowerright]
#mower[0] is the mower facing left
#mower[1] is the mower facing right


#Grass.  two diffrent colors for the stripe effect
grass_cut1 = pygame.Surface((16,16))
grass_cut1.fill((0,200,0))
grass_cut2 = pygame.Surface((16,16))
grass_cut2.fill((0,220,0))
grass_cut = (grass_cut1,grass_cut2)

grass_uncut = pygame.Surface((16,16))
grass_uncut.fill((0,255,0))

level = 1 #What level we are on.  a global variable.

def game():
    field = [ #0 means uncut grass.  1 means cut.
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
    
    playerx = 8
    playery = 8
    player_face = 1
    
    global captions,caption_delay,cur_caption #So we can change the caption vars
                                              #Within a function.
    while 1:
        #Handle the caption
        if caption_delay: #If delay not zero
            caption_delay-=1 #Subtract one, continue on
        else:
            cur_caption+=1#add one to the current caption
            if cur_caption==len(captions): #Loop to begining if on the last caption
                cur_caption=0
            #set the caption.  The string LEVEL gets replace by the variable level
            pygame.display.set_caption(captions[cur_caption].replace('LEVEL',str(level)))
            caption_delay = 200 #Reset caption delay
        
        for event in pygame.event.get(): #The all important event loop
            if event.type == QUIT: sys.exit() #When the user presses the X in the corner
            if event.type == KEYDOWN: #If user pressed a key
                if event.key == K_ESCAPE: sys.exit() #Exit is pressed Esc
                if event.key == K_F1: #F1 key
                    #Screen shot.
                    for i in range(9999): #See if file mow 0000.bmp exists.
                        path = os.path.join(os.getcwd(),'mow '+str(i).zfill(4)+'.bmp')
                        if os.path.exists(path): #if not, see if mow 0001.bmp etc...
                            continue
                        else: #If not found, save it as that filename
                            #If shift is held, save the screen
                            if pygame.key.get_pressed()[K_LSHIFT]:
                                pygame.image.save(screen,path)
                            else: #else, save the realscreen
                                pygame.image.save(realscreen,path)
                            print 'writing to',path
                            break #Break loop
                
                if event.key == K_F2: #F2 key
                    #Go through each tile, set to 0
                    for y,line in enumerate(field):
                        for x,cell in enumerate(line):
                            field[y][x]=0
                
                if event.key == K_LEFT: #Move left
                    player_face = 0 #which way the mower is facing
                    if playerx>0: #make sure mower stays in the screen
                        playerx -= 1
                elif event.key == K_RIGHT: #Move right
                    player_face = 1 #which way the mower is facing
                    if playerx<15: #make sure mower stays in the screen
                        playerx += 1
                elif event.key == K_UP: #Move up
                    if playery>0: #make sure mower stays in the screen
                        playery -= 1
                elif event.key == K_DOWN: #Move down
                    if playery<15: #make sure mower stays in the screen
                        playery += 1
        
        field[playery][playerx] = 1 #Mow where ever the player is
        
        screen.fill((0,0,0)) #Fill screen with black.
                             #not really needed because tiles cover entire screen.
        
        done = 1 #See if the entire lawn is mowed
        for y,line in enumerate(field):
            for x,cell in enumerate(line):
                if cell: #Draw the cut grass
                    screen.blit(grass_cut[y%2],(x*16,y*16))
                    # mod the y by 2 to alternate the grass patern
                    # between grass_cut[0] and grass_cut[1]
                else:#If any tile is still 0, we are not done
                    screen.blit(grass_uncut,(x*16,y*16))
                    done = 0

        #Draw the mower sprite to the screen.
        #tiles are 16*16 so we multiply each cord by 16
        screen.blit(mower[player_face],(playerx*16,playery*16))
        
        if done: #If all the grass is gone
            return #we're done!
        
        pygame.transform.scale2x(screen,realscreen) #Resize screen and put it on
                                                    #realscreen(what the user actually sees)
        pygame.display.flip() #Flip the display, updates what the user sees
        clock.tick(fps) #Tick the clock to control fps

while 1: #Forever...
    game() #play the game
    level += 1 #once the game is won, add 1 to the level
    #loop and play it again!

#Yes, the ordering is a joke
