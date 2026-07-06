def is_leap_year(year):
    # Reject impossible input
    if year <= 0:
        print(f"Error: {year} is not a valid year. Please enter a positive integer.")
        return None

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

# --- Main input ---
try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Error: Please enter a whole number.")
    exit()

result = is_leap_year(year)
if result is True:
    print(f"{year} IS a leap year.")
elif result is False:
    print(f"{year} is NOT a leap year.")
print("\n--- Test Cases ---")

# Test 1: 2024 — Basic rule: divisible by 4, not a century year → LEAP
r = is_leap_year(2024)
print(f"2024 → {'LEAP' if r else 'NOT leap'}  | Why: divisible by 4, not a century year")

# Test 2: 1900 — Tricky: divisible by 4 AND by 100 but NOT 400 → NOT LEAP
# Many people wrongly assume 1900 was a leap year.
r = is_leap_year(1900)
print(f"1900 → {'LEAP' if r else 'NOT leap'}  | Why: century year not divisible by 400")

# Test 3: 2000 — Special override: divisible by 400 → LEAP
# This tests that the 400-rule correctly overrides the 100-rule.
r = is_leap_year(2000)
print(f"2000 → {'LEAP' if r else 'NOT leap'}  | Why: divisible by 400 — overrides century rule")

# Edge case: negative year
print("\n--- Edge Case ---")
is_leap_year(-10)
is_leap_year(0)
