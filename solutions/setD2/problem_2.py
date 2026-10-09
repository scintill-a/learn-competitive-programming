dist, mpg, price = map(float, input().split())
gallons = dist / mpg
total_cost = gallons * price
cost_per_mile = total_cost / dist
print(f"Gallons: {gallons:.2f} | Total Cost: ${total_cost:.2f} | Cost Per Mile: ${cost_per_mile:.2f}")
