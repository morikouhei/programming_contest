n = int(input())
ans = [float("INF")]*(n+1)

l = [list(map(int,input().split())) for i in range(n)]

for i in range(3**n):
    now = i
    X = [0]
    Y = [0]
    count = 0
    for j in range(n):
        m = now%3
        if m == 1:
            X.append(l[j][1])
            count += 1
        elif m == 2:
            Y.append(l[j][0])
            count += 1
        now //= 3
    cal = 0
    for x,y,p in l:
        c = float("INF")
        for nx in X:
            c = min(c,abs(y-nx))
        for ny in Y:
            c = min(c,abs(x-ny))
        cal += c*p
    ans[count] = min(ans[count],cal)
for i in ans:
    print(i)