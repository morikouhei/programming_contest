import math
T = int(input())
l,X,Y = map(int,input().split())
q = int(input())

def calc(t):
    x = 0
    y = -l/2*math.sin(t/T*math.pi*2)
    z = l/2 - l/2*math.cos(t/T*math.pi*2)
    return math.degrees(math.atan2(z, ((x-X)**2+(y-Y)**2)**0.5))



for i in range(q):
    e = int(input())
    print(calc(e))
