# Bitwise Operators: Operate on individual bits of numbers
a = 5 & 3   # AND: 1 if both bits are 1 → 1
b = 5 | 3   # OR: 1 if at least one bit is 1 → 7
c = 5 ^ 3   # XOR: 1 if bits are different → 6
d = ~5      # NOT: Flips bits → -6
e = 5 << 1  # Left Shift: Shifts bits left → 10
f = 5 >> 1  # Right Shift: Shifts bits right → 2

print(a, b, c, d, e, f)
