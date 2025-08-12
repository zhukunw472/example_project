# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:52:29 2025

@author: zhuku
"""

'''
Plot all, this is like finalizing the plot so that the scale is correct
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import motordesign_keyelements as fun


# Step 3: For each line, draw circles with center equally spaced on each of the radius
def draw_circles(point, radius=6, color='blue', linestyle='solid'):
    '''
    points are numpy arrays (N, 2) of points on the radius 
    
    Each point is representing a center of the circle. 
    
    '''

        
    # Define the circle
    circle = fun.Circle(radius, point) # Circle here refers to the circle class defined in boarddesign_keyelements
        
    # Draw the circle
    c = plt.Circle(circle.center, circle.radius, fill=False, color=color, linestyle=linestyle)
        
    # Add the current plotted circle to the final plot
    plt.gca().add_patch(c)



def plot_all(x_upper, y_upper, x_lower, y_lower, increment_axis_number):
    '''
    Plot out everything on a graph with proper calibrations of the size of everything
    '''
    
    # Set up the limit in x and y axis 
    plt.xlim(x_lower, x_upper)
    plt.xlim(y_lower, y_upper)
    
    
    # Generate ticks at every 25 units from 0 to 200 in transformed coordinates
    tick_values_x = np.arange(x_lower, x_upper, increment_axis_number)
    tick_values_y = np.arange(y_lower, y_upper, increment_axis_number)
    
    # Ensure 0 is included
    if 0 not in tick_values_x:
        tick_values_x = np.sort(np.append(tick_values_x, 0))
    if 0 not in tick_values_y:
        tick_values_y = np.sort(np.append(tick_values_y, 0))
    
    
    # Set ticks and labels
    ax = plt.gca()
    ax.set_aspect('equal')
    ax.set_xticks(tick_values_x)
    ax.set_xticklabels([str(int(val)) for val in tick_values_x], fontsize=16)
    ax.set_yticks(tick_values_y)
    ax.set_yticklabels([str(int(val)) for val in tick_values_y], fontsize=16)
    
    # Add axis labels with units
    plt.xlabel('x [mm]', fontsize=18)
    plt.ylabel('y [mm]', fontsize=18)
