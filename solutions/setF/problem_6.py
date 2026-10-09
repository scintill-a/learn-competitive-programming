nums = list(map(int, input().split()))
low, high = 0, len(nums) - 1
while low < high:
    mid = (low + high) // 2
    if nums[mid] < nums[mid + 1]:
        low = mid + 1
    else:
        high = mid
print(f"Peak Index: {low} | Value: {nums[low]}")
