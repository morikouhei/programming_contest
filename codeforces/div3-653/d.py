from collections import Counter

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    l = [int(i)%k for i in input().split()]
    c = Counter(l)
    now = 0
    ma = float("INF")
    
    for i,j in c.items():
    
        if i == 0:
            continue
        if now < j:
            now = j
            ma = i
        elif now == j:
            if ma > i:
                now = j
                ma = i
    if ma == float("INF"):
        print(0)
    else:
        
        print(k*(now-1)+(k-ma)+1)
