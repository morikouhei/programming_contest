t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = [int(i) for i in input().split()]
    am = [0]
    mod = [[] for i in range(x)]
    mod[0].append(0)
    for i in range(n):
        j = (am[-1]+a[i])%x
        am.append(j)
        mod[j].append(i+1)
    
    ans = 0
    for i in range(1,x):
        if len(mod[i]) == 0:
            continue
        if len(mod[i]) == 1:
            ans = max(ans,mod[i][0],n-mod[i][0])
        else:
            a,b = mod[i][0],mod[i][-1]
            ans = max(b-a+1,ans)
            if a != 0:
                ans = max(ans,b)
            if b != n:
                ans = max(ans,n-a)
    if ans == 0:
        print(-1)
    else:
        print(ans)
