n,m = map(int,input().split())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
Sl = [0]*2
Tl = [0]*2
for s in S:
    Sl[s] = 1
for t in T:
    Tl[t] = 1
if (Sl[0] == 0 and Tl[0]) or (Sl[1] == 0 and Tl[1]):
    print(-1)
    exit()

ans = m
now = S[0]
dif = n+1
for i in range(1,n):
    if S[i] != now:
        dif = min(dif,i,n-i)


first = 0
now = S[0]
for t in T:
    if t != now:
        now = t
        if first:
            ans += 1
        else:
            first = 1
            ans += dif
print(ans)


