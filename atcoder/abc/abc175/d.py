n,k = map(int,input().split())
p = list(map(int,input().split()))
used = [0]*n
c = list(map(int,input().split()))
ans = -float("INF")
def calc(x):
    l = []
    now = x
    score = 0
    while used[now] == 0:
        used[now] = 1
        l.append(c[now])
        now = p[now]-1
    S = sum(l)
    le = len(l)
    if S > 0 and k > le:
        score += (k//le-1)*S
        mod = k%le
        now = 0
        for i in range(le):
            cal = 0
            for j in range(le):
                if j <= mod:
                    now = max(now,cal+S)
                cal += l[(i+j)%le]
                now = max(now,cal)
        return score+now
    else:
        mod = min(le,k)
        now = -float("INF")
        for i in range(le):
            cal = 0
            for j in range(mod):
                cal += l[(i+j)%le]
                now = max(now,cal)
        return score+now
    
for i in range(n):
    if used[i] == 0:
        ans = max(ans,calc(i))
print(ans)