n,l,r = map(int,input().split())
A = list(map(int,input().split()))
ans = []
for a in A:
    if l <= a <= r:
        ans.append(a)
    elif abs(l-a) < abs(r-a):
        ans.append(l)
    else:
        ans.append(r)
print(*ans)