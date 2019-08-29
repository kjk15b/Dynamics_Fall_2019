#!/bin/python

'''
Kolby Kiesling
kjk15b@acu.edu

08 - 29 - 2019

Sample work from in class.

Two boxes on top of one another


----> P = 6 [lbs]
    ----
   |    | A = 20 [lbs]
    ----
 ----------
|          | B = 50 [lbs]
 ----------

mu = 0.3

'''

import matplotlib.pyplot as plt
import numpy as np

def main():
    g = 32.2 # [ft/s^2]
    p = 6 # [lbs]
    mA = 20 / g # [slugs]
    mB = 50 / g # [slugs]
    mu = 0.3
    Ff = mu * mA * g # find the force of friction on box A
    aA = (p - Ff) / mA # Acceleration of A [ft/s^2]
    aB = (Ff) / mB # Acceleration of B [ft/s^2]
    
    print "Acceleration A:\t{0}\tAcceleration B:{1}".format(aA, aB)
    
    push = np.arange(0, 25, 1)
    accel_A = list()
    accel_B = list()
    
    for i in range(len(push)):
        accel_A.append((push[i] - Ff) / mA) # Acceleration of A [ft/s^2]
        accel_B.append((Ff) / mB) # Acceleration of B [ft/s^2]
        
    plt.figure(1)
    plt.title("Box Accelerations")
    plt.xlabel("Pushing Force [lbs]")
    plt.ylabel("Acceleration [ft/s^2]")
    plt.plot(push, accel_A, color="red", label="Box A")
    plt.plot(push, accel_B, color="blue", label="Box B")
    plt.legend(loc="upper left")
    plt.show()
    
main()