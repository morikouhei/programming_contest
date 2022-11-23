n = int(input())
A = list(map(int,input().split()))
l = [[] for i in range(2)]
for a in A:
    l[a%2].append(a)

ans = -1
for s in l:
    s.sort(reverse=True)
    if len(s) >= 2:
        ans = max(ans,s[0]+s[1])
print(ans)