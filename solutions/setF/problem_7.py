from collections import Counter

s = input().strip()
k = int(input().strip())

if k == 0 or not s:
    print("Max Length: 0 | Substring: ")
else:
    counts = Counter()
    l = 0
    max_len = 0
    best_sub = ""
    for r, ch in enumerate(s):
        counts[ch] += 1
        while len(counts) > k:
            left_ch = s[l]
            counts[left_ch] -= 1
            if counts[left_ch] == 0:
                del counts[left_ch]
            l += 1
        if (r - l + 1) > max_len:
            max_len = r - l + 1
            best_sub = s[l:r + 1]
    print(f"Max Length: {max_len} | Substring: {best_sub}")
