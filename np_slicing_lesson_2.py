"""
NumPy Array Slicing (Rows and Columns)
--------------------------------------

This script demonstrates how slicing works in NumPy arrays.

Topics covered:
1. Row slicing
2. Column slicing
3. Reverse slicing
4. Stepping in slices
5. Slicing rows and columns together

Important rule:
array[start : end : step]

- start → index where slicing begins
- end → index where slicing stops (exclusive)
- step → how many positions to move each time

Aurthor: Muhammad Adeel
"""

import numpy as np


# ---------------------------------------------------
# Creating a 2D Array
# ---------------------------------------------------

array = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
])

print("Original Array:\n", array)


# ---------------------------------------------------
# Row Slicing
# ---------------------------------------------------

# Default stepping (step = 1)
print("\nDefault stepping (prints rows normally):\n", array[0:6:1])

# Step = 2 (every second row)
print("\nStepping by 2 (every second row):\n", array[0:6:2])

# Reverse rows
print("\nReverse rows:\n", array[::-1])

# Reverse rows with step = -2
print("\nReverse rows with step -2:\n", array[::-2])


# ---------------------------------------------------
# Column Slicing
# ---------------------------------------------------

# First column
print("\nFirst column:\n", array[:,0])

# Range of columns (1st and 2nd)
print("\nFirst two columns:\n", array[:,0:2])

# Columns with stepping
print("\nColumns with step 3 (1st and 4th column):\n", array[:,0:5:3])

# Reverse columns
print("\nReverse all columns:\n", array[:,::-1])

# Reverse columns with step -2
print("\nReverse columns with step -2:\n", array[:,::-2])


# ---------------------------------------------------
# Slicing Rows and Columns Together
# ---------------------------------------------------

# 2x2 submatrix
print("\n2x2 matrix slice:\n", array[0:2:1, 0:2:1])

# 4x4 submatrix
print("\n4x4 matrix slice:\n", array[0:4:1, 0:4:1])