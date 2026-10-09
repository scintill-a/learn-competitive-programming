from collections import deque

nums = list(map(int, input().split()))
k = int(input().strip())

dq = deque()
res = []
for i, x in enumerate(nums):
    while dq and dq[0] < i - k + 1:
        dq.popleft()
    while dq and nums[dq[-1]] <= x:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        res.append(nums[dq[0]])
print(f"Window Maxima: {' '.join(map(str, res))}")
