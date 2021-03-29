from gamelib import main
from gamelib import player
import pygame

x = 0
y = 0


def updatePlayerDown(key):
    if key == pygame.K_a:
        player.playerangle = -0.1
    elif key == pygame.K_d:
        player.playerangle = 0.1

def updatePlayerUp(key):
    if key == pygame.K_a or key == pygame.K_d:
        player.playerangle = 0

def rectRotate(surface, color, pos, rotation_angle):
    s = pygame.Surface((pos[2]*2,pos[3]*2))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color, ((pos[2]-pos[2]//2),(pos[3]-pos[3]//2),pos[2],pos[3]))
    s = pygame.transform.rotate(s, -rotation_angle)
    incfromrotw = (s.get_width()-pos[2]*2)//2
    incfromroth = (s.get_height()-pos[3]*2)//2
    surface.blit(s, (pos[0]-pos[2]+pos[2]//2-incfromrotw,pos[1]-pos[3]+pos[3]//2-incfromroth))

