import sys, pygame
#.init() must be called in every pygame, I can explain but for now, just know to
# call it
pygame.init()

size = width, height = 320, 240
# speed is two varibles, and x and a y coordinate
speed = [2, 2]
black = 0, 0, 0

# this line sets the resolution of the screen by calling set_mode
# it is saved as a variable screen because it will be needed to draw objects on 
# the screen
screen = pygame.display.set_mode((320, 240))

# this loads a sprite and stores it into a variable
ball = pygame.image.load("ball.bmp")

# calling get_rect() on a image will give you the coordinates of the image. When
# moving sprites in python, use the rect and the image will follow
ballrect = ball.get_rect()

# this is known as the game loop, it is run forever, hence the while true
while True:
	# this checks if there were any events in pygame, like any button presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # calling .move on a rect will move the ball rect AND the image. The move 
    # must be a two item variable
    ballrect = ballrect.move(speed)

    # .left, .right, .button, and .top are all attributes that correspond the 
    # edges on the rect
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # .fill(black) will erase the entire screen
    screen.fill(black)
    # .blit is a way to say redraw this image with at this rect.
    screen.blit(ball, ballrect)
    # .flip is called to refresh the screen to show the newly draw images
    pygame.display.flip()
