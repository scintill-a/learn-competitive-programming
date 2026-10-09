nums = list(map(int, input().split()))
xor_acc = 0
for x in nums:
    xor_acc ^= x
print(f"Unique Element: {xor_acc}")
