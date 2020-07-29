import sys
input = sys.stdin.readline
from collections import defaultdict
n = int(input())
UR = defaultdict(list)
UD = defaultdict(list)
UL = defaultdict(list)
DR = defaultdict(list)
DL = defaultdict(list)
RL = defaultdict(list)

for i in range(n):
    x,y,u = input().split()
    x,y = int(x), int(y)
    if u == "U":    
        UD[x].append((y,1))
        UR[x+y].append((x-y,0))
        UL[y-x].append((x+y,1))
    elif u == "D":    
        UD[x].append((y,0))
        DR[y-x].append((x+y,0))
        DL[x+y].append((x-y,1))
    elif u == "R":   
        RL[y].append((x,1))
        DR[y-x].append((x+y,1))
        UR[x+y].append((x-y,1))
        
    else:
        RL[y].append((x,0))
        UL[y-x].append((x+y,0))
        DL[x+y].append((x-y,0))

ans = float("INF")

for x in [UD, UL, UR, DR, DL, RL]:
    for v in x.values():
        V = sorted(v)

        for i in range(len(V)-1):
            if V[i][1] and not V[i+1][1]:
                ans = min(ans,V[i+1][0]-V[i][0])


if ans == float("INF"):
    print("SAFE")
else:
    print(ans*5)
