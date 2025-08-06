# ✅ 6. Paint Requirement Estimator
# Problem:
# Each can of paint covers A square feet. If house area is T, how many cans needed?

# Formula Quantity Needed = Total Work / Capacity per Unit

import math

def paint_cans_required(area: int, coverage_per_can: int) -> int:
    if area <= 0 or coverage_per_can <= 0:
        raise ValueError("Area and coverage per can must be positive")
    return math.ceil(area / coverage_per_can)

print(paint_cans_required(1200, 350))  # Output: 4
