from collections import Counter

s = input().strip()
p = input().strip()

if len(s) < len(p):
    print("Anagram Indices: None")
else:
    p_cnt = Counter(p)
    w_cnt = Counter(s[:len(p)])
    res = []
    if w_cnt == p_cnt:
        res.append(0)
    k = len(p)
    for i in range(k, len(s)):
        w_cnt[s[i]] += 1
        w_cnt[s[i - k]] -= 1
        if w_cnt[s[i - k]] == 0:
            del w_cnt[s[i - k]]
        if w_cnt == p_cnt:
            res.append(i - k + 1)
    if not res:
        print("Anagram Indices: None")
    else:
        print(f"Anagram Indices: {', '.join(map(str, res))}")
