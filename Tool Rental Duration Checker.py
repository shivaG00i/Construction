# ✅ 8. Tool Rental Duration Checker
# Problem:
# You rent a machine at ₹500/day. You used it for D days.
# If you have ₹B, is it enough?

def is_rental_possible(days: int, budget: int) -> bool:
    if days < 0 or budget < 0:
        raise ValueError("Days and budget must be non-negative")

    total_cost = 500 * days
    return total_cost <= budget

print(is_rental_possible(5, 3000))  # Output: True
print(is_rental_possible(7, 3000))  # Output: False
