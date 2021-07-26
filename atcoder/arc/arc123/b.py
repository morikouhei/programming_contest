n = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
C = sorted(list(map(int,input().split())))
ans = 0
a = n-1
c = n-1
ans = 0
for i in range(n)[::-1]:
    b = B[i]
    while a >= 0 and A[a] >= b:
        a -= 1
    if a < 0:
        break
    if C[c] <= b:
        continue
    ans += 1
    c -= 1
    a += 1
print(ans)