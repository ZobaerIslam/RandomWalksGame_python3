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

# Seed set
np.random.seed(78)

# Initialize and populate all_walks
all_walks = []

# Simulate random walk 10 times
for j in range(10):
    
    # Initialize random_walk
    random_walk = [0]
    
    # Set For Loop for run 100 times
    for i in range(100):
        
        # Initialize step: last element in random_walk
        step = random_walk[-1]
        
        # Roll the dice
        dice = np.random.randint(1,7)
        
        # Determine next step
        if dice <= 2 : 
            step = max(0, step - 1)
        elif dice <= 5 :
            step += 1
        else :
            step += np.random.randint(1,7)
            
        # Append next step to random_walk
        random_walk.append(step)
    
    # Append random walk to all_walks
    all_walks.append(random_walk)
    
    
# Convert all_walks to Numpy array
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Transpose np_aw
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
