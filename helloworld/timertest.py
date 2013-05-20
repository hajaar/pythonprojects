import pygame, sys
from pygame.locals import QUIT, USEREVENT

count_time = 1

def showMsg():
    global count_time
    print 'time = ', count_time
    count_time += 1
    
pygame.init()
pygame.time.set_timer(USEREVENT+1,1000)

while True:
    for event in pygame.event.get():
        if event.type == USEREVENT + 1:
            showMsg()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                    