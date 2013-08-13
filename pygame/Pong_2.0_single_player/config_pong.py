import pygame
pygame.mixer.init()
hit_sound=pygame.mixer.Sound("hit.wav")
HEIGHT=480
WIDTH=600
THICKNESS=10
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
FRICTION=0.25
FRICTION_2=0.2
X_VELOCITY_SCALE=0.04 
RADIUS=10
GAP=20
LENGTH=200
COMP_LENGTH=200
SPEED=250
Y_SPEED_1=2.0 # vertical speed of ball 1
Y_SPEED_2=1.8 # vertical speed of ball 2
PLAYER_BAT_SPEED=4.0
DIFFICULTY=4.0 #comp bat speed
