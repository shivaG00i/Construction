# ✅ 9. Window Installation Count
# Problem:
# Each floor has W windows. If a building has F floors, how many windows to install?


def total_windows(floors: int, windows_per_floor: int) -> int:
    if floors < 0 or windows_per_floor < 0:
        raise ValueError("Inputs must be non-negative")
    return floors * windows_per_floor

print(total_windows(5, 10))  # Output: 50
