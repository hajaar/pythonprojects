import pygame, sys 
from pygame.locals import *
from const import *

m_left = 0
m_top = 0
direction = 0



def movePacman():
    global m_left, m_top, direction

    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            m_left -= 10
            direction = 0
        if event.key == K_RIGHT:
            m_left += 10
            direction = 1        
        if event.key == K_UP:
            m_top -= 10
            direction = 2
        if event.key == K_DOWN:
            m_top += 10
            direction = 3

    print m_left, m_top, direction
    windowSurface.fill(GREEN)
    if direction == 0:        
        windowSurface.blit(leftImageSurface,(m_left,m_top))
    elif direction == 1:
        windowSurface.blit(myImageSurface,(m_left,m_top))
    elif direction == 2:
        windowSurface.blit(upImageSurface,(m_left,m_top))
    else :
        windowSurface.blit(downImageSurface,(m_left,m_top))       
    pygame.display.update()    
        
pygame.init()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0,32)
myImageSurface = pygame.image.load('/home/hajaar/Downloads/pacman.png').convert_alpha()
leftImageSurface = pygame.transform.flip(myImageSurface,True,False)
upImageSurface = pygame.transform.rotate(myImageSurface,90)
downImageSurface = pygame.transform.rotate(myImageSurface,270)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            movePacman()

        