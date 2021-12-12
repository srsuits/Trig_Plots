# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 15:19:22 2021

@author: shelb
"""

import matplotlib.pyplot as plt
import numpy as np

# create x coordinates, empty y coordinate numpy array
x = np.linspace(0, 2*np.pi, 100)
#x = np.array([])
y = np.array([])


def get_coords(function, y):
    # ensure all input is in lowercase
    function = function.lower()
    
    if function == 'cosine':
        y = np.cos(x)
    elif function == 'sine':
        y = np.sin(x)
    elif function == 'tangent':
        y = np.tan(x)
    elif function == 'cotangent':
        y = np.arctan(x)
    #elif function == 'cosecant':
    #    y = np.arcsin(x)
    #elif function == 'secant':
    #    y = np.arccos(x)
    # error thrown if non alpha chars present in user input
    elif not(function.isalpha()):
        print("\nERROR: type only letters")
    # error thrown if user input does not match options
    else:
        print("\nERROR: please choose one of the options listed")
    
    return y
        



# until input matches requirements
while y.size == 0:
    # print function options
    print("Functions: \n\t sine \n\t cosine \n\t tangent \n\t cotangent")
    function = input("Choose a trig funciton from the list above: ")
    
    # function to perform trig fucntion
    y = get_coords(function, y)
    
# plot x and y coordinates
plt.plot(x, y)

