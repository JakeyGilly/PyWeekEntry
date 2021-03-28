import pygame, sys

def main():
    pygame.init()
    global screenheight
    global screenwidth
    size = screenwidth, screenheight = 854, 480
    carHeight = (screenheight / 2) - 25
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("raylib on c++ is better")
    red = 255, 0, 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Update Game Logic
        carHeight -= 0.25
        

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the things on the screen
        drawstartroad(screen)
        pygame.draw.rect(screen, red, ((screenwidth / 2) - 25, carHeight, 50, 50))
        pygame.display.flip()
        

        # Update the screen
        pygame.display.update()


#class Road():
#    def __init__(self,length):
#        self.length = length
        

#def drawroad(screen, length, width, direction):
#    pass
def drawstartroad(screen):
    length = 200
    width = 10
    pygame.draw.line(screen, (86,86,86), ((screenwidth/4)*3, screenheight) , ((screenwidth/4)*3, 0), width)
    pygame.draw.line(screen, (86,86,86), (screenwidth/4, screenheight) , (screenwidth/4, 0), width)