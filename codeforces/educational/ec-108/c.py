t = int(input())
for _ in range(t):
    n = int(input())
    u = list(map(int,input().split()))
    s = list(map(int,input().split()))
    L = [[] for i in range(n+1)]
    for i,j in zip(u,s):
        L[i].append(j)
    
    ans = [0]*(n+1)
    for i in range(n+1):
        if L[i] == []:
            continue
        L[i].sort(reverse=True)
        cum = [0]
        le = len(L[i])
        for j in L[i]:
            cum.append(cum[-1]+j)
        for j in range(1,n+1):
            if j > le:
                break
            ans[j] += cum[-1-(le%j)]
 
    print(*ans[1:])