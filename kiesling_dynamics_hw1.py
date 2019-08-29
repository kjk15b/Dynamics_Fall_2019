#!/bin/python
'''
Kolby Kiesling
kjk15b@acu.edu

ENGR 222.01
Programming Homework 1
Problem: 12-86
Aug 27 2019

This program is set to model finding an optimal initial
velocity and angle for kicking a ball over a fence:


  /              |
 /               | 3 m
o________________|
        6 m
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    dx, dy = 6, 3 # Change in positions for x and for y (Meters)
    ay = -9.81 # gravity (m/s^2)
    
    theta_array = np.arange(30, 75, 4) # Create a linearly spacing of theta values
    
    '''
    Theta values are chosen from needing to be larger than atan(3/6)
    while also being less than 90 degress
    '''
    v_init = list() # list to append initial velocities
    
    for i in range(len(theta_array)):
        try:
            # using v^2 = v_o^2 + 2a*dy, we can assume v is zero at the 3m point making it a minimum for the
            # parabolic motion
            v_o = np.sqrt(2 * abs(ay) * dy) / np.sin(theta_array[i] * np.pi / 180)
            print "Initial Velocity:\t{0}\tIncident Angel:\t{1}".format(v_o, theta_array[i])
            v_init.append(v_o)
        except:
            print "\n\n\nError in calculation\n\n\n"
    plt.figure(1)
    plt.title("Required Velocity to Clear a Wall")
    plt.xlabel("Theta [deg]")
    plt.ylabel("Velocity [m/s]")
    plt.plot(theta_array, v_init)
    plt.show()
    
main()