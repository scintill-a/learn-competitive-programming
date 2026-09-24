x1, y1, x2, y2 = map(float, input().split())


euc = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
man = abs(x2 - x1) + abs(y2 - y1)

print(f"Euclidean: {euc:.2f} Manhattan: {man:.2f}")