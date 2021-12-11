n,k,a = map(int,input().split())
ans = a
for i in range(k-1):
    ans += 1
    if ans == n+1:
        ans = 1
print(ans)