# ✅ 3. Bricks Per Wall
# Problem:
# A single wall requires B bricks. For N walls, how many bricks are needed?

def total_bricks(walls: int, bricks_per_wall: int) -> int:
    if walls < 0 or bricks_per_wall < 0:
        raise ValueError("Number of walls and bricks per wall must be non-negative")
    return walls * bricks_per_wall

print(total_bricks(10, 500))  # Output: 5000
