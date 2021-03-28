import math
n = int(input())
x0,y0 = map(int,input().split())
xn,yn = map(int,input().split())

rot = math.pi*2/n
cx = (x0+xn)/2
cy = (y0+yn)/2

x = cx+(x0-cx)*math.cos(rot)-(y0-cy)*math.sin(rot)
y = cy+(x0-cx)*math.sin(rot)+(y0-cy)*math.cos(rot)
print(x,y)