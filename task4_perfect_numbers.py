# TASK 4: Perfect Numbers
# A number is 'perfect' if it equals the sum of its proper divisors.
# Example: 6 = 1 + 2 + 3  ✓
#
# Rules:
#   - Read limit N from user
#   - Use nested loops (no arrays)
#   - Accumulate divisor sum on the fly inside the inner loop
#   - Discuss how performance changes as N grows

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

# -------------------------------------------------------------------
# PERFORMANCE DISCUSSION
# -------------------------------------------------------------------
#
# For each number `num` up to N, the inner loop runs (num - 1) times.
# Total work = 1 + 2 + 3 + ... + (N-1)  =  N*(N-1)/2  →  O(N²)
#
# What this means as N grows:
#   N =     100  →         ~5,000 iterations  (fast)
#   N =   1,000  →       ~500,000 iterations  (still quick)
#   N =  10,000  →    ~50,000,000 iterations  (noticeable delay)
#   N = 100,000  → ~5,000,000,000 iterations  (very slow — minutes)
#
# Doubling N roughly QUADRUPLES the work. This is why the nested-loop
# approach becomes impractical for large N.
#
# A smarter approach: only check divisors up to √num.
#   If d divides num, then (num/d) also divides it — count both at once.
#   This cuts the inner loop to O(√num) per number → total O(N√N).
#   Much faster, but requires more careful logic.
