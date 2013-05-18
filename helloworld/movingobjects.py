import pygame
import sys
import random
import time
from pygame.locals import QUIT


WINDOWHEIGHT = 400
WINDOWWIDTH = 400

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)

direction_x = 1
direction_y = 1

def ranColor():
    colors_list =[YELLOW, RED, GREEN, BLUE, WHITE]
    return colors_list[random.randint(0,4)]
        
def ranVelocity():
    vel_x = random.randint(1,5)
    vel_y = random.randint(1,5)
    vel_direction_x = random.randint(0,1) 
    vel_direction_y = random.randint(0,1)
    return (vel_x,vel_y,vel_direction_x,vel_direction_y)

def generateCircles():
    global circle_list
    circle_list = {}
    for i in range(10):
        pos_x = random.randint(60,349)
        pos_y = random.randint(60,349)
        tmp_radius = random.randint(10,50)
        tmp_color = ranColor()
        circle_list[i] = [tmp_color,pos_x,pos_y,tmp_radius]
        pygame.draw.circle(windowSurface,tmp_color,(pos_x,pos_y),tmp_radius,2)

def moveCircles():
    global direction_x, direction_y
    windowSurface.fill(BLACK)       
    for i in range(10):
        vel = ranVelocity()
        circle_list[i][1] += direction_x*vel[0]
        circle_list[i][2] += direction_y*vel[1]
        if (circle_list[i][1] > WINDOWWIDTH - circle_list[i][3]):
            direction_x = -1*direction_x
        if (circle_list[i][2] > WINDOWHEIGHT - circle_list[i][3]):
            direction_y = -1*direction_y
        if (circle_list[i][1] > circle_list[i][3]):
            direction_x = -1*direction_x
        if (circle_list[i][2] > circle_list[i][3]):
            direction_y = -1*direction_y
        pygame.draw.circle(windowSurface,circle_list[i][0],(circle_list[i][1],circle_list[i][2]),circle_list[i][3],2)
    
    
global windowSurface    
windowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Moving Objects')    
generateCircles()    


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    moveCircles()
    pygame.display.update()
    time.sleep(0.1)
                