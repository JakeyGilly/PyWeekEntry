from gamelib import roads
from gamelib import player
from gamelib import time
import pygame, sys

screenheight = 1080
screenwidth = 1920


def main():
    pygame.init()
    # Set player starting X, Y
    player.x = 0
    player.y = 0

    #  Setting up the screen
    size = screenwidth, screenheight
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chase")
    #Detecting for Quit and Key Press events
    player.playerangle = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: player.updatePlayerDown(event.key)
            if event.type == pygame.KEYUP: player.updatePlayerUp(event.key)
        
        player.updateVelocity(player.pushed_forward,player.pushed_backward)
        #Rotate if needed
        player.angle += player.playerangle
        # Clear the screen
        screen.fill((255, 255, 255))
        # Draw the things on the screen
        roads.drawstartroad(screen, player.x,player.y)
        player.rectRotate(screen, (255, 0, 0), ((screenwidth / 2) - 25,(screenheight / 2) - 25 , 50, 70), player.angle)
        # Update the screen
        pygame.display.update()