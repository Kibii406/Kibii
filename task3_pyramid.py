# TASK 3: Numeric Pyramid
# Reads integer n. Shape depends on odd/even:
#   ODD  n → Solid filled pyramid (triangle)
#   EVEN n → Hollow diamond
#
# PAPER DESIGN:
#
# Solid Pyramid (n=5):        Hollow Diamond (n=4):
#     *                              *
#    ***                            * *
#   *****                          * *
#  *******                          *
# *********
#
# LOOP STRUCTURE (Solid Pyramid):
#   Outer loop: row goes from 1 to n
#     - leading spaces = (n - row)
#     - stars          = (2*row - 1)
#   No inner loop needed; string multiplication handles it.
#
# LOOP STRUCTURE (Hollow Diamond):
#   half = n // 2
#   Top half:    outer loop row from 1 to half
#     - if row==1: single star (tip)
#     - else:      star + inner spaces + star
#   Bottom half: outer loop row from (half-1) down to 1
#     - mirror image of top half

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
