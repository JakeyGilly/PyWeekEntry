from gamelib import main
from gamelib import player
from gamelib import time
import pygame
from time import sleep as s

deltaTime = 0
Time = 0
timestep = 1
getTicksLastFrame = 0
t = 0

def updateTime():
    time.t = pygame.time.get_ticks()
    # deltaTime in seconds.
    time.deltaTime = (time.t - time.getTicksLastFrame) / 1000.0
    time.getTicksLastFrame = time.t
