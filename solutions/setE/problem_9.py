nums = list(map(int, input().split()))
total = sum(nums)
cur_max = cur_min = nums[0]
max_sum = min_sum = nums[0]
for x in nums[1:]:
    cur_max = max(x, cur_max + x)
    max_sum = max(max_sum, cur_max)
    cur_min = min(x, cur_min + x)
    min_sum = min(min_sum, cur_min)
if max_sum < 0:
    ans = max_sum
else:
    ans = max(max_sum, total - min_sum)
print(f"Max Circular Sum: {ans}")
