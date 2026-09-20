val = [*map(int, input().split())]


for i in range(len(val)):
    if i % 2 == 0:
        val[i] = val[i] * 2
    else:
        val[i] = -val[i]


print(val)