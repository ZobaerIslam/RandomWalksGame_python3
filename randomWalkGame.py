#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 19:36:53 2020

@author: zobaer islam
"""

# Import numpy
import numpy as np

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Initialize random_walk
random_walk = [0]

# Set for loop for run 100 times
for i in range(100):
    
    # Initialize step: last element in random_walk
    step = random_walk[-1]
    
    # Roll the dice
    dice = np.random.randint(1,7)
    
    # Determine next step
    if dice <= 2 : 
        step -= 1
    elif dice <= 5 :
        step += 1
    else :
        step += np.random.randint(1,7)
        
    # Append next step to random_walk
    random_walk.append(step)
    
# Print random_walk
print(random_walk)

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()
