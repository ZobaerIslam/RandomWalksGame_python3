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

# Simulate random walk 500 times
for j in range(500):
    
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
            step = step + 1
        else :
            step = step + np.random.randint(1,7)
            
        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
            
        # Append next step to random_walk
        random_walk.append(step)
    
    # Append random walk to all_walks
    all_walks.append(random_walk)
    
    
# Convert all_walks to Numpy array
np_aw = np.array(all_walks)

# Transpose np_aw
np_aw_t = np.transpose(np_aw)

# Select last raw from np_aw_t
ends = np_aw_t[100, :]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

# ----Calculate the possibility of win----
# Count greater then 60
count = len(ends[ends >= 60])
chance = (count / 500) * 100
print("The possibility of win: " + str(chance) + "%")