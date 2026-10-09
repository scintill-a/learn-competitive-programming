da, db = map(float, input().split())
together = (da * db) / (da + db)
share_a = (together / da) * 100.0
print(f"Days Together: {together:.2f} | Worker A Share: {share_a:.1f}%")
