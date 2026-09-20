import math

r, h = input().split()

r = float(r)
h = float(h)

vol = math.pi * (r**2) * h
area = (2*math.pi) * r *h + (2*math.pi) * (r**2)


print(f"$Volume: {vol:.2f} Area: {area:.2f}")