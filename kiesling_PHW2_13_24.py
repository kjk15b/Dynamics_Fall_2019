#!/bin/python

'''
Kolby Kiesling
kjk15b@acu.edu

          o  briefcase starting point
          /
         /. hypotenuse = 5 [m]
        /
       /   30 [deg]
      |
      | h = 2.5 [m]
-------
   r [m]



This program varies the length of the hypotenuse of the upper triangle
to find the distance r that a 60 kg briefcase will travel.
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    track_length = np.arange(1, 15, 1) # vary the hypotenuse of the triangle from 1 to 15 [m]
    gravity = 9.81 # [m/s^2]
    theta = 30 * np.pi / 180 # radians
    mass = 60 # [kg]
    height = 2.5 # [m]
    
    distance = list()
    velocity = list()
    
    for i in range(len(track_length)):
        '''
        From the sum of the forces in the x-direction we can get: a_x = g cos(theta)
        
        To find the launch velocity (x-dir) of the brief case we use:
            v_fx^2 = v_ix^2 + 2 * a_x * dx
        
        dx: change in x position while the briefcase is on the upper triangle
            dx = track_length * cos(theta) -> for brevity I will refer to track length as dr
        
        Initially the briefcase is at rest
            v_fx = sqrt(2 * g cos(theta) * dr * cos(theta))
            v_fx = cos(theta) * sqrt(2 * g * dr)
        
        We now solve for the time of flight
            hf = h_o + v_oy * t + 1/2 a_y * t^2
            
            a_y = g
            hf = 0
            v_oy = 0
        
            hf = 2.5 [m]
        
            hf = 1/2 a_y * t^2
        
            t = sqrt(2 * hf / a_y)
        
        Finally, plug in to find R:
        
        R = Vx * t
        R = cos(theta) * sqrt(2 * g * dr) * sqrt(2 * hf / a_y)
        '''
        
        try:
            t = np.sqrt(2 * height / abs(gravity))
            print "Time:\t{0} [s]\tTrack:\t{1} [m]".format(t, track_length[i])
            Vx =  np.sqrt(2 * gravity * track_length[i])
            distance.append(Vx * t)
            velocity.append(Vx)
            
            print "Velocity:\t{0}[m/s]\tDistance:\t{1}[m]\n".format(Vx, distance[i])
            
        except:
            print "\n\n\nError in calculations\n\n\n"
            
    plt.figure(1)
    plt.title("Briefcase Launch Distance")
    plt.xlabel("Track Length [m]")
    plt.ylabel("Briefcase Distance Traveled [m]")
    plt.plot(track_length, distance)
    
    plt.figure(2)
    plt.title("Briefcase Velocity")
    plt.xlabel("Track Length [m]")
    plt.ylabel("Briefcase X Velocity [m/s]")
    plt.plot(track_length, velocity)
    
    plt.show()
    
    
main()