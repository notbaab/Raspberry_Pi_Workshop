from pygame import *
from pygame import _view
from random import *
from math import *

init()

size = width,height = 800,600
screen = display.set_mode(size)

# Create the plane images
# The following code is very memory inefficient, but that's irrelevant and it makes my life easier.
plane1 = image.load('images/plane1.png')
plane1 = [plane1,transform.rotate(plane1,45),transform.rotate(plane1,90),transform.rotate(plane1,135)\
,transform.rotate(plane1,180),transform.rotate(plane1,225),transform.rotate(plane1,270),transform.rotate(plane1,315)]
for i in plane1: i.set_colorkey((255,255,255))

plane2 = image.load('images/plane2.png')
plane2 = [plane2,transform.rotate(plane2,45),transform.rotate(plane2,90),transform.rotate(plane2,135)\
,transform.rotate(plane2,180),transform.rotate(plane2,225),transform.rotate(plane2,270),transform.rotate(plane2,315)]
for i in plane2: i.set_colorkey((255,255,255))

plane3 = image.load('images/plane3.png')
plane3 = [plane3,transform.rotate(plane3,45),transform.rotate(plane3,90),transform.rotate(plane3,135)\
,transform.rotate(plane3,180),transform.rotate(plane3,225),transform.rotate(plane3,270),transform.rotate(plane3,315)]
for i in plane3: i.set_colorkey((255,255,255))

arrow = image.load('images/arrow.bmp')
arrow = [arrow,transform.rotate(arrow,270),transform.rotate(arrow,180),transform.rotate(arrow,90)]

gamestate = 0

ft = font.Font('fonts/BOOKOS.ttf',60)

running = 1
while running:      # Startup menu
    event.pump()
    if key.get_pressed()[K_ESCAPE]:
        running = 0
        gamestate = 0

    mx,my = mouse.get_pos()
    lc = mouse.get_pressed()[0]

    screen.fill((255,255,255))

    # Button for normal mode
    normal_i = ft.render('Normal Mode',1,(0,0,0)),ft.size('Normal Mode')
    screen.blit(normal_i[0],(400-normal_i[1][0]/2,150-normal_i[1][1]/2))
    if 400-normal_i[1][0]/2 < mx < 400+normal_i[1][0]/2 and 150-normal_i[1][1]/2 < my < 150+normal_i[1][1]/2:
        draw.rect(screen,(255,0,0),(400-normal_i[1][0]/2-10,150-normal_i[1][1]/2-5,normal_i[1][0]+20,normal_i[1][1]+10),4)
        if lc:
            running = 0
            gamestate = 1

    # Button for fast mode
    fast_i = ft.render('Fast Mode',1,(0,0,0)),ft.size('Fast Mode')
    screen.blit(fast_i[0],(400-fast_i[1][0]/2,300-fast_i[1][1]/2))
    if 400-fast_i[1][0]/2 < mx < 400+fast_i[1][0]/2 and 300-fast_i[1][1]/2 < my < 300+fast_i[1][1]/2:
        draw.rect(screen,(255,0,0),(400-fast_i[1][0]/2-10,300-fast_i[1][1]/2-5,fast_i[1][0]+20,fast_i[1][1]+10),4)
        if lc:
            running = 0
            gamestate = 2

    # Button for passive mode
    passive_i = ft.render('Passive Mode',1,(0,0,0)),ft.size('Passive Mode')
    screen.blit(passive_i[0],(400-passive_i[1][0]/2,450-passive_i[1][1]/2))
    if 400-passive_i[1][0]/2 < mx < 400+passive_i[1][0]/2 and 450-passive_i[1][1]/2 < my < 450+passive_i[1][1]/2:
        draw.rect(screen,(255,0,0),(400-passive_i[1][0]/2-10,450-passive_i[1][1]/2-5,passive_i[1][0]+20,passive_i[1][1]+10),4)
        if lc:
            running = 0
            gamestate = 3

    display.flip()
    time.wait(20)

if gamestate == 3:
    PSPEED = 5
else:
    PSPEED = 11

player1 = [width/2,height/2,10]
direction = 1
points = 0

font1 = font.Font('fonts/BOOKOS.ttf',20)

class explosion:
    def __init__(self,min_size,max_size,colour,x,y):
        """This class is just for handling explosion variables."""

        self.size = min_size
        self.max_size = max_size
        self.colour = colour
        self.x = round(x)
        self.y = round(y)

    def draw(self):
        """Draw the explosion."""

        if self.size <= self.max_size:
            draw.circle(screen,self.colour,(self.x,self.y),self.size)
            self.size += 1


class missile:
    def __init__(self,supr = 0):
        """This class handles the missiles."""

        self.x1 = (randint(width/8,width/8*2),randint(width/8*6,width/8*7))[randint(0,1)]
        self.y1 = height
        self.x2 = self.x1
        self.y2 = height+3
        self.x_vel = 0
        self.y_vel = -3
        self.tail_list = []
        self.alive = 0

        if not supr:    # Missile class 1
            self.fuel = randint(200,250)
            self.speed = randint(5,8)/10
            self.colour = (0,0,0)
        elif supr == 1: # Missile class 2
            self.fuel = randint(250,400)
            self.speed = 1
            self.colour = (128,0,128)
        elif supr == 2: # Missile class 3
            self.fuel = 250
            self.speed = 3
            self.colour = (0,0,0)
        self.supr = supr


    def move(self):
        """Move the missile to its new position."""

        global dead,player,points,gamestate

        if self.alive:

            if self.fuel > 0:

                if len(self.tail_list) >= 10: del self.tail_list[-1]
                self.tail_list.insert(0,((self.x1,self.y1),(self.x2,self.y2)))

                if self.supr != 2:  # Change velocity towards the player
                    dist = abs(self.x_vel)*(abs(self.x_vel)+1)/2
                    if self.x_vel < 0 and self.x1-dist < 0: self.x_vel += 2
                    elif self.x_vel > 0 and self.x1+dist > width: self.x_vel -= 2
                    elif self.x1 < player1[0]: self.x_vel += self.speed
                    elif self.x1 > player1[0]: self.x_vel -= self.speed

                    dist = abs(self.y_vel)*(abs(self.y_vel)+1)/2
                    if self.y_vel < 0 and self.y1-dist < 0: self.y_vel += 2
                    elif self.y_vel > 0 and self.y1+dist > height: self.y_vel -= 2
                    elif self.y1 < player1[1]: self.y_vel += self.speed
                    elif self.y1 > player1[1]: self.y_vel -= self.speed

                else:   # Move strait towards the player
                    angle = atan((player1[1]-self.y1)/(player1[0]-self.x1+0.00001))
                    if self.x1 > player1[0]: angle += radians(180)
                    self.x_vel = cos(angle)*self.speed
                    self.y_vel = sin(angle)*self.speed
                self.fuel -= 1

            else:
                self.y_vel += 0.5

            self.x2 = self.x1
            self.y2 = self.y1
            self.x1 += self.x_vel
            self.y1 += self.y_vel

            if self.y1 > height+10 and self.fuel <= 0:  # Missile crashed into the ground
                self.alive = 0

                if self.supr == 0:      # Scoring for dead missiles
                    if gamestate == 1:
                        points += 100
                    elif gamestate == 2:
                        points += 75
                    elif gamestate == 3:
                        points += 125

                elif self.supr == 1: points += 150
                elif self.supr == 2: points += 200
                explosions.append(explosion(25,30,(255,0,0),self.x2,self.y2))

            if sqrt((self.x1-player1[0])**2+(self.y1-player1[1])**2) < 10:  # Missile hit the player
                self.alive = 0
                self.fuel = 0
                explosions.append(explosion(25,30,(255,0,0),self.x1,self.y1))
                player1[2] -= 1

        elif self.fuel <= 0: dead += 1

        else:
            if self.supr == 2: r_num = randint(1,80)
            else: r_num = randint(1,20)
            if r_num == 1:
                self.alive = 1
                explosions.append(explosion(25,30,(255,255,0),self.x1,self.y1))

    def draw(self):
        """Draw the missile."""

        if self.alive:

            if self.fuel > 0:   # Draw fire/smoke behind the missile
                for i,p in enumerate(self.tail_list):
                    draw.line(screen,(25*i,25*i,25*i),p[0],p[1],6+i*2)
                    if i < 3:
                        draw.line(screen,(255,0,0),p[0],p[1],7-i*3)

            if self.supr != 2:  # Draw the missile
                draw.line(screen,self.colour,(self.x1,self.y1),(self.x2,self.y2),3)
            else:
                if self.fuel > 0: draw.line(screen,(255,0,0),(self.x1,self.y1),(self.x2,self.y2),3)
                draw.circle(screen,self.colour,(round(self.x1),round(self.y1)),4)

            # Draw pointing arrow if missile is out of the screen
            if self.x1 < 0: screen.blit(arrow[3],(0,self.y1-5))
            elif self.x1 > width: screen.blit(arrow[1],(width-10,self.y1-5))
            elif self.y1 > height: screen.blit(arrow[2],(self.x1-5,height-10))
            elif self.y1 < 0: screen.blit(arrow[0],(self.x1-5,0))


level = 0
missiles = []
explosions = []

hp_start = 0

if gamestate: running = 1
while running:      # Main game loop
    level += 1

    if hp_start == player1[2]: points += 1000

    if gamestate == 2:
        num_missiles = round(level*1.25)    # Set the number of missiles to spawn
    else:
        num_missiles = level
    missiles = []
    hp_start = player1[2]

    if gamestate == 1:
        if level >= 7:
            for i in range(round((level-7)/4)+1):
                missiles.append(missile(1))
        if level >= 3:
            for i in range(round((level-3)/5)+1):
                missiles.append(missile(2))

    for i in range(num_missiles-len(missiles)):
        missiles.append(missile())

    time.wait(100)

    while 1:        # Level loop
        event.pump()
        k = key.get_pressed()
        mx,my = mouse.get_pos()
        lc,mc,rc = mouse.get_pressed()

        if k[K_ESCAPE]:
            running = 0
            break

        # Complicated plane movement
        if k[K_UP]:
            if player1[1] - sin(pi/4)*PSPEED > 10:
                if k[K_LEFT] and player1[0] - cos(pi/4)*PSPEED > 10:
                    player1[0] -= cos(pi/4)*PSPEED
                    player1[1] -= sin(pi/4)*PSPEED
                    direction = 8

                elif k[K_RIGHT] and player1[0] + cos(pi/4)*PSPEED < width-10:
                    player1[0] += cos(pi/4)*PSPEED
                    player1[1] -= sin(pi/4)*PSPEED
                    direction = 2

                elif player1[1] - PSPEED > 10:
                    direction = 1
                    player1[1] -= PSPEED

            if gamestate == 3: points -= 1

        elif k[K_DOWN]:
            if player1[1] + sin(pi/4)*PSPEED < height-10:
                if k[K_LEFT] and player1[0] - cos(pi/4)*PSPEED > 10:
                    player1[0] -= cos(pi/4)*PSPEED
                    player1[1] += sin(pi/4)*PSPEED
                    direction = 6

                elif k[K_RIGHT] and player1[0] + cos(pi/4)*PSPEED < width-10:
                    player1[0] += cos(pi/4)*PSPEED
                    player1[1] += sin(pi/4)*PSPEED
                    direction = 4

                elif player1[1] - PSPEED < height-10:
                    direction = 5
                    player1[1] += PSPEED

            if gamestate == 3: points -= 1

        elif k[K_LEFT] and player1[0] - PSPEED > 10:
            player1[0] -= PSPEED
            direction = 7
            if gamestate == 3: points -= 1

        elif k[K_RIGHT] and player1[0] + PSPEED < width-10:
            player1[0] += PSPEED
            direction = 3
            if gamestate == 3: points -= 1

        screen.fill((255,255,255))

        dead = 0
        for i in missiles:  # Update missiles
            i.move()
            i.draw()

        if dead >= num_missiles: break  # End the level if all of the missiles are dead

        # Draw plane
        x,y = plane1[1-direction].get_size()
        if gamestate == 1: screen.blit(plane1[1-direction],(player1[0]-x/2,player1[1]-y/2))
        if gamestate == 2: screen.blit(plane2[1-direction],(player1[0]-x/2,player1[1]-y/2))
        if gamestate == 3: screen.blit(plane3[1-direction],(player1[0]-x/2,player1[1]-y/2))

        for i in explosions:    # Draw explosions
            i.draw()

        try:    # Draw text
            msg_hp = font1.render('You have %i lives left'%(player1[2]),1,(0,0,0))
            screen.blit(msg_hp,(15,15))

            msg_lv = font1.render('Level '+str(level),1,(0,0,0))
            screen.blit(msg_lv,(15,50))

            msg_pts = font1.render('Points: '+str(points),1,(0,0,0))
            screen.blit(msg_pts,(15,85))
        except: pass

        display.flip()

        if player1[2] < 1:  # Player has died
            running = 0
            break

        if gamestate == 1:
            time.delay(20)
        elif gamestate == 2:
            time.delay(15)
        elif gamestate == 3:
            time.delay(30)

quit()