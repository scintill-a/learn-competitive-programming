n = int(input().strip())
intervals = []
for _ in range(n):
    intervals.append(list(map(int, input().split())))

starts = sorted([iv[0] for iv in intervals])
ends = sorted([iv[1] for iv in intervals])
max_c = cur_c = 0
i = j = 0
while i < n and j < n:
    if starts[i] < ends[j]:
        cur_c += 1
        if cur_c > max_c:
            max_c = cur_c
        i += 1
    else:
        cur_c -= 1
        j += 1
print(f"Peak Concurrent: {max_c}")
