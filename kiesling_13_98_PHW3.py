#!/bin/python

'''
Kolby Kiesling
Dynamics 13 - 98

09 / 12 / 2019

This program models a rotating arm:

     o
    /
   /
  /
 /\
/  \

Determine the force of the rod on the cylinder and the normal force

Mass of cylinder: 0.5 [kg]
theta = 30 [deg]
constant angular velocity theta_d = 2 [rad/s]

The particle only makes contact with one of the sides of the wall

        o|
        / -> Experiencing normal from one wall and force from rod


'''
import numpy as np
import matplotlib.pyplot as plt

def main():
    mass = 0.5 # [kg]
    g = 9.81 # [m/s^2]
    dx = 0.5 # [m]
    theta_d = 2 # [rad/s]
    
    theta = np.arange(1, 75, 1) # create my range of angle values
    
    Fr = list()
    Fn = list()
    
    for i in range(len(theta)):
        try:
            # Finding R values
            r = dx / np.cos(theta[i] * np.pi / 180) # find the length of the arm
            r_d = theta_d * dx * np.tan(theta[i] * np.pi / 180) # find r dot
            secant = 1 / np.cos(theta[i] * np.pi / 180)
            
            r_dd = (r_d * pow(theta_d, 2) * dx * np.tan(theta[i] * np.pi / 180)) + (r * pow(secant, 2) * pow(theta_d, 2))
            
        
            Fg_ur = mass * g * np.sin(theta[i] * np.pi / 180) # Force of gravity in {ur} direction
            F_ar = mass * (r_dd - 2 * (r * pow(theta_d, 2))) # Sum force in {ur}
        
            Fn.append((F_ar + Fg_ur) / np.cos(theta[i] * np.pi / 180))
        
            # Solve for Fr
            Fg_ut = mass * g * np.cos(theta[i] * np.pi / 180)
            F_ut = mass * (2 * r_d * theta_d)
        
            Fn_ut = Fn[i] * np.sin(theta[i] * np.pi / 180)
        
            Fr.append(Fn_ut + Fg_ut + F_ut) # Calculate the force
        
            print("FN:\t{0}[N]\tFR:\t{1}[N]".format(Fn[i], Fr[i]))
            
        except:
            print("Error in calculation\n\n\n")
    
    plt.figure(1)
    plt.title("Forces as a Function of Theta [13-98]")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Force [N]")
    plt.plot(theta, Fn, color="red", label="Normal Force")
    plt.plot(theta, Fr, color="blue", label="Rod Force")
    plt.legend(loc="upper left")
    plt.show()
    
main()
        