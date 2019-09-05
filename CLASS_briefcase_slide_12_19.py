#!/bin/python

'''
Kolby Kiesling
kjk15b@acu.edu

Work in class 09 - 05 - 2019
In class review and introduction of cylindrical coordinates

Help with some homework problems
    1) FBD + KD
    2) F = ma
    3) Split into components [# of equations, 2D -> 2 equations, generally]
    4) Decompose vectors
    5) Solve
        5a) # eq = # unkn.
        5b) Go to kinematic equations, relate two accelerations

Problem 13-19

Briefcase going down a ramp
weight = 40 [lbs]

\.   A   
 \o
  \
   \.   C
    |.    B
    ------

AC = 20 [ft]
g = 32.2 [ft/s^2]
B = 4 [ft]
mu = 0.2
Vo = 10 [ft/s]

Find the distance from the inclined plane the briefcase will land
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    dr = 20 # [ft]
    theta = 30 # [deg]
    dy = 4 # [ft]
    g = 32.2 # [ft/s^2]
    Vo = 10 # [ft/s]
    mu = 0.2
    
    ax = g * np.sin(theta * np.pi / 180) - mu * g * np.cos(theta * np.pi / 180)
    
    dx = dr * np.cos(theta * np.pi / 180)
    
    vfx = np.sqrt(pow(Vo * np.sin(theta * np.pi / 180), 2) + 2 * ax * dx)
    
    time = np.sqrt(2 * dy / g)
    
    xf = vfx * time
    
    print "Final briefcase position:\t{0} [ft]".format(xf)
    
    theta_array = np.arange(0, 85, 1)
    xF = list()
    
    for i in range(len(theta_array)):
        ax = g * np.sin(theta_array[i] * np.pi / 180) - mu * g * np.cos(theta_array[i] * np.pi / 180)
        dx = dr * np.cos(theta_array[i] * np.pi / 180)
        
        vfx = np.sqrt(pow(Vo * np.sin(theta_array[i] * np.pi / 180), 2) + 2 * ax * dx)
        
        time = np.sqrt(2 * dy / g)
        
        xF.append(vfx * time)
        
        print "Angle:\t{0} [deg]\t|\tPosition:\t{1} [ft]".format(theta_array[i], vfx * time)
        
    plt.figure()
    plt.title("Briefcase Final Position vs Inclined Angle")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Position [ft]")
    plt.plot(theta_array, xF)
    plt.show()
        
main()