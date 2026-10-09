import math

r, theta = map(float, input().split())
arc = 2.0 * math.pi * r * (theta / 360.0)
area = math.pi * (r ** 2) * (theta / 360.0)
print(f"Arc Length: {arc:.2f} | Sector Area: {area:.2f}")
