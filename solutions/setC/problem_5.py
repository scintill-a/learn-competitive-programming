s1, e1, s2, e2 = map(int, input().split())

# 1 5 3 8

start = max(s1, s2)
end = min(e1, e2)

range = 0

def main():
    global range

    if start > end:
        range = 0
        return "DISJOINT"
    elif start == end:
        range = 1
        return "TOUCHING"
    elif (s1 >= s2 and e1 <= e2) or (s2 >= s1 and e2 <= e1):
        range = end - start + 1
        return "SUBSET"
    else:
        range = end - start + 1
        return "OVERALLPING"

    
print(f"{main()} {range}")