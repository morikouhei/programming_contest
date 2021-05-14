n,a,b = map(int,input().split())
ans = [1]
for i in range(n-1):
    ans.append(ans[-1]*b%n)
print(*ans)