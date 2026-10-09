x1, y1, x2, y2, px, py = map(float, input().split())

if x1 < px < x2 and y1 < py < y2:
    print("Position: INSIDE")
elif x1 <= px <= x2 and y1 <= py <= y2:
    print("Position: BORDER")
else:
    print("Position: OUTSIDE")
