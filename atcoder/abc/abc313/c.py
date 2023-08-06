n = int(input())
A = list(map(int,input().split()))

s = sum(A)
A.sort()

m = s%n
t = s//n
ans = 0
print(t,m)
for i,a in enumerate(A):
    if i < n-m:
        ans += abs(a-t)
    else:
        ans += abs(a-t-1)
print(ans//2)