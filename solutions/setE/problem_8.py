nums = list(map(int, input().split()))
res = [-1] * len(nums)
stack = []
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        idx = stack.pop()
        res[idx] = x
    stack.append(i)
print(" ".join(map(str, res)))
