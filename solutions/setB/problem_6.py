word = list(input())
target = input()


def p6(word, target, idx=0):

    if (idx >= len(word)):
        return -1

    if (word[idx] == target):
        return idx

    idx += 1


    return p6(word, target, idx)


print(p6(word, target))