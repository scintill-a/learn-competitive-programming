import math

a, b, c = map(float, input().split())
disc = b**2 - 4.0 * a * c

if disc > 1e-9:
    r1 = (-b + math.sqrt(disc)) / (2.0 * a)
    r2 = (-b - math.sqrt(disc)) / (2.0 * a)
    larger = max(r1, r2)
    smaller = min(r1, r2)
    print(f"Type: Two Real Roots | Roots: {larger:.2f}, {smaller:.2f}")
elif abs(disc) <= 1e-9:
    root = -b / (2.0 * a)
    print(f"Type: One Real Root | Root: {root:.2f}")
else:
    print("Type: No Real Roots")
