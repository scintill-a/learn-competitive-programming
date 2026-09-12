nums = [*map(int, input().split())]

seen = {}
dups = []

for i in range(len(nums)):
    seen[nums[i]] = seen.get(nums[i],0) + 1


for x,y in seen.items():
    if y > 1:
        dups.append(x)

# dups = [i for i, x in seen.items() if x > 1]

print(dups)


