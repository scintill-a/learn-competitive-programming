m, v = map(float, input().split())
momentum = m * v
ke = 0.5 * m * (v ** 2)
print(f"Momentum: {momentum:.2f} kg*m/s | Kinetic Energy: {ke:.2f} J")
