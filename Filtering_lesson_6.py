"""
Filtering Elements from a NumPy Array
-------------------------------------

This lesson demonstrates how to filter elements from a NumPy array
based on specific conditions.

We will cover two main techniques:

1. Boolean Indexing
   - Selects elements that satisfy a condition.
   - Returns a flattened (1D) array.
   - The original shape of the array is lost.

2. np.where()
   - Applies a condition to every element.
   - Keeps the original shape of the array.
   - Replaces values that do not satisfy the condition.

Author: Muhammad Adeel
"""

import numpy as np

# ---------------------------------------------------
# Creating a NumPy array representing ages
# ---------------------------------------------------

Age = np.array([
    [11, 12, 31, 41],
    [51, 61, 17, 81],
    [91, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
])

print("Original Age Array:\n", Age)


# ---------------------------------------------------
# Method 1: Boolean Filtering
# ---------------------------------------------------
# This method returns only the values that satisfy
# the condition, but it flattens the array.

# Teenagers (age < 18)
teenagers = Age[Age < 18]
print("\nTeenagers (Age < 18):", teenagers)

# Adults (18 to 33)
adults = Age[(Age >= 18) & (Age <= 33)]
print("\nAdults (18 - 33):", adults)

# Old people (age > 65)
old = Age[Age > 65]
print("\nOld (Age > 65):", old)


# ---------------------------------------------------
# Note:
# In Boolean filtering, the shape of the original
# array is lost because the result becomes a 1D array.
# ---------------------------------------------------


# ---------------------------------------------------
# Method 2: Using np.where()
# ---------------------------------------------------
# np.where keeps the original array shape.

teenagers_matrix = np.where(Age < 18, Age, np.nan)

print("\nTeenagers Matrix (using np.where):")
print(teenagers_matrix)


# ---------------------------------------------------
# Explanation of np.where()
# ---------------------------------------------------
# Syntax:
# np.where(condition, value_if_true, value_if_false)
#
# condition      -> Age < 18
# value_if_true  -> Age
# value_if_false -> np.nan
#
# If the condition is True, the age value is kept.
# If False, it is replaced with NaN.