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
gobbler_left = 0    
gobbler_top = 0
foodblocks = []
gobblervelx = 0
gobblervely = 0



def createFoodBlocks():
    '''
    Keeps creating blocks that are meant to be gobbled up. Always maintain a constant level of blocks
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
            foodblocks.append([pygame.Rect(fb_top,fb_left,FOODBLOCKWIDTH,FOODBLOCKHEIGHT),random.randint(1,10),random.randint(1,10)])
            pygame.draw.rect(windowSurface,GREEN,foodblocks[count_blocks][0],0)
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
    global gobbler, gobblervelx,gobblervely
    windowSurface.fill(BLACK)
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            gobblervelx = -MOVESPEED
            gobblervely = 0
        if event.key == K_RIGHT:
            gobblervelx = MOVESPEED
            gobblervely = 0
        if event.key == K_UP:
            gobblervelx = 0
            gobblervely = -MOVESPEED
        if event.key == K_DOWN:
            gobblervelx = 0
            gobblervely = MOVESPEED                        
    if gobbler.left > 0 :
        gobbler.left += gobblervelx
    if gobbler.right < WINDOWWIDTH:
        gobbler.left += gobblervelx
    if gobbler.top >= 0 :
        gobbler.top += gobblervely
    if gobbler.bottom <= WINDOWHEIGHT:
        gobbler.top += gobblervely
    pygame.draw.rect(windowSurface,RED,gobbler,0)
    [pygame.draw.rect(windowSurface,GREEN,foodblock[0],0) for foodblock in foodblocks]
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
    windowSurface.fill(BLACK)
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
        foodblock[0].left += foodblock[1]
        foodblock[0].top += foodblock[2]
        pygame.draw.rect(windowSurface,GREEN,foodblock[0],0)
    pygame.draw.rect(windowSurface,RED,gobbler,0)

                  
#initialize the game
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
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
            pygame.display.update()
        else:
            pygame.quit()
            sys.exit()
             
        