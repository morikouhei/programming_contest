n,d = map(int,input().split())
LR = [list(map(int,input().split())) for i in range(n)]
LR.sort(key=lambda x: x[1])
ans = 0

now = 0
while now < n:

    r = LR[now][1]
    while now < n and LR[now][0]-r < d:
        now += 1
    
    ans += 1

print(ans)