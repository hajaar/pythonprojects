import pygame, sys
from pygame.locals import *
from const import *
import random

#Constants Definition
NOOFFOODBLOCKS = 11
FOODBLOCKWIDTH = 20
FOODBLOCKHEIGHT = 20


#Globals definition
gobbler_left = 0    
gobbler_right = 0
foodblocks = []

def createFoodBlocks():
    '''
    Keeps creating blocks that are meant to be gobbled up. Always maintain a constant level of blocks
    '''
    global foodblocks
    foodblocks ={}
    count_blocks = 0
    while count_blocks < NOOFFOODBLOCKS:
        fb_top = random.randint(0,WINDOWHEIGHT-FOODBLOCKHEIGHT)
        fb_left = random.randint(0,WINDOWWIDTH-FOODBLOCKWIDTH)
        does_not_contain = True
        for i in range(len(foodblocks)):
#             print foodblocks[i][1], fb_top, str(foodblocks[i][1]+FOODBLOCKHEIGHT)   
#             if (fb_top > foodblocks[i][1] and fb_top < foodblocks[i][1]+FOODBLOCKHEIGHT 
#                 and fb_left > foodblocks[i][0] and fb_left < foodblocks[i][0]+FOODBLOCKWIDTH):
#                 does_not_contain =False
#                 break
            myRect = foodblocks[i]
            print myRect, fb_left, fb_top
            print myRect.collidepoint(fb_left,fb_top)
            if (myRect.collidepoint(fb_left,fb_top)):
                does_not_contain = False
                break
            i += 1
                            
        if does_not_contain:
            foodblocks[count_blocks] = pygame.Rect(fb_top,fb_left,FOODBLOCKWIDTH,FOODBLOCKHEIGHT)
            pygame.draw.rect(windowSurface,GREEN,foodblocks[count_blocks],0)
            count_blocks +=1
      
            
def createGobbler():
    '''
    Create the gobbler
    '''
    global gobbler_left, gobbler_right
    global gobbler
    gobbler_left = WINDOWWIDTH//2
    gobbler_right = WINDOWHEIGHT//2
    gobbler_width = 40
    gobbler_height = 40
    gobbler =pygame.Rect(gobbler_left,gobbler_right,gobbler_width,gobbler_height)
    pygame.draw.rect(windowSurface,RED,gobbler,4)    
    createFoodBlocks()
    
def moveGobbler():
    '''
    Move the gobbler around. 
    '''
    global gobbler
    windowSurface.fill(BLACK)
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            if gobbler.left >= MOVESPEED:
                gobbler.left -= MOVESPEED
        if event.key == K_RIGHT:
            if gobbler.right <= WINDOWWIDTH-MOVESPEED:
                gobbler.left += MOVESPEED
        if event.key == K_UP:   
            if gobbler.top >= MOVESPEED:
                gobbler.top -= MOVESPEED            
        if event.key == K_DOWN:
            if gobbler.bottom <= WINDOWWIDTH-MOVESPEED:
                gobbler.top += MOVESPEED
    pygame.draw.rect(windowSurface,RED,gobbler,4)
    i=0
    while i < len(foodblocks):
        pygame.draw.rect(windowSurface,GREEN,foodblocks[i],2)
        i += 1
    
    gobbleFoodBlocks()
    
def gobbleFoodBlocks():
    '''
    Gobble Blocks up
    '''
    collidingBlocks()
    
def collidingBlocks():
    '''
    Check for collisions
    '''    

#initialize the game
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
createGobbler()
pygame.display.update()


    
while True:
    for event in pygame.event.get():
        if event.type != QUIT:
            moveGobbler()
            pygame.display.update()
        else:
            pygame.quit()
            sys.exit()
             
        