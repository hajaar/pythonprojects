import pygame
from pygame.locals import QUIT
import sys

pygame.init()
windowSurface = pygame.display.set_mode((400,400),0,32)
pygame.display.set_caption('Vaaya Bhimu')
basicFont = pygame.font.SysFont(None, 28, True, True)
myText = basicFont.render('Moonjiya Paaru',True,(255,255,255),(0,0,255))
textRect = myText.get_rect()
textRect.centerx = 200
textRect.centery = 200
windowSurface.fill((255,255,255))
pygame.draw.polygon(windowSurface,(0,255,255),((10,10),(10,30),(30,50),(50,10)))
pygame.draw.line(windowSurface, (0, 0, 255), (60, 60), (120,60), 4)
windowSurface.blit(myText,textRect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
            