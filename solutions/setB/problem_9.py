nums = [*map(int, input().split())]


seen = {}


def p9():
    for i in nums:
        seen[i] = seen.get(i, 0) + 1

    for x, y in seen.items():
        if y == 1:
            return x
            break

    return None


print(p9())