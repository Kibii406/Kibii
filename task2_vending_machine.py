# TASK 2: Vending Machine Change Calculator
# Soda costs 75 cents. Coins: 1c, 5c, 10c, 25c.
# Rules: Output exact change using FEWEST coins possible.
# Constraint: ONLY if/else — no loops, no arrays.
#
# HAND-WORKED EXAMPLE (change = 40 cents):
#   Step 1: Can we use a 25c? 40 >= 25 → YES → 1 quarter, remainder = 15
#   Step 2: Can we use a 10c? 15 >= 10 → YES → 1 dime,    remainder = 5
#   Step 3: Can we use a 5c?   5 >= 5  → YES → 1 nickel,  remainder = 0
#   Step 4: Pennies = 0
#   Total coins: 3  (25 + 10 + 5)

try:
    inserted = int(input("Enter amount inserted (in cents): "))
except ValueError:
    print("Error: enter a whole number.")
    exit()

COST = 75

if inserted < COST:
    print(f"Not enough money. You need at least {COST} cents. You inserted {inserted}.")
else:
    change = inserted - COST

    print(f"\nInserted : {inserted}c")
    print(f"Cost     : {COST}c")
    print(f"Change   : {change}c")

    # --- Greedy breakdown using only if/else (no loops, no arrays) ---
    quarters = 0
    dimes    = 0
    nickels  = 0
    pennies  = 0

    # Quarters (25c each) — max possible given our coin system is 3
    if change >= 75:
        quarters = 3
        change = change - 75
    elif change >= 50:
        quarters = 2
        change = change - 50
    elif change >= 25:
        quarters = 1
        change = change - 25

    # Dimes (10c each)
    if change >= 30:
        dimes = 3
        change = change - 30
    elif change >= 20:
        dimes = 2
        change = change - 20
    elif change >= 10:
        dimes = 1
        change = change - 10

    # Nickels (5c each) — only 0 or 1 needed after quarters and dimes
    if change >= 5:
        nickels = 1
        change = change - 5

    # Remaining cents → pennies
    pennies = change

    print("\nChange breakdown (fewest coins):")
    print(f"  25c quarters : {quarters}")
    print(f"  10c dimes    : {dimes}")
    print(f"   5c nickels  : {nickels}")
    print(f"   1c pennies  : {pennies}")
    print(f"  Total coins  : {quarters + dimes + nickels + pennies}")

# -------------------------------------------------------------------
# WRITTEN EXPLANATION
# -------------------------------------------------------------------
#
# WHY GREEDY WORKS FOR THIS COIN SYSTEM {1, 5, 10, 25}:
# Each coin is a clean multiple of smaller coins (25 = 5×5, 10 = 2×5).
# Always picking the largest coin that fits never "traps" you — the
# remaining amount can always be made exactly with smaller coins.
# Example: 30c → 25 + 5 = 2 coins. No better solution exists.
#
# A SYSTEM WHERE GREEDY FAILS:
# Coins: {1, 3, 4} — make change for 6 cents.
#   Greedy picks 4 first → 4 + 1 + 1 = 3 coins.
#   Optimal:              → 3 + 3     = 2 coins.
# The greedy approach overshoots because 4 doesn't combine cleanly with 3.
