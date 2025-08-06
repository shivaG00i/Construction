# ✅ 10. Tile Calculation
# Problem:
# Each tile is 2 sq. ft. A room is L x B feet. How many tiles required (round up)?

# Quantity/Units Required= [Total area to Cover/ area per unit ]


import math


def tiles_required(length: int, breadth: int, tile_area: int = 2) -> int:
    if length <= 0 or breadth <= 0 or tile_area <= 0:
        raise ValueError("Length, breadth, and tile area must be positive")

    room_area = length * breadth
    return math.ceil(room_area / tile_area)

print(tiles_required(10, 12))  # Output: 60

