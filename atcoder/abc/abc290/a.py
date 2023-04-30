n,m = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for b in map(int,input().split()):
    ans += A[b-1]
print(ans)