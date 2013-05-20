import pygame, sys
from pygame.locals import *
from const import *
import random


#Constants Definition
NOOFFOODBLOCKS = 15
FOODBLOCKWIDTH = 20
FOODBLOCKHEIGHT = 20


#Globals definition
gobbler_left = 0    
gobbler_top = 0
foodblocks = []

def createFoodBlocks():
    '''
    Keeps creating blocks that are meant to be gobbled up. Always maintain a constant level of blocks
    '''
    global foodblocks, gobbler
    foodblocks =[]
    count_blocks = 0
    while count_blocks < NOOFFOODBLOCKS:
        fb_top = random.randint(0,WINDOWHEIGHT-FOODBLOCKHEIGHT)
        fb_left = random.randint(0,WINDOWWIDTH-FOODBLOCKWIDTH)
        does_not_contain = True
        if (gobbler.collidepoint(fb_left,fb_top)):
            does_not_contain = False
            break   
        for foodblock in foodblocks:
            if (foodblock.collidepoint(fb_left,fb_top)):
                does_not_contain = False
                break                            
        if does_not_contain:
            foodblocks.append(pygame.Rect(fb_top,fb_left,FOODBLOCKWIDTH,FOODBLOCKHEIGHT))
            pygame.draw.rect(windowSurface,GREEN,foodblocks[count_blocks],0)
            count_blocks +=1

      
            
def createGobbler():
    '''
    Create the gobbler
    '''
    global gobbler_left, gobbler_top
    global gobbler
    gobbler_left = WINDOWWIDTH//2
    gobbler_top = WINDOWHEIGHT//2
    gobbler_width = 40
    gobbler_height = 40
    gobbler =pygame.Rect(gobbler_left,gobbler_top,gobbler_width,gobbler_height)
    pygame.draw.rect(windowSurface,RED,gobbler,0)    
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
    pygame.draw.rect(windowSurface,RED,gobbler,0)
    [pygame.draw.rect(windowSurface,GREEN,foodblock,0) for foodblock in foodblocks]
  
    gobbleFoodBlocks()
    moveFoodBlocks()
    
def gobbleFoodBlocks():
    '''
    Gobble Blocks up
    '''
    for foodblock in foodblocks:
        if foodblock.colliderect(gobbler):
            foodblocks.remove(foodblock)
            break

def moveFoodBlocks():
    '''
    Move Food Blocks
    '''
    windowSurface.fill(BLACK)
    for foodblock in foodblocks:
        direction_x = random.randint(0,1)
        direction_y = random.randint(0,1)
        if direction_x == 0:
            if foodblock.left >= 2*MOVESPEED:
                foodblock.left -= 2*MOVESPEED
        else:
            if foodblock.right <= WINDOWWIDTH-2*MOVESPEED:
                foodblock.left += 2*MOVESPEED
        if direction_y:   
            if foodblock.top >= 2*MOVESPEED:
                foodblock.top -= 2*MOVESPEED            
        else:
            if foodblock.bottom <= WINDOWWIDTH-2*MOVESPEED:
                foodblock.top += 2*MOVESPEED
        pygame.draw.rect(windowSurface,GREEN,foodblock,0)
    pygame.draw.rect(windowSurface,RED,gobbler,0)      
        
                
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
             
        