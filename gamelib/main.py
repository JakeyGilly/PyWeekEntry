from gamelib import roads
from gamelib import player
import pygame, sys

screenheight = 480
screenwidth = 854


def main():
    # Set player starting X, Y
    angle = 0
    player.x = (screenwidth / 2) - 25
    player.y = (screenheight / 2) - 25
    # Setting up the screen
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
        angle += player.playerangle
        # Clear the screen
        screen.fill((255, 255, 255))
        # Draw the things on the screen
        roads.drawstartroad(screen)
        #pygame.draw.rect(screen, (0, 0, 255), (player.x, player.y, 50, 50))
        player.rectRotate(screen, (255, 0, 0), (player.x, player.y, 50, 70), angle)
        pygame.display.flip()
        # Update the screen
        pygame.display.update()


