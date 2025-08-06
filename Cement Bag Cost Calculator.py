# ✅ 2. Cement Bag Cost Calculator
# Problem:
# You need X cement bags for building. Each bag costs Y rupees. What’s the total cost?


def cement_cost(bags: int, cost_per_bag: int) -> int:
    if bags<=0 or cost_per_bag<=0:
         raise ValueError("Quantity and price must be non-negative")
    result=bags*cost_per_bag
    return result

print(cement_cost(50, 320))  # Output: 16000
