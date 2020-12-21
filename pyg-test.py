import sys, pygame
pygame.init()

size = width, heigh = 1280, 720
speed = [1,1]
black = 0,0,0

# creating a graphical window: 
screen = pygame.display.set_mode(size) 
# it creats a surface object (images are surgace object in pygame)

ball = pygame.image.load("intro_ball.gif") # we load the ball image
ballrect = ball.get_rect() #rect = rectangular area 


while 1: #never ending loop
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit() #checks for quit event and shuts down pygame

    ballrect = ballrect.move(speed) #this moves the ball at the variable speed
    # these if statments will reverse the speed if the ball has moved outside the screen
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > heigh:
        speed[1] = -speed[1]

    screen.fill(black) # turns the screen black so the previous frame will be earsed - comment this line and you will see a "trail"
    screen.blit(ball, ballrect) # blit is copying pixels from one image to another
    pygame.draw.rect(screen, (255,0,0),(200,150,100,50),2) 
    pygame.display.flip() # this makes the drawing visable on the screen - it makes sure we show the full images and not just harf ones