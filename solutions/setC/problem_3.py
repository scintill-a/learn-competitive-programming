hex = input()

# #RRGGBB
r = hex[1:3]
g = hex[3:5]
b = hex[5:]

r = int(r, 16)
g = int(g, 16)
b = int(b, 16)


L = 0.2126 * r + 0.7152 * g + 0.0722 * b

print(f"RGB: ({r}, {g}, {b}) L: {L:.1f}")