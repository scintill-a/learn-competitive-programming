import math

a, b = map(float, input().split())
c = math.sqrt(a**2 + b**2)
p = a + b + c
area = 0.5 * a * b
print(f"Hypotenuse: {c:.2f} | Perimeter: {p:.2f} | Area: {area:.2f}")
