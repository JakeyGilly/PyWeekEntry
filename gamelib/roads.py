from gamelib import main
import pygame

def drawstartroad(screen):
    length = 200
    width = 10
    pygame.draw.line(screen, (86,86,86), ((main.screenwidth/4)*3, main.screenheight) , ((main.screenwidth/4)*3, 0), width)
    pygame.draw.line(screen, (86,86,86), (main.screenwidth/4, main.screenheight) , (main.screenwidth/4, 0), width)

#class Road():
#    def __init__(self,length):
#        self.length = length
        

#def drawroad(screen, length, width, direction):
#    pass