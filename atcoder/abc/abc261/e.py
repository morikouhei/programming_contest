n,c = map(int,input().split())
TA = [list(map(int,input().split())) for i in range(n)]

ans = [0]*n
dp0 = [0]*(n+1)
dp1 = [1]*(n+1)
for i in range(30):

    dp0[0] = 0
    dp1[1] = 1
    num = 1<<i
    for j in range(n):
        t,a = TA[j]

        x = 1 if a & 1<<i else 0

        if t == 1:
            dp0[j+1] = dp0[j]&x
            dp1[j+1] = dp1[j]&x
        elif t == 2:
            dp0[j+1] = dp0[j]|x
            dp1[j+1] = dp1[j]|x
        elif t == 3:
            dp0[j+1] = dp0[j]^x
            dp1[j+1] = dp1[j]^x


    base = 1 if c & 1<<i else 0
    for j in range(n):
        if base:
            base = dp1[j+1]
        else:
            base = dp0[j+1]
        ans[j] += base*num
for i in ans:
    print(i)
    
    