"""Experiment 11: Create a Pandas Series with ten random numbers -- CO-4"""

import numpy as np
import pandas as pd

np.random.seed(42)                               # same numbers each run
numbers = np.random.randint(1, 100, size=10)     # ten ints between 1 and 99

s = pd.Series(numbers, name="Random Numbers")

print(s)
print("\nMax   :", s.max())
print("Min   :", s.min())
print("Mean  :", s.mean())
print("\nSummary:\n", s.describe())
