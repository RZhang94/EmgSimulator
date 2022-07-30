import sys
import numpy as np
import pygame

import pygame.locals
 
from armpart import ArmPart

#black and white
black = (0, 0, 0)
white = (255, 255, 255)

# initialize the window 
pygame.init()
 
width = 750
height = 750
display = pygame.display.set_mode((width, height))
fpsClock = pygame.time.Clock()

## draw the arm
upperarm = ArmPart('upperarm.png', scale=.7)
forearm = ArmPart('forearm.png', scale=.8)
hand = ArmPart('hand.png', scale=1.0)  ##todo : find another hand
 
origin = (width / 3, height / 2)  ##define position of the arm