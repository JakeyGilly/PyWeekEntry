from gamelib import roads
from gamelib import player
import pygame, sys

screenheight = 480
screenwidth = 854


def main():
    # Set player starting X, Y
    player.x = (screenwidth / 2) - 25
    player.y = (screenheight / 2) - 25
    # Setting up the screen
    size = screenwidth, screenheight
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chase")
    #Detecting for Quit and Key Press events
    playerX_change = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN: #player.updatePlayer(event.key)
                if event.key == pygame.K_a:
                    playerX_change = -0.1
                elif event.key == pygame.K_d:
                    playerX_change = 0.1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    playerX_change = 0
        player.x += playerX_change
        # Clear the screen
        screen.fill((255, 255, 255))
        # Draw the things on the screen
        roads.drawstartroad(screen)
        pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, 50, 50))
        pygame.display.flip()
        # Update the screen
        pygame.display.update()


