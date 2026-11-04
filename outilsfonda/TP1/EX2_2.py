import math

def presque_egaux(a, b, tolerance=1e-9):
    return abs(a - b) <= tolerance
print(presque_egaux(0.1 + 0.2, 0.3))
print(presque_egaux(1.0, 1.5))




