from gamelib import main
import pygame


def drawstartroad(screen,offsetX,offsetY): 
    pygame.draw.rect(screen, (86,86,86),((main.screenwidth//2)//2-offsetX,0-offsetY,main.screenwidth//2,main.screenheight))

#class Road():
#    def __init__(self,length):
#        self.length = length
        

#def drawroad(screen, length, width, direction):
#    pass