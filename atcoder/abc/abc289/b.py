n,m = map(int,input().split())
A = list(map(int,input().split()))
re = [0]*n
for a in A:
    re[a-1] = 1

ans = []
now = 0
for i,a in enumerate(re,1):
    if a:
        continue
    for j in range(now+1,i+1)[::-1]:
        ans.append(j)
    now = i
print(*ans)