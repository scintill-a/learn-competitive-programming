prices = list(map(int, input().split()))
budget = int(input())


count = 0

for price in prices:
    if budget == 0:
        break

    if (budget >= price and price > 0):
        count += 1
        budget -= price
    if (price > 0 and budget <= price):
        continue
    if (price == 0):
        count += 1

    if budget == 0:
        break


print((budget, count))