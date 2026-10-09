arr = list(map(int, input().split()))
l, r = map(int, input().split())
pref = [0] * (len(arr) + 1)
for i, x in enumerate(arr):
    pref[i + 1] = pref[i] + x
ans = pref[r + 1] - pref[l]
print(f"Prefix Sum: {ans}")
