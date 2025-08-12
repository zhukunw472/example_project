# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 23:24:44 2025

@author: zhuku
"""

'''
main file for the design of the automated lifting setup
'''

'''
import motordesign_keyelements as fun1
import motordesign_functions as fun

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Motor design

# ADJUSTABLE ELEMENTS
# Set the origin
origin = [0, 0]
# First aluminum piece
aluminum1_height = 212 # [mm]
# Second aluminum piece
#aluminum2_height = 200 # [mm]
# Distance between two motor frames
dist_1 = 50
# Distance between motor frame and experiment tank aluminum shelf
dist_2 = 100
# Distance between two frames under acrylic base
dist_3 = 368


# Third aluminum piece
aluminum3_height = 200 # aluminum 3 and 4 are identical
# Frame thickness always the same
frame_width = 30 
# How high I want to set the second piece (horizontal aluminum frame) the lower bottom of the horizontal frame
aluminum2_height = 550 
# Distance between aluminum piece 1 and the setup (left edge)
dist_frame_setup = 100 
# Styrofoam board length
styrofoam_length = 428
styrofoam_width = 155
# motor's acrylic base size (mabs)
motor_length = 110
motor_width = 70

arm_length = 300
arm_width = 20

# Plot range
x_lower = -200
x_upper = 800
y_lower = -200
y_upper = 800
increment_axis_number = 50

# Fixed parameter
full_tank_width_withedge = 428
acrylic_bottom_length = 428
acrylic_bottom_thickness = 12


# Create figure
plt.figure(figsize=(20, 20), dpi=300)

# Step 1: Draw all the aluminum frames
frames = [fun1.Board(origin, frame_width, aluminum1_height), # Piece 1
          fun1.Board([origin[0]+frame_width+dist_1, origin[1]], frame_width, aluminum1_height), # Piece 2
          fun1.Board([origin[0]+2*frame_width+dist_1+dist_2, origin[1]], frame_width, aluminum3_height), # Piece 3
          fun1.Board([origin[0]+3*frame_width+dist_1+dist_2+dist_3, origin[1]], frame_width, aluminum3_height)] # Piece 4
for f in frames:
    f.draw()


# Step 2: Draw all the acrylic bottom (底座 for the acrylic) (Piece 5)
acrylic_bottom = fun1.Board([origin[0]+2*frame_width+dist_1+dist_2, origin[1]+aluminum3_height], 
                            acrylic_bottom_length, acrylic_bottom_thickness)
acrylic_bottom.draw(facecolor='lightgray')

# Step 3: Plot the styrofoam board (Piece 6)
styrofoam = fun1.Board([origin[0]+2*frame_width+dist_1+dist_2, origin[1]+aluminum3_height+acrylic_bottom_thickness], styrofoam_length, styrofoam_width)
styrofoam.draw(facecolor='violet')

# Step 4: Rectangle for motor (Piece 7)
motor = fun1.Board([origin[0], origin[1]+aluminum1_height], motor_length, motor_width)
motor.draw(facecolor='black')

# Step 5: The bar/arm connects the motor to styrofoam board
arm = fun1.Board([origin[0]+0.5*motor_length, origin[1]+aluminum1_height+0.2*motor_width], arm_length, arm_width)
arm.draw(facecolor='bisque')
    
# Finalize the plot with the right dimensions
fun.plot_all(x_upper, y_upper, x_lower, y_lower, increment_axis_number)
'''











import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D
from matplotlib import animation
import numpy as np

# -------------------------- Setup Parameters --------------------------
origin = [0, 0]
aluminum1_height = 212
aluminum3_height = 200
frame_width = 30
dist_1 = 50
dist_2 = 80
dist_3 = 368
acrylic_bottom_thickness = 12
styrofoam_length = 428
styrofoam_width = 155
motor_length = 110
motor_width = 70
arm_length = 300
arm_width = 20

x_lower = -200
x_upper = 800
y_lower = -200
y_upper = 900
# -------------------------- Static Elements --------------------------
fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
ax.set_xlim(x_lower, x_upper)
ax.set_ylim(y_lower, y_upper)
ax.set_aspect('equal')
ax.set_xlabel('x [mm]')
ax.set_ylabel('y [mm]')

# Aluminum Frames
frames = [
    patches.Rectangle((origin[0], origin[1]), frame_width, aluminum1_height, facecolor='dimgray'),
    patches.Rectangle((origin[0] + frame_width + dist_1, origin[1]), frame_width, aluminum1_height, facecolor='dimgray'),
    patches.Rectangle((origin[0] + 2 * frame_width + dist_1 + dist_2, origin[1]), frame_width, aluminum3_height, facecolor='dimgray'),
    patches.Rectangle((origin[0] + 3 * frame_width + dist_1 + dist_2 + dist_3, origin[1]), frame_width, aluminum3_height, facecolor='dimgray')
]
for frame in frames:
    ax.add_patch(frame)

# Acrylic Base
acrylic_x = origin[0] + 2 * frame_width + dist_1 + dist_2
acrylic_y = origin[1] + aluminum3_height
acrylic_bottom = patches.Rectangle((acrylic_x, acrylic_y), styrofoam_length, acrylic_bottom_thickness, facecolor='lightgray')
ax.add_patch(acrylic_bottom)

# Motor Base
motor_x = origin[0]
motor_y = origin[1] + aluminum1_height
motor = patches.Rectangle((motor_x, motor_y), motor_length, motor_width, facecolor='black')
ax.add_patch(motor)

# -------------------------- Rotating Elements --------------------------
# Arm and foam initial position
arm_x = origin[0] + 0.5 * motor_length
arm_y = origin[1] + aluminum1_height + 0.2 * motor_width
foam_x = acrylic_x
foam_y = acrylic_y + acrylic_bottom_thickness
fix_pt1 = (acrylic_x+frame_width, arm_y+0.5*arm_width)
fix_pt2 = (acrylic_x+3*frame_width, arm_y+0.5*arm_width)
fix_pt_radius = 2

# Rotation center = left end center of the arm
rotation_center = (arm_x, arm_y + arm_width / 2)

# Arm and styrofoam (will rotate)
foam_rect = patches.Rectangle((foam_x, foam_y), styrofoam_length, styrofoam_width, color='violet', zorder=1)
arm_rect = patches.Rectangle((arm_x, arm_y), arm_length, arm_width, color='bisque', zorder=2)

# Fixing points on the styrofoam 
fix_pt1 = patches.Circle(fix_pt1, fix_pt_radius, zorder=3)
fix_pt2 = patches.Circle(fix_pt2, fix_pt_radius, zorder=3)

ax.add_patch(foam_rect)
ax.add_patch(arm_rect)
ax.add_patch(fix_pt1)
ax.add_patch(fix_pt2)

# -------------------------- Animation Function --------------------------
def animate(i):
    angle = i  # degrees
    t = Affine2D().rotate_deg_around(rotation_center[0], rotation_center[1], angle)
    arm_rect.set_transform(t + ax.transData)
    foam_rect.set_transform(t + ax.transData)
    fix_pt1.set_transform(t + ax.transData)
    fix_pt2.set_transform(t + ax.transData)
    return arm_rect, foam_rect, fix_pt1, fix_pt2

# -------------------------- Create Animation --------------------------
ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 50, 50), interval=30, blit=True, repeat=False)

plt.show()

