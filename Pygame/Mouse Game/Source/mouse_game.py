from pygame import *
from pygame import _view
from random import *
from math import *

init()

size = width,height = 800,600
screen = display.set_mode(size)

black_map = Surface((1600,1200))
draw.circle(black_map,(255,255,255),(800,600),150)

title = font.Font('fonts/BOOKOS.ttf',26)
f1 = font.Font('fonts/BOOKOS.ttf',20)

screen.fill((255,255,255))
display.flip()

class obstacles:
    def __init__(self):
        """This handles all obstacles."""

        self.obstacle_list = []
        self.spawn_point = []
        self.win_point = []
        self.deaths = 0
        self.difficulty = 0
        self.hidden = 0
        self.name = ''

    def create(self,details,colour,circle=False):
        """Add an obstacle to the list."""

        self.obstacle_list.append([details,colour,circle])

    def collision(self,px,py):
        """Check if the player is colliding with an obstacle."""

        self.deaths += 1
        for i in self.obstacle_list:
            if len(i[0]) == 3:
                x,y,rad = i[0]
                if sqrt((x-px)**2+(y-py)**2) < rad+p_rad: returner = 1
                try: return returner
                except: pass
            else:
                x,y,w,h = i[0]
                if x < px <= x+w and y < py <= y+h: returner = 1
                if x < px <= x+w:
                    if y-p_rad < py < y+h+p_rad: returner = 1
                if y < py < y+h:
                    if x-p_rad < px < x+w+p_rad: returner = 1
                else:
                    if y < py: h_add = 0
                    if y > py+h: h_add = h
                    if x < px: w_add = 0
                    if x > px+w: w_add = w
                    try:
                        if sqrt((x-px+w_add)**2+(y-py+h_add)**2) < p_rad: returner = 1
                    except: pass
                try:
                    return returner
                except: pass
        self.deaths -= 1
        return 0

    def draw_all(self):
        """Draw all of the obstacles."""

        for i in self.obstacle_list:
            if len(i[0]) == 3:
                x,y,rad = i[0]
                draw.circle(screen,i[1],(round(x),round(y)),round(rad))
            else:
                x,y,w,h = i[0]
                draw.rect(screen,i[1],(x,y,w,h))
        x,y,rad = self.win_point
        draw.circle(screen,(0,255,0),(round(x),round(y)),round(rad))

    def get_win(self,px,py):
        """Check if the player has won."""

        x,y,rad = self.win_point
        if sqrt((x-px)**2+(y-py)**2) < rad+p_rad: return 1
        return 0

    def load_map(self,filename):
        """Load an obstacle map."""

        fIn = open(filename, 'rU')
        exec(fIn.read())
        fIn.close()

    def update(self):
        """Update the movement of obstacles."""

        for i in self.obstacle_list:
            if type(i[2]) == type([]):

                if type(i[2][0]) == type(1):

                    if i[2][0] < 100:   # All different kinds of growth

                        if i[2][0] == 0: x_m,y_m,w_m,h_m = 0,1,0,1
                        elif i[2][0] == 1: x_m,y_m,w_m,h_m = 0,0,1,0
                        elif i[2][0] == 2: x_m,y_m,w_m,h_m = 0,0,0,1
                        elif i[2][0] == 3: x_m,y_m,w_m,h_m = 1,0,1,0
                        elif i[2][0] == 4: x_m,y_m,w_m,h_m = 0,1,1,1
                        elif i[2][0] == 5: x_m,y_m,w_m,h_m = 0,0,1,1
                        elif i[2][0] == 6: x_m,y_m,w_m,h_m = 1,0,1,1
                        elif i[2][0] == 7: x_m,y_m,w_m,h_m = 1,1,1,1
                        elif i[2][0] == 8: x_m,y_m,w_m,h_m = 0,1,0,2
                        elif i[2][0] == 9: x_m,y_m,w_m,h_m = 1,0,2,0
                        elif i[2][0] == 11: x_m,y_m,w_m,h_m = 1,1,2,1
                        elif i[2][0] == 12: x_m,y_m,w_m,h_m = 0,1,1,2
                        elif i[2][0] == 13: x_m,y_m,w_m,h_m = 1,0,2,1
                        elif i[2][0] == 14: x_m,y_m,w_m,h_m = 1,1,1,2
                        elif i[2][0] == 15: x_m,y_m,w_m,h_m = 1,1,2,2

                        i[2][3] += i[2][2]

                        i[0][0] -= i[2][2]*x_m
                        i[0][1] -= i[2][2]*y_m
                        i[0][2] += i[2][2]*w_m
                        i[0][3] += i[2][2]*h_m

                    elif 100 <= i[2][0] < 200:  # Different directions of movement
                        if i[2][0] == 100: x_m,y_m = 1,0
                        elif i[2][0] == 110: x_m,y_m = 0,1
                        elif i[2][0] == 120: x_m,y_m = 1,1
                        elif i[2][0] == 130: x_m,y_m = -1,1

                        i[2][3] += i[2][2]

                        i[0][0] += i[2][2]*x_m
                        i[0][1] += i[2][2]*y_m

                    elif 200 <= i[2][0]:        # Circular growth
                        if i[2][0] == 200: r_m = 1

                        i[2][3] += i[2][2]*r_m

                        i[0][2] += i[2][2]*r_m

                    if i[2][3] >= i[2][1]: i[2][2] = -sqrt(i[2][2]**2)
                    elif i[2][3] <= 0: i[2][2] = sqrt(i[2][2]**2)

                elif type(i[2][0]) == type([]): # Rotational movement

                    centre_x,centre_y = i[2][0]

                    x_m = cos(radians(i[2][3]))*i[2][1]
                    y_m = sin(radians(i[2][3]))*i[2][1]

                    i[0][0] = centre_x + x_m
                    i[0][1] = centre_y + y_m

                    i[2][3] += i[2][2]

                    if i[2][3] >= 360: i[2][3] = i[2][3]-360
                    elif i[2][3] <= 0: i[2][3] = i[2][3]+360

                elif type(i[2][0]) == type(1.0):    # Chasing player
                    if i[2][0] == 1.0:
                        if px-i[0][0] != 0:
                            angle = atan((py-i[0][1])/(px-i[0][0]))
                        elif py > i[0][1]:
                            angle = radians(90)
                        else:
                            angle = radians(-90)
                        if px < i[0][0]:
                            angle += radians(180)

                        if len(i[2]) == 5:
                            angle += radians(i[2][4])

                        i[0][0] += cos(angle)*i[2][2]
                        i[0][1] += sin(angle)*i[2][2]

                    if i[2][0] == 1.1: pass

                    if sqrt((i[0][0]-i[2][3][0])**2+(i[0][1]-i[2][3][1])**2) >= i[2][1]:
                        i[0][0],i[0][1] = i[2][3]

game_map = obstacles()  # Initialise the obstacles

def move_player(mx,my):
    """Moves the player towards the mouse a certain distance."""

    global px,py,p_speed

    if px-mx != 0: angle = atan((py-my)/(px-mx))
    elif py < my: angle = radians(90)
    elif py > my: angle = radians(-90)
    else: return

    if px > mx: angle += radians(180)

    x_adder = cos(angle)*p_speed
    y_adder = sin(angle)*p_speed

    if px < mx and px+x_adder > mx: px = mx
    elif px > mx and px+x_adder < mx: px = mx
    elif py < my and py+y_adder > my: py = my
    elif py > my and py+y_adder < my: py = my
    else:
        px += cos(angle)*p_speed
        py += sin(angle)*p_speed

def blit_font(text,font,colour,coords):
    """Helper for drawing fonts on the screen."""

    x_t,y_t = font.size(text)
    x,y = coords
    screen.blit(font.render(text,1,colour),(x-x_t/2,y-y_t/2))

fps = time.Clock()
p_speed = 5
p_rad = 8
level = 1
points = 0

cont = 1
while cont:

    try: game_map.load_map('maps/map'+str(level)+'.md')  # Load map. If no more maps, quit.
    except:
        cont = 0
        break

    border = 40
    game_map.create((0,0,width,border),(0,0,255))
    game_map.create((0,0,border,height),(0,0,255))
    game_map.create((0,height-border,width,border),(0,0,255))
    game_map.create((width-border,0,border,height),(0,0,255))

    px,py = game_map.spawn_point

    deaths_last = game_map.deaths

    mb1 = 0

    level += 1

    while cont:

        for evnt in event.get():
            if evnt.type == QUIT:   # Exit game
                cont = 0
                break
            elif evnt.type == MOUSEBUTTONDOWN:
                if evnt.button == 1: mb1 = 1
            elif evnt.type == MOUSEBUTTONUP:
                if evnt.button == 1: mb1 = 0

        k = key.get_pressed()
        mx,my = mouse.get_pos()

        if mb1: move_player(mx,my)

        if game_map.collision(px,py):
            px,py = game_map.spawn_point
            mb1 = 0

        if k[K_ESCAPE]:
            cont = 0
            break

        if game_map.get_win(px,py): break

        # Render game and text
        screen.fill((255,255,255))

        if game_map.hidden:
            screen.blit(black_map,(-800+px,-600+py,800-px,600-py))

        game_map.update()
        game_map.draw_all()

        draw.circle(screen,(255,0,0),(round(px),round(py)),p_rad)
        blit_font(game_map.name,title,(255,255,0),(width/2,20))
        blit_font('Deaths: '+str(game_map.deaths-deaths_last),f1,(255,255,0),(width/6,20))
        blit_font('Difficulty: '+str(game_map.difficulty),f1,(255,255,0),(width/6*5,20))
        blit_font('Total Deaths:'+str(game_map.deaths),f1,(255,255,0),(width/6,580))
        blit_font('Total Points:'+str(points-game_map.deaths),f1,(255,255,0),(width/2,580))
        blit_font('Level: '+str(level-1),f1,(255,255,0),(width/6*5,580))

        display.flip()

        fps.tick(1000/10)

    points += game_map.difficulty

##print('score = '+str(points-game_map.deaths))

quit()