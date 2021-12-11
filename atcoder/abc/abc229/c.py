n,w = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(n)]
AB.sort(reverse=True)
ans = 0
for a,b in AB:
    cost = min(b,w)
    ans += a*cost
    w -= cost
print(ans)