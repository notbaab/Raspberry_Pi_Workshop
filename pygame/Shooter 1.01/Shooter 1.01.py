import pygame
import random # for random line color
import pygame.mouse

# Random color script
a = random.randrange(1,255,1)
b = random.randrange(1,255,1)
c = random.randrange(1,255,1)
linecolor = a, b, c
#a bunch of variables
bgcolor = 0, 0, 0
x = y = 0
LEFT = 1
running = 1
s = 0
screen = pygame.display.set_mode((640, 400))
# defining image
image = pygame.image.load( "DK.bmp" )
imagePosition = image.get_rect()
imagePosition.bottom = 200
imagePosition.left = 300
screen.blit( image, imagePosition )
while running:
     event = pygame.event.poll()
     pygame.display.init()
     # font stuff
     pygame.font.init()
     fontDefault = pygame.font.Font( None, 48 )
     fontScoot = pygame.font.Font("scootchover-sans.ttf",24)
     
     pygame.event.pump()
     pygame.mouse.set_visible(0)
     if event.type == pygame.QUIT:
         running = 0
     elif event.type == pygame.MOUSEMOTION:
         x, y = event.pos

     elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
         s = s + 1 # number of shots fired
         pygame.mixer.init()
         shot = pygame.mixer.Sound("shot.wav")
         shot.play()
     
     # score board color variables and "if" statements:
     s1 = 66
     s2 = 66
     s3 = 66
     if s > 99:
          s1 = 0
          s2 = 120
          s3 = 0
     if s > 199:
          s1 = 255
          s2 = 120
          s3 = 0
     if s  > 299:
          s1 = 187
          s2 = 0
          s3 = 0
     if s > 399:
          s1 = 255
          s2 = 255
          s3 = 0
     if s > 499:
          s1 = 0
          s2 = 0
          s3 = 255
     if s > 599:
          s1 = 0
          s2 = 255
          s3 = 0
     if s > 699:
          s1 = 128
          s2 = 255
          s3 = 255
     if s > 799:
          s1 = 64
          s2 = 128
          s3 = 128
     if s > 899:
          s1 = 255
          s2 = 255
          s3 = 255
     if s > 999:
          # score board
          s1 = random.randrange(1,255,1)
          s2 = random.randrange(1,255,1)
          s3 = random.randrange(1,255,1)
          # aimer
          a = random.randrange(1,255,1)
          b = random.randrange(1,255,1)
          c = random.randrange(1,255,1)
          linecolor = a, b, c
          ya = random.randrange(1,6,1)
          if ya == 1:
               image = pygame.image.load( "ya.bmp" )
          if ya == 2:
               image = pygame.image.load( "ya2.bmp" )
          if ya == 3:
               image = pygame.image.load( "ya3.bmp" )
          if ya == 4:
               image = pygame.image.load( "ya4.bmp" )
          if ya == 5:
               image = pygame.image.load( "ya5.bmp" )
          if ya == 6:
               image = pygame.image.load( "ya6.bmp" )
     score = fontScoot.render( "Score: " + str(s),1, (s1,s2,s3))
     if s > 999:
          score = fontScoot.render( "OMG!! YOU SCORE IS " + str(s),1, (s1,s2,s3))
     if s > 1999:
          score = fontScoot.render( "HOLY F*CKING SH*T!! YOU SCORE IS " + str(s),1, (s1,s2,s3))

     pygame.display.set_caption("Shooter! 1.1 - Besktrap")

     screen.blit( score, (500,100) )
     screen.fill(bgcolor)
     screen.blit( image, imagePosition )
     pygame.draw.line(screen, linecolor, (x, 0), (x, 399))
     pygame.draw.line(screen, linecolor, (0, y), (639, y))
     screen.blit( score, (100,100) )
     pygame.display.flip()
