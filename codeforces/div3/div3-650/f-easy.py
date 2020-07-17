t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l1 = sorted(list(set(l)))
    d = defaultdict(int)
    for i in range(len(l1)):
        d[l1[i]] = i
    l2 = []
    for i in l:
        l2.append(d[i])
    dp = [0]*n
    d = defaultdict(list)
    print(l2)
    for i in range(n):
        x = d[l2[i]]
        y = d[l2[i]-1]
        now = 0
        if x:
            now = (max(now,max(x)))
        if y:
            now = (max(now,max(y)))
        dp[i] = now+1
        d[l2[i]].append(now+1)
    print(n-max(dp))
    print(d)
    