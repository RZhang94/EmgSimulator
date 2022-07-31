import sys
import numpy as np
import pygame
import time

import pygame.locals
 
from armpart import ArmPart

from read_sample_data_noPlot import * 

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
upperarm = ArmPart('upperarm.png', scale=.7, initial_rotation=-0.2)
forearm = ArmPart('forearm.png', scale=.8, initial_rotation=-1.5)
hand = ArmPart('hand.png', scale=1.0, initial_rotation=-1.5)  ##todo : find another hand
 
origin = (width / 3, height / 2)  ##define position of the arm

## speed and direction
#speed = input("what speed do we want?")
#direction = input("What direction do we want(1 or -1)?")
speed = 0
direction = -1
##direction -1 : rise, counterclockwise
##direction 1 : relax, clockwise
sd = speed*direction

# need a module to downsample the data

for i in range(len(differentialForce1)):
    # if differentialForce1[i] - 0.5 > 0:
    #     direction = - 1
    # else:
    #     direction = 1


    # need the module to set the time delay and compare with the execution time per loop
    start_time = time.time()
    # speed = differentialForce1[i] * 0.5
    # sd = speed * direction
    # sd = 0
    

    display.fill(white)
 
    ua_image, ua_rect = upperarm.rotate(.00) 
    fa_image, fa_rect = forearm.rotate(-.02*sd) 
    h_image, h_rect = hand.rotate(-.02*sd)
 
    # generate (x,y) positions of each of the joints
    joints_x = np.cumsum([0, 
                          upperarm.scale * np.cos(upperarm.rotation),
                          forearm.scale * np.cos(forearm.rotation),
                          hand.length * np.cos(hand.rotation)]) + origin[0]
    joints_y = np.cumsum([0, 
                          upperarm.scale * np.sin(upperarm.rotation),
                          forearm.scale * np.sin(forearm.rotation), 
                          hand.length * np.sin(hand.rotation)]) * -1 + origin[1]
    joints = [(int(x), int(y)) for x,y in zip(joints_x, joints_y)]
 
 ## ignore for now
    def transform(rect, origin, arm_part):
        rect.center += np.asarray(origin)
        rect.center += np.array([np.cos(arm_part.rotation) * arm_part.offset,
                                -np.sin(arm_part.rotation) * arm_part.offset])
 
## ignore for now
    transform(ua_rect, joints[0], upperarm)
    transform(fa_rect, joints[1], forearm)
    transform(h_rect, joints[2], hand)
    #  transform the hand a bit more because it's weird
    h_rect.center += np.array([np.cos(hand.rotation), 
                             -np.sin(hand.rotation)]) * -10
 
    display.blit(ua_image, ua_rect)
    display.blit(fa_image, fa_rect)
    display.blit(h_image, h_rect)
 
    # check for quit
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    fpsClock.tick(30)

    end_time = time.time()
    interval_time = end_time - start_time
    # print('time per loop is:  ', interval_time)