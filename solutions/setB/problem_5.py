a, b, c = map(int, input().split())


def p5():

    if (a + b < c or a + c < b or a + b < c):
        print("Invalid Triangle")
        return

    if (a == b == c):
        print("Equilateral")
    elif (a == b or a == c or b == c):
        print("Isosceles")
    else:
        print("Scalene")


p5()