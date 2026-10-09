principal, rate_pct, years = map(float, input().split())
interest = principal * (rate_pct / 100.0) * years
maturity = principal + interest
print(f"Interest: ${interest:.2f} | Maturity: ${maturity:.2f}")
