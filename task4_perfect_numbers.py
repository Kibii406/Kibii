try:
    N = int(input("Enter limit N: "))
except ValueError:
    print("Please enter a positive integer.")
    exit()

if N <= 0:
    print("Please enter a positive integer.")
else:
    print(f"\nSearching for perfect numbers from 1 to {N}...\n")
    found_any = False

    for num in range(2, N + 1):          # outer loop: every candidate number
        divisor_sum = 0
        for d in range(1, num):          # inner loop: every possible divisor
            if num % d == 0:
                divisor_sum += d         # accumulate on the fly — no array needed
        if divisor_sum == num:
            print(f"  {num} is PERFECT  (proper divisors sum = {divisor_sum})")
            found_any = True

    if not found_any:
        print("  No perfect numbers found in that range.")

