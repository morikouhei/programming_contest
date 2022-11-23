import math
n = int(input())
A = list(map(int,input().split()))
ans = min(2,len(set(A)))

g = 0
for a,na in zip(A,A[1:]):
    g = math.gcd(g,abs(a-na))

if g != 1:
    ans = 1
print(ans)