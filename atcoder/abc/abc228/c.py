n,k = map(int,input().split())
P = [list(map(int,input().split())) for i in range(n)]
p = []
for i in range(n):
    p.append([sum(P[i]),i])

p.sort()

ans = [0]*n

now = 0
for i in range(n):
    while now < n and p[i][0]+300 >= p[now][0]:
        now += 1
    if n-1 - (now-1) >= k:
        ans[p[i][1]] = 1

for i in ans:
    if i:
        print("No")
    else:
        print("Yes")
