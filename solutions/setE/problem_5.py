height = list(map(int, input().split()))
l, r = 0, len(height) - 1
max_area = 0
best_pair = (0, 0)
while l < r:
    area = (r - l) * min(height[l], height[r])
    if area > max_area:
        max_area = area
        best_pair = (l, r)
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
print(f"Max Water: {max_area} | Lines: {best_pair[0]}, {best_pair[1]}")
