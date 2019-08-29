#!/bin/python
'''
Kolby Kiesling
kjk15b@acu.edu

ENGR 222.01
Programming Homework 1
Problem: 12-90
Aug 27 2019

This program finds the distance that a ball
can be launched at a given angle, theta.

  / \             
 /   \            
o_____o
  R [m]
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    ay = -9.81 # [m/s^2]
    v_o = 10 # [m/s]
    theta = np.arange(30, 60, 1)
    
    '''
    Background:
    We know that the change in height is zero, so we can use the quadratic formula to find tof
    
    this gives t = (2v_o sin(theta)) / ay
    
    We use this time to plug into dx = v_o * cos(theta) * t
    
    The final formula looks something like:
    
    dx = R = (v_o * cos(theta) * (2 * v_o * sin(theta)) / (ay))
    '''
    dx = list() # list for appending distances while iterating
    
    for i in range(len(theta)):
        try:
            r = (pow(v_o, 2) * 2 * np.cos(theta[i] * np.pi / 180) * np.sin(theta[i] * np.pi / 180)) / abs(ay)
            print "Distance:\t{0}[m]\tAngle:\t{1}[deg]".format(r, theta[i])
            dx.append(r)
        except:
            print "\n\n\nError\n\n\n"
        
    plt.figure(1)
    plt.title("Separation Distance of Ball Launched")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Distance [m]")
    plt.plot(theta, dx, linestyle="-.", color="red")
    plt.scatter(theta, dx)
    plt.show()
    
main()