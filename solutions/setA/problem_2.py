seconds = int(input(""))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
second = seconds % 60


print(f"{hours:02d}:{minutes:02d}:{second:02d}")
