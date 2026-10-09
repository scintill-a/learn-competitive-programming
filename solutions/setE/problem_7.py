s = input().strip()
seen = {}
l = 0
max_len = 0
best_sub = ""
for r, ch in enumerate(s):
    if ch in seen and seen[ch] >= l:
        l = seen[ch] + 1
    seen[ch] = r
    if (r - l + 1) > max_len:
        max_len = r - l + 1
        best_sub = s[l:r + 1]
print(f"Max Length: {max_len} | Substring: {best_sub}")
