n = int(input().strip())

count = 0
largest = 0
curr = n
d = 2

while d * d <= curr:
    while curr % d == 0:
        count += 1
        largest = d
        curr //= d
    d += 1

if curr > 1:
    count += 1
    largest = curr

print(f"Factor Count: {count} | Largest Factor: {largest}")
