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

