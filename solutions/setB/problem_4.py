x, y = map(float, input().split())


def plane():

    if (x == 0 and y == 0):
        print("Origin")
    elif (x == 0 and y != 0):
        print("Y axis")
    elif (x != 0 and y == 0):
        print("X axis")
    elif (x > 0 and y > 0):
        print("Quadrant 1")
    elif (x < 0 and y > 0):
        print("Quadrant 2")
    elif (x < 0 and y < 0):
        print("Quadrant 3")
    else:
        print("Quadrant 4")


plane()