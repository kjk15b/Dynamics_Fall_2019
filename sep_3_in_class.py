#!/bin/python

'''

Kolby Kiesling
kjk15b@acu.edu


In class work 09 - 03 - 2019
'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    '''
    Process for solving problems in Dynamics:
    1) FBD + KD
    2) Write Vector Equations
    3) Split Vectors + Write Components
    4) Solve
    -----------------------------------------
      -
     |_|    
      -  /
     |_|/
       /
      /
       -------
    Two boxes stacked on top of each other, box A is on top and box B in on the bottom, A and B are connected to a pully at the top of the inclined plane.
    
    mu_ab = [0.2]
    ma = 10 [kg]
    mb = 20 [kg]
    theta = 30 [deg]
    
    What are the accelerations? 
    
    Distances from datum: Sa, Sb
    length = Sa + Sb + junk [Stuff we don't care about]
    d/dt -> 0 = -Va - Vb
    Aa = -Ab (Accelerations are equal but opposite) -> Describes how the system moves
    [Kinematics of a pulley]
    
    '''
    
    theta = np.arange(0, 75, 1)
    a_accel = list()
    b_accel = list()
    ma, mb = 10, 20 # [kg]
    mu = 0.2
    mass = ma + mb
    g = 9.81 # [m/s^2]
    
    
    for i in range(len(theta)):
        a = -ma * g * pow(mass, -1) * np.sin(theta[i] * np.pi / 180)
        b = -mb * g * pow(mass, -1) * np.sin(theta[i] * np.pi / 180)
        c = -ma * g * pow(mass, -1) * np.cos(theta[i] * np.pi / 180)
        
        a_accel.append(a + b + c)
        b_accel.append(-1 * (a + b + c))
        
    plt.figure(1)
    plt.title("Sliding Box Accelerations")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Acceleration [m/s^2]")
    plt.plot(theta, a_accel, color='red', label="Box A")
    plt.plot(theta, b_accel, color='blue', label="Box B")
    plt.legend(loc="upper left")
    plt.show()
    
    
    
    
main()