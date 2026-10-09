nums = list(map(int, input().split()))
k = int(input().strip())
w_sum = sum(nums[:k])
max_sum = w_sum
best_idx = 0
for i in range(k, len(nums)):
    w_sum += nums[i] - nums[i - k]
    if w_sum > max_sum:
        max_sum = w_sum
        best_idx = i - k + 1
print(f"Max Sum: {max_sum} | Start Index: {best_idx}")
