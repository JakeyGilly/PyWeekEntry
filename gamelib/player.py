from gamelib import main
from gamelib import player
import pygame

x = 0
y = 0


def updatePlayerDown(key):
    if key == pygame.K_a:
        player.playerX_change = -0.1
    elif key == pygame.K_d:
        player.playerX_change = 0.1

def updatePlayerUp(key):
    if key == pygame.K_a or key == pygame.K_d:
        player.playerX_change = 0