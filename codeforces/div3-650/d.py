from collections import Counter
t = int(input())
for _ in range(t):
    s = list(input())
    s.sort(reverse=True)
    now = 0
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(s)
    count = 0
    ans = [""]*n
    while count < n:
        ind = []
        for i in range(n):
            if l[i] == 0:
                ind.append(i)
        while c[s[now]] < len(ind):
            now += 1
        for i in ind:
            ans[i] = s[now]
        x = s[now]
        while now < len(s) and s[now] == x: 
            now += 1
        for i in range(n):
            if l[i] <= 0:
                l[i] += 10**10
            else:
                for j in ind:
                    l[i] -= abs(i-j)
        count += len(ind)
    print(*ans,sep="")
            



