from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    C = Counter(A)
    l = [0]*(n+1)
    for c in C.values():
        l[c] += 1
    ans = n
    cuml = [0]*(n+1)
    for i in range(1,n+1):
        cuml[i] = cuml[i-1]+l[i]*i
    count = 0
    now = 0
    for i in range(n+1)[::-1]:
        if l[i] == 0 and count == 0:
            continue
        calc = cuml[i-1]+now
        ans = min(ans,calc)
        count += l[i]
        now += count
    print(ans)
