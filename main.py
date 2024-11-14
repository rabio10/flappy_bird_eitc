import pygame
import random
"""

position x , y 
vitesse dx , dy :  variation de x , y par rapport au temps
acceleration ddx, ddy: variation de vitesse 

button pressed
x change => x s'incremente par dx
dx change => dx s'incremente par ddx => s'augmente puis diminue 

vitesse initial : dx_0  = 10 pixels/frame --- dy_0 = 0
gravity : g = 10

in a frame : 
    y += dy_0
    if button up pressed : 
        ddy += -5
    dy += ddy
    apres dans la partie de changement de emplacement de y 
    y += dy
    ddy += g

"""
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

img = pygame.image.load('dino.png').convert()
img = pygame.transform.scale(img,(100,100))
rect = img.get_rect()
rect.center = (500,200)
x = 0
y = 520

g = 10

dx_0 = 10
dy_0 = 0

dx = 0
dy = 0

ddx = 0
ddy = 0

move_up = False
# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 36)

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_up = True
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    screen.blit(img,(x,y))
    # let's set vitesse
    dx = dx_0
    dy = dy_0
    print(f"position y : {y}")
    print(f"dy = {dy}")
    print(f"ddy = {ddy}")
    print("---------------------")

    # move in y
    #y += dy

    if move_up:
        ddy = -5
    dy += ddy
    y += dy
    ddy += g
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    move_up = False
    clock.tick(60)  # limits FPS to 60

pygame.quit()