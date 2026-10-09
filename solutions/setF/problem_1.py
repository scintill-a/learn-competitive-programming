nums = list(map(int, input().split()))
total = sum(nums)
left = 0
found = False
for i, x in enumerate(nums):
    if left == total - left - x:
        print(f"Pivot Index: {i} | Value: {x}")
        found = True
        break
    left += x
if not found:
    print("Pivot Index: -1")
