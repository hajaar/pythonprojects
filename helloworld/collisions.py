import pygame, sys
from pygame.locals import *
from const import *
import random
import time


#Constants Definition
NOOFFOODBLOCKS = 15
FOODBLOCKWIDTH = 20
FOODBLOCKHEIGHT = 20
#Globals definition
foodblocks = []
direction = 'RIGHT'

def createFoodBlocks():
    '''
    Keeps creating blocks that are meant to be gobbled up. 
    '''
    global foodblocks, gobbler, vector
    foodblocks =[]
    vector = []
    count_blocks = 0
    while count_blocks < NOOFFOODBLOCKS:
        fb_top = random.randint(0,WINDOWHEIGHT-FOODBLOCKHEIGHT)
        fb_left = random.randint(0,WINDOWWIDTH-FOODBLOCKWIDTH)
        does_not_contain = True
        if (gobbler.collidepoint(fb_left,fb_top)):
            does_not_contain = False
            break   
        for foodblock in foodblocks:
            if (foodblock[0].collidepoint(fb_left,fb_top)):
                does_not_contain = False
                break                            
        if does_not_contain:
            foodblocks.append([pygame.Rect(fb_left,fb_top,FOODBLOCKWIDTH,FOODBLOCKHEIGHT),random.randint(1,10),random.randint(1,10)])
            windowSurface.blit(blinkySurface,(fb_left,fb_top))
            count_blocks +=1
    print count_blocks

                  
def createGobbler():
    '''
    Create the gobbler
    '''
    global gobbler
    gobbler_width = 40
    gobbler_height = 40
    gobbler_left = random.randint(gobbler_width, WINDOWWIDTH - gobbler_width)
    gobbler_top = random.randint(gobbler_height, WINDOWHEIGHT - gobbler_height)
    gobbler =pygame.Rect(gobbler_left,gobbler_top,gobbler_width,gobbler_height)
    windowSurface.blit(myImageSurface,(gobbler.left,gobbler.top))    
    createFoodBlocks()
    createWalls()

    
def moveGobbler():
    '''
    Move the gobbler around. 
    '''
    global gobbler, direction
    windowSurface.fill(WHITE)
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            direction = 'LEFT'
        if event.key == K_RIGHT:
            direction = 'RIGHT'
        if event.key == K_UP:
            direction = 'UP'          
        if event.key == K_DOWN:
            direction = 'DOWN'                     
    if direction == 'LEFT':
        gobbler.left += -MOVESPEED
        windowSurface.blit(leftImageSurface,(gobbler.left,gobbler.top))
    elif direction == 'RIGHT':
        gobbler.left += MOVESPEED
        windowSurface.blit(myImageSurface,(gobbler.left,gobbler.top))        
    elif direction == 'UP':
        gobbler.top += -MOVESPEED
        windowSurface.blit(upImageSurface,(gobbler.left,gobbler.top))
    elif direction == 'DOWN':
        gobbler.top += +MOVESPEED
        windowSurface.blit(downImageSurface,(gobbler.left,gobbler.top)) 
    if gobbler.left < 0:
        gobbler.right = WINDOWWIDTH    
    if gobbler.right > WINDOWWIDTH:
        gobbler.left = 0
    if gobbler.top < 0:
        gobbler.bottom = WINDOWHEIGHT
    if gobbler.bottom > WINDOWHEIGHT:
        gobbler.top = 0             
    [windowSurface.blit(blinkySurface,(foodblock[0].left,foodblock[0].top)) for foodblock in foodblocks]
    gobbleFoodBlocks()

    
def gobbleFoodBlocks():
    '''
    Gobble Blocks up
    '''
    global foodblocks, vector
    for foodblock in foodblocks:
        if foodblock[0].colliderect(gobbler):
            foodblocks.remove(foodblock)
            break


def bounceFoodBlocks():
    '''
    Bounce Food Blocks
    '''
    global foodblocks
    windowSurface.fill(WHITE)
    for foodblock in foodblocks:
        for momoblock in foodblocks:
            if foodblock[0].colliderect(momoblock[0]):
                foodblock[1] = -1*foodblock[1]
                foodblock[2] = -1*foodblock[2]
                momoblock[1] = -1*momoblock[1]
                momoblock[2] = -1*momoblock[2]          
        if foodblock[0].left <= 0 or foodblock[0].right >= WINDOWWIDTH:
            foodblock[1] = -1*foodblock[1]
        if foodblock[0].top <= 0 or foodblock[0].bottom >= WINDOWHEIGHT:
            foodblock[2] = -1*foodblock[2]
        for wall in walls:                      
            if foodblock[0].colliderect(wall):
                foodblock[1] = -1 * foodblock[1]
                foodblock[2] = -1 * foodblock[2]
        foodblock[0].left += foodblock[1]
        foodblock[0].top += foodblock[2]
        windowSurface.blit(blinkySurface,(foodblock[0].left,foodblock[0].top))

   
def createWalls():
    '''
    Creates walls which constrains movement
    '''
    global walls
    walls = []    
    walls.append(Rect(WINDOWWIDTH//2,0,1,WINDOWHEIGHT//4))
    walls.append(Rect(WINDOWWIDTH//2,3*WINDOWHEIGHT//4,1,WINDOWHEIGHT//4))
    walls.append(Rect(WINDOWWIDTH//3,100,WINDOWWIDTH//3,10))
    for wall in walls:
        pygame.draw.rect(windowSurface, BLACK,wall)
    
                      
#initialize the game
pygame.init()
fpsClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
myImageSurface = pygame.image.load('/home/hajaar/Downloads/pacman.png').convert_alpha()
myImageSurface = pygame.transform.scale(myImageSurface,(44,44))
leftImageSurface = pygame.transform.flip(myImageSurface,True,False)
upImageSurface = pygame.transform.rotate(myImageSurface,90)
downImageSurface = pygame.transform.rotate(myImageSurface,270)
blinkySurface = pygame.image.load('/home/hajaar/Downloads/blinky.png').convert_alpha()
blinkySurface = pygame.transform.scale(blinkySurface,(22,22))
createGobbler()
pygame.time.set_timer(USEREVENT+1,100)
pygame.display.update() 
while True:
    for event in pygame.event.get():
        if event.type != QUIT:
            if event.type == USEREVENT + 1:
                bounceFoodBlocks()
                moveGobbler()
            moveGobbler()
            createWalls()
        else:
            pygame.quit()
            sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)
             
        