balance, count, unit_price, d_price, tax = map(float, input().split())

count = int(count)
d_price = int(d_price)
tax = int(tax)

unit_discounted_price = (unit_price * count) - ((unit_price * count) * (d_price/100))
tax_price_total = unit_discounted_price + (unit_discounted_price * (tax/100))

print(f"${tax_price_total:.2f}  |  ${balance - tax_price_total:.2f}  |  ${tax_price_total / count:.2f}")

