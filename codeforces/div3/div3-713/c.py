t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    S = list(input())
    ans = []
    for s in S:
        if s == "?":
            ans.append(-1)
        else:
            ans.append(int(s))

    n = len(S)
    left = 0
    if n%2:
        if ans[n//2] != -1:
            l[ans[n//2]] -= 1
        else:
            left = 1
    cand = []
    ok = 1

    for i in range(n//2):
        a,b = ans[i],ans[-1-i]
        if a == -1:
            if b == -1:
                cand.append(i)
            elif b == 0:
                l[0] -= 2
                ans[i] = 0
            else:
                l[1] -= 2
                ans[i] = 1
        elif a == 0:
            if b == 1:
                ok = 0
            else:
                l[0] -= 2
                ans[-1-i] = 0
        else:
            if b == 0:
                ok = 0
            else:
                l[1] -= 2
                ans[-1-i] = 1
    if ok == 0:
        print(-1)
        continue
    for i in cand:
        if l[0] >= 2:
            l[0] -= 2
            ans[i] = ans[-1-i] = 0
            continue
        if l[1] >= 2:
            l[1] -= 2
            ans[i] = ans[-1-i] = 1
    
    if left:
        if l[0] != 0:
            ans[n//2] = 0
            l[0] -= 1
        elif l[1] != 0:
            l[1] -= 1
            ans[n//2] = 1
    if l[0] == l[1] == 0:
        print(*ans,sep="")
    else:
        print(-1)