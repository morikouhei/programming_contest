n,p = map(int,input().split())
ans = 0
A = list(map(int,input().split()))
for a in A:
    if a < p:
        ans += 1
print(ans)