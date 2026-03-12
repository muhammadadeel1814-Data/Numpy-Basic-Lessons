"""
NumPy Array Creation, Indexing, Shape, and Dimensions
-----------------------------------------------------

This script demonstrates:

1. Creating a 3D NumPy array
2. Accessing elements using indexing
3. Using `.shape` to determine the structure of the array
4. Using `.ndim` to determine the number of dimensions

Author: Muhammad Adeel
"""

import numpy as np


# ---------------------------------------------------
# Creating a 3D Array
# ---------------------------------------------------
# Structure explanation:
# Axis 0 → Blocks
# Axis 1 → Rows
# Axis 2 → Columns

array = np.array([
    [['A','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l']],
    [['m','n','o'], ['p','q','r'], ['s','t','u'], ['v','w','x']]
])


# ---------------------------------------------------
# Indexing Elements from the Array
# ---------------------------------------------------
# Index format for a 3D array:
# array[block, row, column]

# Extracting characters to build the word "Adeel"

word = (
    array[0,0,0] +   # A
    array[0,1,0] +   # d
    array[0,1,1] +   # e
    array[0,1,1] +   # e
    array[0,3,2]     # l
)

print("Extracted Word:", word)


# ---------------------------------------------------
# Array Information
# ---------------------------------------------------

print("\n")

# Shape of the array
# .shape returns the size of each dimension
print("Array Shape (Axis, Rows, Columns):", array.shape)

# Number of dimensions
# .ndim returns how many dimensions the array has
print("Array Dimensions (.ndim):", array.ndim)