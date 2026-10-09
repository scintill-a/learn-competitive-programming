speed, limit = map(float, input().split())

if speed <= limit:
    print("Status: No Violation | Excess: 0.0 mph | Fine: $0.00")
else:
    excess = speed - limit
    if excess <= 10.0:
        status = "Minor Violation"
        fine = 50.00
    elif excess <= 20.0:
        status = "Moderate Violation"
        fine = 125.00
    else:
        status = "Reckless Speeding"
        fine = 250.00 + (excess - 20.0) * 10.00
    print(f"Status: {status} | Excess: {excess:.1f} mph | Fine: ${fine:.2f}")
