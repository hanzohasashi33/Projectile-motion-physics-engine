import pygame                                        #import pygame module
import math                                          #import math module for trignometric functions

wScreen = 1200                                       #specify height and width of pygame window
hScreen = 500                          

win = pygame.display.set_mode((wScreen,hScreen))     #window parameters
pygame.display.set_caption('Projectile Motion')      #set title for window


class ball(object):                                  #define a class ball to draw the golf ball
    def __init__(self,x,y,radius,color):         
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)             #draw a golf ball
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)
        
        
        '''
        Draws a circle on the given surface.

        Parameters:
            surface (Surface) -- surface to draw on
            color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
            center (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- center 
            point of the circle as a sequence of 2 ints/floats, e.g. (x, y)
            radius (int or float) -- radius of the circle, measured from the center parameter, a radius of 0 will only draw the center pixel
        '''


    @staticmethod
    def ballPath(startx, starty, power, ang, time):
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power                         #define the path of the golf ball as terms of velocity and distance

        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)

        newx = round(distX + startx)
        newy = round(starty - distY)


        return (newx, newy)                                    #returns new position


def redrawWindow():
    win.fill((64,64,64))                                       #window background color to grey
    golfBall.draw(win)                                         #draws a golfball at the specified coordinates
    pygame.draw.line(win, (0,0,0),line[0], line[1])            #draws a line to specify power and respected things
    
    '''
    Draws a straight line on the given surface. There are no endcaps. For thick lines the ends are squared off.

    Parameters:
        surface (Surface) -- surface to draw on
        color (Color or int or tuple(int, int, int, [int])) -- color to draw with, the alpha value is optional if using a tuple (RGB[A])
        start_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- start position of the line, (x, y)
        end_pos (tuple(int or float, int or float) or list(int or float, int or float) or Vector2(int or float, int or float)) -- end position of the line, (x, y)
    '''
    
    pygame.display.update()

def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))
    except:
        angle = math.pi / 2

    if pos[1] < sY and pos[0] > sX:              #specifies the angle in respective coordinates
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle
        
    return angle


golfBall = ball(300,494,5,(255,255,255))          #draws a golf ball

run = True
time = 0
power = 0
angle = 0
shoot = False
clock = pygame.time.Clock()
while run:
    clock.tick(200)
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05                          #time is the respective time delay 
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            time = 0
            golfBall.y = 494

    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]
    redrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:               #throws the ball into projectile motion
            if not shoot:
                x = golfBall.x
                y = golfBall.y
                pos =pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                angle = findAngle(pos)



pygame.quit()
quit()
