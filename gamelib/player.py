from gamelib import main
from gamelib import player
from gamelib import time
import pygame

x = 0
y = 0

acceleration = 0.1


pushed_forward = False
pushed_backward = False
velocity = 0

def updatePlayerDown(key):
    if key == pygame.K_a:
        player.playerangle = -0.1
    elif key == pygame.K_d:
        player.playerangle = 0.1
    elif key == pygame.K_w:
        player.pushed_forward = True
    elif key == pygame.K_s:
        player.pushed_backward = True

def updatePlayerUp(key):
    if key == pygame.K_a or key == pygame.K_d:
        player.playerangle = 0
    if key == pygame.K_w:
        player.pushed_forward = False
    if key == pygame.K_s:
        player.pushed_backward = False

def rectRotate(surface, color, pos, rotation_angle):
    s = pygame.Surface((pos[2]*2,pos[3]*2))
    s = s.convert_alpha()
    s.fill((0,0,0,0))
    pygame.draw.rect(s, color, ((pos[2]-pos[2]//2),(pos[3]-pos[3]//2),pos[2],pos[3]))
    s = pygame.transform.rotate(s, -rotation_angle)
    incfromrotw = (s.get_width()-pos[2]*2)//2
    incfromroth = (s.get_height()-pos[3]*2)//2
    surface.blit(s, (pos[0]-pos[2]+pos[2]//2-incfromrotw,pos[1]-pos[3]+pos[3]//2-incfromroth))

def updateVelocity(move,unmove):
    player.y -= (player.velocity)# * time.deltaTime
    #player.velocity += time.timestep * acceleration * time.deltaTime;
    if move:
        if player.velocity < 2:
            player.velocity += acceleration
    if unmove:
        if player.velocity >= 0:
            player.velocity -= acceleration / 10
    if player.velocity < 0:
        player.velocity = 0
    print(player.velocity)
    #print(player.y)

