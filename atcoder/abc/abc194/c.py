n = int(input())
A = list(map(int,input().split()))
A.sort()
s = sum(A)

ans = 0
for a in A:
    ans += n*a**2
    ans -= a*s
print(ans)