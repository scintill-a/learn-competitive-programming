a, b, c = map(float, input().split())

if a <= 0 or b <= 0 or c <= 0 or abs((a + b + c) - 180.0) > 1e-3:
    print("Invalid Triangle")
else:
    max_ang = max(a, b, c)
    if abs(max_ang - 90.0) < 1e-3:
        kind = "Right"
    elif max_ang > 90.0:
        kind = "Obtuse"
    else:
        kind = "Acute"
    print(f"Type: {kind} | Max Angle: {max_ang:.1f}°")
