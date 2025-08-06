# ✅ 4. Water Tank Fill Time
#
# Problem:
# A water tank has capacity C liters. A pipe fills F liters per minute.
# How many minutes to fill?

# formula Time = (Work or Distance or Volume)/ Rate
#

import math

def fill_time(capacity: int, flow_rate: int) -> int:
    if capacity <= 0 or flow_rate <= 0:
        raise ValueError("Capacity and flow rate must be positive")
    return math.ceil(capacity / flow_rate)

print(fill_time(1000, 30))  # Output: 34
