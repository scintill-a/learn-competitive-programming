# idea of the palindrome is just given a string s, s = s[::-1]
# no conditionals

s = input()

def is_palindrome(s):
    check = (s == s[::-1])
    val = ["Not Palindrome", "Palindrome"]

    return val[check]

print(is_palindrome(s))


