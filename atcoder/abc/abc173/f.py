N = int(input())
ans = 0
for n in range(1,N+1):
    ans += n*(N+1-n)

for _ in range(N-1):
    a,b = map(int,input().split())
    if a > b:
        a,b = b,a
    ans -= a*(N+1-b)

print(ans)