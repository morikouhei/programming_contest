t = int(input())

def calc(x):
    now = 0
    for i in range(x,n):
        now += sA[i][0]
    for i in range(x-1,-1,-1):
        if now >= sA[i][0]:
            now += sA[i][0]
        else:
            return 0

    return 1
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    sA = [[A[i],i] for i in range(n)]
    sA.sort(reverse=True)
    ans = []
    
    l = 0
    r = n
    while r > l + 1:
        m = (r+l)//2
        if calc(m):
            l = m
        else:
            r = m
    
    for i in range(l+1):
        ans.append(sA[i][1]+1)
    ans.sort()
    print(len(ans))
    print(*ans)