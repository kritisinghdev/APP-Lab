"""Experiment 10: Create a one-dimensional NumPy array containing 1 to 10 -- CO-4"""

import numpy as np

arr = np.arange(1, 11)          # start=1, stop=11 (excluded), so 1..10

print("Array     :", arr)
print("Shape     :", arr.shape)
print("Dimension :", arr.ndim)
print("Data type :", arr.dtype)
print("Sum       :", arr.sum())
print("Mean      :", arr.mean())
print("Squares   :", arr ** 2)

# Another way: np.linspace(1, 10, 10, dtype=int)
