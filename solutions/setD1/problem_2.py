dist, s_time = input().split()

dist = float(dist)
hour = float(s_time[:2])
minute = float(s_time[3:5])
seconds = float(s_time[6:])

min_t_hour = hour * 60
total_min  = min_t_hour + minute
t_seconds = total_min * 60 + seconds


# speed = d / t
speed = dist / (t_seconds/3600)
phase_km = t_seconds / dist
# min_phase, sec_phase = divmod(phase_km, 60)
min_phase = phase_km // 60
sec_phase = phase_km % 60


print(f"Total(s): {int(t_seconds)}  |  {speed:.2f}km/h  |  {int(min_phase):02d}:{int(sec_phase):02d}km")
