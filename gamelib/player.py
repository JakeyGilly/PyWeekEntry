from gamelib import main
from gamelib import player
import pygame

x = 0
y = 0


def updatePlayer(key):
    if key == pygame.K_a:
        player.x = player.x - 7
    elif key == pygame.K_d:
        player.x = player.x + 7