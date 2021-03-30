from gamelib import main
import pygame

def drawstartroad(screen,offsetX,offsetY):
    length = 200
    width = 10
    pygame.draw.line(screen, (86,86,86), ((main.screenwidth/4)*3-offsetX, main.screenheight-offsetY) , ((main.screenwidth/4)*3-offsetX, 0-offsetY), width)
    pygame.draw.line(screen, (86,86,86), (main.screenwidth/4-offsetX, main.screenheight-offsetY) , (main.screenwidth/4-offsetX, 0-offsetY), width)

#class Road():
#    def __init__(self,length):
#        self.length = length
        

#def drawroad(screen, length, width, direction):
#    pass