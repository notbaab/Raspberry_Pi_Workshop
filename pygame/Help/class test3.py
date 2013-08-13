import pygame
from pygame.locals import*
import math
import random
import sys
pygame.init()

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, size):
        pygame.sprite.Sprite.__init__(self)

        self.radius = radius

        self.image = pygame.Surface([self.radius*2, self.radius*2])
        pygame.draw.circle(self.image, [0,0,255], [self.radius,self.radius], self.radius)
        self.image.set_colorkey([0,0,0])
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move([random.randint(self.radius, size[0]-self.radius),random.randint(self.radius, size[1]-self.radius)])

        self.xspeed = random.randint(1,3)*rand_pn()
        self.yspeed = random.randint(1,3)*rand_pn()



    def move(self, size):
        self.rect = self.rect.move([self.xspeed, self.yspeed])
        if self.rect.left<0 or self.rect.right>size[0]:
            self.xspeed*=-1
        if self.rect.bottom<0 or self.rect.top>size[1]:
            self.yspeed*=-1
        
    def update(self, screen):
        screen.blit(self.image, self.rect)

class Boom(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.radius = 30
        self.org_radius = int(self.radius)

        self.image = pygame.Surface([self.radius*2, self.radius*2])
        pygame.draw.circle(self.image, [255,127,0], [self.radius,self.radius], self.radius)
        self.image.set_colorkey([0,0,0])
        
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)

        self.life = self.radius
        
    def update(self, screen):
        self.radius = self.life

        self.image.fill([0,0,0])
        pygame.draw.circle(self.image, [255,127,0], [self.org_radius,self.org_radius], self.radius)
        self.image.set_colorkey([0,0,0])
        
        screen.blit(self.image, self.rect)
        self.life-=1
    


def get_dist(rect1, rect2):
    distance = (max(math.sqrt(math.pow(rect1.center[0]-rect2.center[0] , 2)+math.pow(rect1.center[1]-rect2.center[1] , 2)),1))
    return distance

def rand_pn():
    return random.randint(0,1)*2-1


def main():
    size = (800,600)
    screen = pygame.display.set_mode(size)
    
    particals = []
    booms = []
    
    for a in xrange(80):
        particals.append(Ball(3, size))

    while 1:  

        for dot1 in particals:
            dot1.move(size)
            dot1.update(screen)

            for dot2 in particals:

                    if get_dist(dot1.rect,dot2.rect)<dot1.radius+dot2.radius and dot1!=dot2:
                        particals.remove(dot1)
                        particals.remove(dot2)
                        booms.append(Boom([(dot1.rect.center[0]+dot2.rect.center[0])/2,(dot1.rect.center[1]+dot2.rect.center[1])/2]))

        for boom in booms:
            boom.update(screen)
            for dot in particals:
                 if get_dist(dot.rect,boom.rect)<dot.radius+boom.radius :
                     particals.remove(dot)

            if boom.life<0:
                booms.remove(boom)
                
        pygame.display.flip()
        screen.fill([0,0,0])

        #exiting by pressing exit or Esc
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT or keys[K_ESCAPE]:
                pygame.quit(); sys.exit()

main()
            
            
