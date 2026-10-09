n = int(input().strip())

rounds = 0
curr = n

while curr >= 10:
    curr = sum(int(d) for d in str(curr))
    rounds += 1

print(f"Rounds: {rounds} | Digital Root: {curr}")
