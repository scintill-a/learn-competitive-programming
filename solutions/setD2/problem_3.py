dist_str, shift = input().split()
dist = float(dist_str)
shift = shift.upper()

if dist <= 1.0:
    fare = 4.00
else:
    excess = dist - 1.0
    rate = 1.50 if shift == "DAY" else 2.25
    fare = 4.00 + excess * rate

print(f"Shift: {shift} | Distance: {dist:.2f} km | Total Fare: ${fare:.2f}")
