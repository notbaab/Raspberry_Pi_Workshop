'''
PyBalls 2.0

Created by Nicola Pesavento 30-01-2010

pesapower@gmail.com
'''
import pygame
from pygame import *

pygame.init()

xmax = 640
ymax = 480
screen = pygame.display.set_mode((xmax,ymax))

clock = pygame.time.Clock()

background = pygame.image.load('background.bmp').convert()
gameover = pygame.image.load('game_over.bmp').convert()

ball_fut = pygame.image.load('ball_fut.bmp').convert()
ball_fut.set_colorkey((255,255,255))
ball_fut.set_alpha(200)
xball_fut = ball_fut.get_height()
yball_fut = ball_fut.get_width()

ball1 = pygame.image.load('ball1.bmp').convert()
ball1.set_colorkey((255,255,255))
xball1 = ball1.get_height()
yball1 = ball1.get_width()

ball2 = pygame.image.load('ball2.bmp').convert()
ball2.set_colorkey((255,255,255))
xball2 = ball2.get_height()
yball2 = ball2.get_width()

ball3 = pygame.image.load('ball3.bmp').convert()
ball3.set_colorkey((255,255,255))
xball3 = ball3.get_height()
yball3 = ball3.get_width()

ball4 = pygame.image.load('ball4.bmp').convert()
ball4.set_colorkey((255,255,255))
xball4 = ball4.get_height()
yball4 = ball4.get_width()

ball5 = pygame.image.load('ball5.bmp').convert()
ball5.set_colorkey((255,255,255))
xball5 = ball5.get_height()
yball5 = ball5.get_width()

# [ x, y, step_x, step_y, height, width, surface, rect]

ball1_list = [100,200,1,1, xball1, yball1, ball1, pygame.Rect((100,200),(xball1,yball1))]
ball2_list = [100,200,1,1, xball2, yball2, ball2, pygame.Rect((100,200),(xball2,yball2))]
ball3_list = [100,200,1,1, xball3, yball3, ball3, pygame.Rect((100,200),(xball3,yball3))]
ball4_list = [100,200,1,1, xball4, yball4, ball4, pygame.Rect((100,200),(xball4,yball4))]
ball5_list = [100,200,-1,-1, xball5, yball5, ball5, pygame.Rect((100,200),(xball5,yball5))]

balls_dict = {'1':ball1_list, '2':ball2_list, '3':ball3_list, '4':ball4_list, 'special ball':ball5_list}

sprites_dict = {'ball1':ball4_list, 'special ball': ball5_list}

n = 1 # variabile per cordinate di ri-generazione palla
# ny = 1 # variabile per cordinate di ri-generazione palla
n_ball = 1 # numero dizionario palla
tp_ball = 1 # tipo di palla
level = 1 # livello
t = 2000 # milli-secondi per ogni livello
seconds = 0 # secondi di gioco
points = 0 # punti
catch_special_ball = 0 # quando "prendo" la special ball diventa 1 

#------- FUNZIONI ---------------------------
def one_num_to_str(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    elif n == 2:
        return '2'
    elif n == 3:
        return '3'
    elif n == 4:
        return '4'
    elif n == 5:
        return '5'
    elif n == 6:
        return '6'
    elif n == 7:
        return '7'
    elif n == 8:
        return '8'
    elif n == 9:
        return '9'

def int_to_str(n):
    a = one_num_to_str(n/1000) + one_num_to_str((n/100)%10) + one_num_to_str((n/10)%10) + one_num_to_str(n%10)
    return a
    
def change_ball(tp_ball, n_ball, n, special_mode = 0):
    a = 1
    b = 1    
    if special_mode:
        key = 'special ball'
        key2 = 'special ball'
        a = -a
        if (seconds % 2):
            b = -b
    else:
        key = one_num_to_str(tp_ball)
        key2 = 'ball' + int_to_str(n_ball)

    sprites_dict[key2] = [0,0,0,0,0,0,0,0]
    sprites_dict[key2][0] = (100 + n)
    sprites_dict[key2][1] = (200 + n/3)
    sprites_dict[key2][2] = balls_dict[key][2] * a
    sprites_dict[key2][3] = balls_dict[key][3] * b
    sprites_dict[key2][4] = balls_dict[key][4]
    sprites_dict[key2][5] = balls_dict[key][5]
    sprites_dict[key2][6] = balls_dict[key][6]
    sprites_dict[key2][7] = pygame.Rect((100,200),(balls_dict[key][4],balls_dict[key][5]))
    tp_ball += 1
    if tp_ball == 5:
        tp_ball = 1
    return tp_ball

def game_over():
    print 'BECCATO'
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('GAME OVER   O_o', 1, (10,10,10))
    text2 = font.render('press mouse and get the purple ball', 1, (10,10,10))
    text_pos = text.get_rect(centerx = screen.get_width()/2, centery = (screen.get_height()/2 - size))
    text2_pos = text.get_rect(centerx = (screen.get_width()/2 - 110), centery = (screen.get_height()/2 + size*1.5))
    credit = font.render('Created by Nicola Pesavento', 1, (10,10,10))
    credit2 = font.render('Powered by Python, Pygame and SDL', 1, (10,10,10))
    gameover.set_alpha(230)
    screen.blit(gameover,(0,0))
    screen.blit(text, text_pos)
    screen.blit(text2, text2_pos)
    screen.blit(credit2,(0,(ymax-size)))
    screen.blit(credit,(0,(ymax-(size*2))))
    show_level(level)
    show_time(seconds)
    show_points(points)
    pygame.display.flip()
    h = 1
    while h:
       for e in pygame.event.get():
           if e.type == QUIT:
               exit()
           if e.type == MOUSEBUTTONDOWN:
               h = 0

def show_level(level):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('level: ' + int_to_str(level), 1, (10,10,10))
    text_pos = text.get_rect(centerx = screen.get_width()/2)
    screen.blit(text, text_pos)

def show_time(seconds):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('time: ' + int_to_str(seconds), 1, (10,10,10))
    screen.blit(text, (0, 0))

def show_points(points):
    size = 36
    font = pygame.font.Font(None, size)
    text = font.render('points: ' + int_to_str(points), 1, (10,10,10))
    screen.blit(text, ((xmax-155),0))
#-------------------------------------------

pygame.time.set_timer(USEREVENT, t) # incremento livelli

pygame.time.set_timer(USEREVENT+1, 1000) # tempo in secondi

while 1:
    #clock.tick(100)

    '''
    if n1 == 3:
        add_speedx = 1
        add_speedy = 1
    '''
    
    screen.blit(background, (0,0))

    xy = pygame.mouse.get_pos()

    for key in sprites_dict:

        sprite = sprites_dict[key]

        if (sprite[0] + sprite[4])>xmax or sprite[0]<0:
            sprite[2] = -sprite[2]
        if (sprite[1] + sprite[5])>ymax or sprite[1]<0:
            sprite[3] = -sprite[3]

        sprite[0] += (sprite[2])
        sprite[1] += (sprite[3])

        screen.blit(sprite[6], (sprite[0],sprite[1]))
    
        sprite[7] = pygame.Rect((sprite[0], sprite[1]),(sprite[4],sprite[5]))

        if sprite[7].collidepoint(xy):
            if key == 'special ball':
                points += 5
                catch_special_ball = 1
            else:
                game_over()
                level = 1
                n_ball = 1
                seconds = 0
                points = 0
                sprites_dict = {'ball1':ball1_list, 'special ball': ball5_list}
                pygame.time.set_timer(USEREVENT, t)
                break

    if catch_special_ball:
        del sprites_dict['special ball']
        catch_special_ball = 0
        change_ball(0, 0, n, 1)

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == USEREVENT:
            n_ball += 1
            level += 1
            n += 10
            if n > (xmax - 100 - xball_fut) :
                n = 0
            pygame.time.set_timer(USEREVENT, t)
            tp_ball = change_ball(tp_ball, n_ball, n)
        if e.type == USEREVENT+1:
            points += 1
            seconds += 1
            
    show_level(level)

    show_time(seconds)

    show_points(points)

    screen.blit(ball_fut, ((100 + n),(200 + n/3)))

    pygame.display.flip()

   # pygame.time.wait(1)         
