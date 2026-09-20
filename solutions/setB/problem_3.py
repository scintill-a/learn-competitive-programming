dist, speed = map(float, input().split())


t_mins = round((dist / speed) * 60) 
hours = t_mins // 60
mins = t_mins % 60

print(f"{hours}hour(s) {mins}minute(s)")