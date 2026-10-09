import math

r = float(input().strip())
area = 3.0 * math.pi * (r ** 2)
vol = (2.0 / 3.0) * math.pi * (r ** 3)
print(f"Total Surface Area: {area:.2f} | Volume: {vol:.2f}")
