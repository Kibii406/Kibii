try:
    start = int(input("Enter a positive starting number: "))
except ValueError:
    print("Please enter a positive integer.")
    exit()

if start <= 0:
    print("Please enter a positive integer.")
    exit()

print(f"\nPART A — Collatz sequence from {start}:")
n = start
steps = 0
print(n, end="")

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
    print(f" → {n}", end="")

print(f"\n\nSteps to reach 1: {steps}")

# ---- PART B: Scan 1 to 99 ----

print("\nPART B — Scanning all starting values from 1 to 99...\n")

longest_start = 1
longest_steps = 0          # tracks the 'longest so far'

for start in range(1, 100):
    n = start
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1

    if count > longest_steps:       # new champion found?
        longest_steps = count       # update longest so far
        longest_start = start       # remember which number caused it

print(f"Longest sequence starts at : {longest_start}")
print(f"Number of steps            : {longest_steps}")
