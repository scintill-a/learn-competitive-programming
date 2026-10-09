s = input().strip()

def is_pal(sub):
    return sub == sub[::-1]

l, r = 0, len(s) - 1
ans = "Valid: True | Deleted: None"
while l < r:
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        if is_pal(s[l + 1:r + 1]):
            ans = f"Valid: True | Deleted: {s[l]}"
        elif is_pal(s[l:r]):
            ans = f"Valid: True | Deleted: {s[r]}"
        else:
            ans = "Valid: False"
        break
print(ans)
