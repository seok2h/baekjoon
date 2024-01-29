time = input().split(" ")
need_time = int(input())

h = int(time[0])
m = int(time[1])

M = m + need_time

while(M - 60 >= 0):
    M -= 60
    h += 1

if h >= 24:
    h -= 24

print(h, M)

