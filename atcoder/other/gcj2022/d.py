def solve():
    n = int(input())
    F = list(map(int,input().split()))
    e = [[] for i in range(n)]
    P = [int(x)-1 for x in input().split()]
    top = [0]*n
    for i,p in enumerate(P):
        if p == -1:
            top[i] = 1
        else:
            e[p].append(i)

    ans = 0    
    calc = [0]*n
    for i in range(n)[::-1]:
        ind = -1
        num = F[i]
        if len(e[i]) > 1:
            mi = 10**10
            for child in e[i]:
                if mi > calc[child]:
                    mi = calc[child]
                    ind = child
            for child in e[i]:
                if ind == child:
                    continue
                ans += calc[child]
            calc[i] = max(num,mi)

        else:
            for child in e[i]:
                num = max(num,calc[child])
            calc[i] = num

        if top[i]:
            ans += calc[i]
    return ans


t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    print(ans)