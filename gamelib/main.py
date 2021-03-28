from gamelib import roads
from gamelib import player
import pygame, sys

screenheight = 480
screenwidth = 854

def main():
    player.x = (screenwidth / 2) - 25
    player.y = (screenheight / 2) - 25
    pygame.init()
    size = screenwidth, screenheight
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Chase")
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                player.updatePlayer(event.key)

        # Update Game Logic
  
        

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the things on the screen
        roads.drawstartroad(screen)
        pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, 50, 50))
        pygame.display.flip()
        

        # Update the screen
        pygame.display.update()


