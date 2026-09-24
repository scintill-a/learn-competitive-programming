server = input().split()

token = server[0][1:-1]
latency = float(server[-1][8:-2]) / 1000


print(f"Timestamp:{token} Latency:{latency}")