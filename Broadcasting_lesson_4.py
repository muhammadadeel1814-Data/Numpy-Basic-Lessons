"""
NumPy Broadcasting
------------------

Broadcasting allows NumPy to perform arithmetic operations on arrays
with different shapes by automatically expanding one of the arrays
so their shapes become compatible.

Broadcasting Rules:
1. Dimensions must either be equal
2. OR one of them must be 1

If one dimension is 1, NumPy "virtually expands" it to match the other array.

Author: Muhammad Adeel
"""

import numpy as np


# ---------------------------------------------------
# Creating Arrays with Different Shapes
# ---------------------------------------------------

# Row vector (1 row, 5 columns)
array = np.array([[1, 2, 3, 4, 5]])

# Column vector (5 rows, 1 column)
array1 = np.array([[6],
                   [7],
                   [8],
                   [9],
                   [0]])


print("Array shape:", array.shape)
print("Array1 shape:", array1.shape)


# ---------------------------------------------------
# Broadcasting Operation
# ---------------------------------------------------
# NumPy expands both arrays virtually to match shape (5,5)

result = array * array1

print("\nBroadcasted Multiplication Result:\n", result)