"""
NumPy Aggregation Functions
---------------------------

Aggregation functions are used to summarize data in an array.
They typically return a single value such as sum, minimum,
maximum, variance, etc.

This script demonstrates:
1. Basic aggregation functions
2. Finding index of min and max values
3. Standard deviation and variance
4. Aggregation along rows and columns using axis

Author: Muhammad Adeel 
"""

import numpy as np


# ---------------------------------------------------
# Creating a 2D NumPy Array
# ---------------------------------------------------

Array = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

print("Original Array:\n", Array)


# ---------------------------------------------------
# Basic Aggregation Operations
# ---------------------------------------------------

print("\nSum of all elements:", np.sum(Array))

print("\nMinimum value:", np.min(Array))

print("\nMaximum value:", np.max(Array))

print("\nIndex of minimum value:", np.argmin(Array))

print("\nIndex of maximum value:", np.argmax(Array))

print("\nStandard Deviation:", np.std(Array))

print("\nVariance:", np.var(Array))


# ---------------------------------------------------
# Aggregation Along Axes
# ---------------------------------------------------

# axis = 0 → column-wise operation
print("\nSum of columns (axis=0):")
print(np.sum(Array, axis=0))

# axis = 1 → row-wise operation
print("\nSum of rows (axis=1):")
print(np.sum(Array, axis=1))