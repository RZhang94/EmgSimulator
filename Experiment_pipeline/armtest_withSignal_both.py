import sys
sys.path.append('/Users/zhangzhaoxiang/Documents/GitHub/EmgSimulator')

import sys
import numpy as np
import pygame
import time
import pygame.locals
from armpart import ArmPart
from simpleDynamics import *


def positionRegularization(Positions, maxPosition, minPosition):
    regPositions = (maxPosition-minPosition) * (Positions - Positions.min())/(Positions.max() - Positions.min()) + minPosition
    scale = (maxPosition-minPosition)/(Positions.max() - Positions.min())
    return regPositions, scale

def gravityScale(Positions, maxPosition, minPosition):
    scale = (maxPosition-minPosition)/(Positions.max() - Positions.min())
    return scale

def armMove(mode, position):
        
    #black and white
    black = (0, 0, 0)
    white = (255, 255, 255)

    # initialize the window 
    pygame.init()
    
    width = 750
    height = 750
    display = pygame.display.set_mode((width, height))
    fpsClock = pygame.time.Clock()

    initial_position_parameters = {'pull':(-1, 0, 1.5, 1/3),
                                    'push':(-2.8, -1.5, -2.8, 2/3)}

    (upper_initial_poistion, forearm_initial_position, maxPosition, origin_x) = initial_position_parameters[mode]


    # kinetic initialization
    upper_initial_poistion = upper_initial_poistion
    forearm_initial_position = forearm_initial_position
    hand_initial_position= forearm_initial_position

    #mamximum position is 1.5
    maxPosition = maxPosition
    minPosition = forearm_initial_position

    ## draw the arm
    upperarm = ArmPart('upperarm.png', scale=.7, initial_rotation=upper_initial_poistion)
    forearm = ArmPart('forearm.png', scale=.8, initial_rotation=forearm_initial_position)
    hand = ArmPart('hand.png', scale=1.0, initial_rotation=hand_initial_position)  ##todo : find another hand
    
    origin = (width * origin_x, height / 2)  ##define position of the arm

    # position regulization
    position, scale = positionRegularization(position, maxPosition, minPosition)
    scale = abs(scale)

    # for i in range(len(differentialForce1)):
    for i in range(len(position)):

        currentPosition = position[i]

        display.fill(white)

        # apply position
        ua_image, ua_rect = upperarm.set_position(upper_initial_poistion) 
        fa_image, fa_rect = forearm.set_position(currentPosition) 
        h_image, h_rect = hand.set_position(currentPosition)
    
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


mode = 'push' # 'pull' or 'push'
armMove(mode, position)