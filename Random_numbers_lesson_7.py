"""
NumPy Random Number Generation
------------------------------

This script demonstrates how to generate random numbers in NumPy.

Topics covered:
1. Creating a random number generator (RNG)
2. Generating random integers
3. Generating random floating-point numbers
4. Shuffling arrays
5. Selecting random elements using choice()

Author: Muhammad Adeel
"""

import numpy as np


# ---------------------------------------------------
# Creating a Random Number Generator (RNG)
# ---------------------------------------------------

# default_rng() creates a modern random generator
rng = np.random.default_rng(seed=1)


# ---------------------------------------------------
# Random Integer Array
# ---------------------------------------------------
# high is exclusive (not included)

print("Random Integer Array (1-6):")
print(rng.integers(low=1, high=7, size=(3, 3)))


# ---------------------------------------------------
# Random Floating Point Array
# ---------------------------------------------------
# uniform(low, high) generates numbers between the range

np.random.seed(1)

print("\nRandom Floating Point Array (-1 to 1):")
print(np.random.uniform(-1, 1, size=(3, 2)))


# ---------------------------------------------------
# Shuffle an Array
# ---------------------------------------------------

array1 = np.array([1,2,3,4,5,6,7,8,9,10])

rng.shuffle(array1)

print("\nShuffled Array:")
print(array1)


# ---------------------------------------------------
# Random Choice from Array
# ---------------------------------------------------

Meat = np.array(["Goat", "Ibex", "Cow", "Buffalo", "Rooster", "Turkey"])

# Select a random element
Meat = rng.choice(Meat)

print("\nRandom Meat Choice:")
print(Meat)