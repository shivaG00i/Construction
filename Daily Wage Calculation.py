# ✅ 5. Daily Wage Calculation
# Problem:
# A worker works H hours/day for D days. If hourly rate is R, what is total pay?



def calculate_wage(hours_per_day: int, days: int, rate: int) -> int:
    if hours_per_day < 0 or days < 0 or rate < 0:
        raise ValueError("Hours, days, and rate must be non-negative")
    return hours_per_day * days * rate

print(calculate_wage(8, 25, 100))  # Output: 20000
