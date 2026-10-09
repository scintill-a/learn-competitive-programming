x1, y1, x2, y2, x3, y3 = map(float, input().split())

cross = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
area = 0.5 * abs(cross)

if area < 1e-3:
    print("Points are Collinear")
else:
    print(f"Valid Triangle | Area: {area:.2f}")
