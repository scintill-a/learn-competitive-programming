nums = list(map(int, input().split()))
target = int(input().strip())
l, r = 0, len(nums) - 1
found = False
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        print(f"Indices: {l}, {r} | Values: {nums[l]}, {nums[r]}")
        found = True
        break
    elif s < target:
        l += 1
    else:
        r -= 1
if not found:
    print("No Pair")
