n = int(input())
P = list(map(int,input().split()))
p0 = P[0]
num = 0
ans = -1
for p in P:
    if p > p0:
        ans = max(ans,p-p0+1)
    elif p == p0:
        num += 1

if ans > 0:
    print(ans)
elif num > 1:
    print(1)
else:
    print(0)
