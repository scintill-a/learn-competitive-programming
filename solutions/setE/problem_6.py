weights = list(map(int, input().split()))
days = int(input().strip())
low, high = max(weights), sum(weights)
ans = high
while low <= high:
    mid = (low + high) // 2
    d = 1
    curr = 0
    for w in weights:
        if curr + w > mid:
            d += 1
            curr = w
        else:
            curr += w
    if d <= days:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(f"Minimum Capacity: {ans}")
