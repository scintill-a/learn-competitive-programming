target = int(input())


def fib_seq(t):
    if (t <= 0):
        return []
    if (t == 1):
        return [0]
    
    l = [0, 1]

    for i in range(1, t - 1):
        new = l[i] + l[i-1]
        l.append(new)

    return l

print(fib_seq(target))