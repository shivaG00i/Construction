
# ✅ 1. House Construction Labor Scheduling
# Problem:
# Given total work W, work per laborer per day R, and number of laborers N,
# calculate number of
# days to finish.
# def calculate_days_to_complete(W: int, R: int, N: int) -> int:
# pass


#formula  Days= W/ R×N

import math

def calculate_days_to_complete(W: int, R: int, N: int) -> int:
    if R <= 0 or N <= 0:
        raise ValueError("Work rate and number of laborers must be positive")
    return math.ceil(W / (R * N))

# 300 units of work, 5 units/day/laborer, 3 laborers
print(calculate_days_to_complete(300, 5, 3))  # Output: 20

