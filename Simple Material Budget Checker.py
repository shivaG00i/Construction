# ✅ 7. Simple Material Budget Checker
# Problem:
# You have budget rupees. Cement = ₹300/bag, Brick = ₹5/unit. If you buy c cement bags and b
# bricks, can you afford it?


def can_afford(budget: int, cement_bags: int, bricks: int) -> bool:
    if budget < 0 or cement_bags < 0 or bricks < 0:
        raise ValueError("Inputs must be non-negative")

    total_cost = (300 * cement_bags) + (5 * bricks)
    return total_cost <= budget

print(can_afford(5000, 10, 100))  # Output: True
print(can_afford(3000, 10, 100))  # Output: False
