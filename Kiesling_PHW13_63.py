#!/bin/python
'''
P13-63

Kolby Kiesling
kjk15b@acu.edu

o--------|
 \       |
  v      |

Find the tension in the rope as the ball goes from 0 to 2 pi

For the tangent direction we get:
    T * sin(theta) + Fg * cos(theta) = ma_t
        where a_t -> 0 for constant speed case

    thus we get:
    
    T * sin(theta) = -Fg * cos(theta)

    T = -Fg cos(theta) / sin(theta)
    T = -Fg cot(theta)
'''
import numpy as np
import matplotlib.pyplot as plt

def projectile():
    theta_array = np.arange(0, np.pi, 0.01)
    w = 5 # [lbs]
    tension = list()
    
    for i in range(len(theta_array)):
        try:
            T = -5 / np.tan(theta_array[i]) # find our tension
            print("Tension:\t{} [N]\n----------".format(T))
            tension.append(abs(T))
        except ValueError:
            pass
    
    plt.figure(1)
    plt.title("Tension in a Rope")
    plt.xlabel("Angle [deg]")
    plt.ylabel("Tension [N]")
    plt.plot(theta_array, tension, color="red")
    plt.show()
    
if __name__ == '__main__':
    projectile()
