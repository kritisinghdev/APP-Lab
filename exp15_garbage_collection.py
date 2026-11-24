"""Experiment 15: Python's automatic garbage collection and manual control
using the gc module  -- CO-5

Python uses (1) reference counting and (2) a cyclic garbage collector
that finds groups of objects referring to each other.
"""

import gc
import sys


class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"  Object {self.name} deleted")


# ---------- 1. Reference counting ----------
print("1) Reference counting")
a = Node("A")
print("  Reference count of A:", sys.getrefcount(a) - 1)   # -1 for the argument
b = a
print("  After b = a         :", sys.getrefcount(a) - 1)
del b
del a                                  # count hits 0 -> deleted immediately

# ---------- 2. Circular reference ----------
print("\n2) Circular reference (reference counting cannot free these)")
gc.disable()                           # stop automatic collection
x = Node("X")
y = Node("Y")
x.other = y
y.other = x                            # x <-> y point to each other
del x, y
print("  x and y deleted, but objects still exist in memory")

collected = gc.collect()               # manual collection
print("  gc.collect() found unreachable objects:", collected)
gc.enable()

# ---------- 3. Useful gc functions ----------
print("\n3) gc module information")
print("  GC enabled?        :", gc.isenabled())
print("  Thresholds (gen0,1,2):", gc.get_threshold())
print("  Current counts     :", gc.get_count())
print("  Stats per generation:")
for i, stat in enumerate(gc.get_stats()):
    print(f"    Generation {i}: {stat}")

# ---------- 4. Changing the threshold ----------
gc.set_threshold(500, 5, 5)
print("\n4) New thresholds:", gc.get_threshold())
