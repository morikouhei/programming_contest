n,x = map(int,input().split())
S = list(map(int,input().split()))
ans = 0
for s in S:
    if s <= x:
        ans += s
print(ans)