num = [*map(int, input().split())]
limit = int(input())

tick = 0
running_sum = 0

for i in range(len(num)):

    if num[i] > 0:
        running_sum += 3 * num[i]
        tick += 1 
    elif num[i] < 0:
        running_sum += num[i]**2
        tick += 1
    elif num[i] == 0:
        tick += 1
        running_sum += 0

    if running_sum >= limit:
        break

print((running_sum, tick))