from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(l)
    s = len(set(l))
    i = c.most_common()[0][1]
    ans = max(min(i,s-1),min(i-1,s))
    print(ans)
        

