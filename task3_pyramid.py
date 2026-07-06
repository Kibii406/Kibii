try:
    n = int(input("Enter n: "))
except ValueError:
    print("Please enter an integer.")
    exit()

if n <= 0:
    print("Please enter a positive integer.")
else:
    if n % 2 != 0:
        # ---- SOLID PYRAMID (odd n) ----
        print(f"\nSolid Pyramid (n={n}, odd):\n")
        for row in range(1, n + 1):
            spaces = " " * (n - row)
            stars  = "*" * (2 * row - 1)
            print(spaces + stars)

    else:
        # ---- HOLLOW DIAMOND (even n) ----
        print(f"\nHollow Diamond (n={n}, even):\n")
        half = n // 2

        # Top half — expanding
        for row in range(1, half + 1):
            spaces = " " * (half - row)
            if row == 1:
                print(spaces + "*")
            else:
                inner = " " * (2 * row - 3)
                print(spaces + "*" + inner + "*")

        # Bottom half — contracting (mirror)
        for row in range(half - 1, 0, -1):
            spaces = " " * (half - row)
            if row == 1:
                print(spaces + "*")
            else:
                inner = " " * (2 * row - 3)
                print(spaces + "*" + inner + "*")
