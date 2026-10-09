n = int(input())
steps = 0
peak = n
curr = n

while curr > 1:
    if curr % 2 == 0:
        curr = curr // 2
    else:
        curr = 3 * curr + 1
    steps += 1
    if curr > peak:
        peak = curr

print(f"Steps: {steps} | Peak: {peak}")
