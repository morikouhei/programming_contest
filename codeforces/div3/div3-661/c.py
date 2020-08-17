from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = 0
    c = Counter(l)
    for i in range(2,101):
        count = 0
        for j,k in c.items():
            if i-j in c:
                count += min(k,c[i-j])
        ans = max(ans,count//2)
    print(ans)