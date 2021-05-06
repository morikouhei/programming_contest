n,k = map(int,input().split())
count = [0]*(n+1)
for i in range(2,n+1):
    if count[i]:
        continue
    for j in range(i,n+1,i):
        count[j] += 1

ans = 0
for i in range(n+1):
    if count[i] >= k:
        ans += 1
print(ans)