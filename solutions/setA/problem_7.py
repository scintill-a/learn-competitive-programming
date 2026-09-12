num = [*map(int, input().split())]

new_list = []

for i in num:
    if (i & 1) == 0:
        new_list.append(i * 8)
    else:
        new_list.append(i + 2)

print(new_list)