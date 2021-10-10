n = int(input())
A = list(map(int,input().split()))
X = int(input())
s = sum(A)
ans = (X//s)*n
X -= (X//s)*s
for a in A:
    X -= a
    ans += 1
    if X < 0:
        print(ans)
        exit()