# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:34:01 2025

@author: zhuku
"""

'''
Define the key elements of the motor setup
'''

import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Define the board class (store board corners' coordinates)
class Board:
    
    # Initiate board
    def __init__(self, origin, length, width): # Origin here doesn't necessarily represent the overall origin
        '''
        Define the origin and the lenght and width 
        '''
        
        self.origin = origin
        self.length = length
        self.width = width
    
    
    # Draw the board draw function will be used both in the parental class and inheritance class
    def draw(self, facecolor='gray'):
        board = patches.Rectangle((self.origin[0], self.origin[1]), self.length,  self.width, 
                                  linewidth=1, edgecolor='black', facecolor=facecolor)
        plt.gca().add_patch(board)
        


class Circle:
    
    # Initiate a circle where circle_id is the circle index
    def __init__(self, radius, center):
        '''
        circle_id: a number
        radius: a number
        center: a tuple of x and y coordinate of a point
        '''
        self.radius = radius
        self.center = center
        
    def draw(self, facecolor='gray', edgecolor='black'):
        circle = patches.Circle(self.center, self.radius, linewidth=1,
                                edgecolor=edgecolor, facecolor=facecolor)
        plt.gca().add_patch(circle)
    
    
        


        