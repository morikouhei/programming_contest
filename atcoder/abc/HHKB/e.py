h,w = map(int,input().split())
S = [list(input()) for i in range(h)]

mod = 10**9+7

two = [1]
for i in range(h*w+5):
    two.append(two[-1]*2%mod)

X = [[0]*w for i in range(h)]
Y = [[0]*w for i in range(h)]
count = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            count += 1
for i in range(h):
    s = 0
    while s < w:
        sta = s
        now = 0
        while now+sta < w and S[i][now+sta] == ".":
            now += 1
        for j in range(now):
            X[i][sta+j] = now
        s += now+1
for i in range(w):
    s = 0
    while s < h:
        sta = s
        now = 0
        while now+sta < h and S[now+sta][i] == ".":
            now += 1
        for j in range(now):
            Y[sta+j][i] = now
        s += now+1
ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            ans += (two[count]-two[count-X[i][j]-Y[i][j]+1])
            ans %= mod
print(ans)
