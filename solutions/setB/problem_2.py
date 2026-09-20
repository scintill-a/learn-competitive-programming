val = int(input())


hun = val // 100
rem = val %  100

fift = rem //  50
rem = rem % 50

twnt = rem // 20
rem = rem % 20

tent = rem // 10
rem = rem % 10

fiv = rem // 5
rem = rem % 5

ons = rem

print(f"{hun}s {fift}s {twnt}s {tent}s {fiv}s {ons}s")
