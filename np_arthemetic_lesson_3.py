"""
NumPy Arithmetic Operations and Comparison Operators
----------------------------------------------------

This script demonstrates:

1. Scalar arithmetic with NumPy arrays
2. Built-in NumPy mathematical functions
3. A small exercise (area of a circle)
4. Element-wise arithmetic between arrays
5. Comparison operators on arrays

Author: Muhammad Adeel
"""

import numpy as np


# ---------------------------------------------------
# Creating a NumPy Array
# ---------------------------------------------------

array = np.array([1, 2, 3])


# ---------------------------------------------------
# Scalar Arithmetic
# ---------------------------------------------------
# Scalar operations apply the operation to every
# element in the array.

print("Array + 1:\n", array + 1)
print("\nArray * 3:\n", array * 3)
print("\nArray / 2:\n", array / 2)
print("\nArray - 1:\n", array - 1)
print("\nArray ** 5 (power):\n", array ** 5)


# ---------------------------------------------------
# NumPy Built-in Mathematical Functions
# ---------------------------------------------------

array1 = np.array([1.999, 2.999, 3.2476532])

print("\nSquare Root of array:\n", np.sqrt(array))

print("\nRounded values:\n", np.round(array1))

print("\nFloor values (round down):\n", np.floor(array1))

print("\nCeil values (round up):\n", np.ceil(array1))

print("\nValue of Pi:\n", np.pi)


# ---------------------------------------------------
# Exercise: Area of a Circle
# ---------------------------------------------------
# Formula: Area = π * r²

radius = np.array([1, 2, 3])
print("\nArea of circles with radius 1,2,3:\n", np.pi * radius**2)


# ---------------------------------------------------
# Element-wise Arithmetic
# ---------------------------------------------------
# Operations between arrays happen element by element.

print("\nArray - array1:\n", array - array1)
print("\nArray + array1:\n", array + array1)
print("\nArray * array1:\n", array * array1)
print("\nArray / array1:\n", array / array1)
print("\nArray ** array1:\n", array ** array1)


# ---------------------------------------------------
# Comparison Operators
# ---------------------------------------------------
# These return Boolean arrays (True/False).

print("\narray < 2:\n", array < 2)
print("\narray == 2:\n", array == 2)
print("\narray >= 2:\n", array >= 2)