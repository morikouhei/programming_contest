n,x = map(int,input().split())
A = list(map(int,input().split()))

ans = 101

for i in range(0,101):

    sA = A + [i]
    sA.sort()
    if sum(sA[1:n-1]) >= x:
        ans = min(ans,i)

if ans == 101:
    ans = -1
print(ans)