n = int(input())
A = list(map(int,input().split()))

A.sort()

ans = 10**20

q = [[0,n,0,29]]

while q:
    l,r,cost,b = q.pop()
    if b == -1:
        ans = min(ans,cost)
        continue

    sb = A[l]>>b&1
    dif = 0
    for i in range(l,r):
        if A[i]>>b&1 != sb:
            dif = 1
            q.append([l,i,cost+(1<<b),b-1])
            q.append([i,r,cost+(1<<b),b-1])
            break
    if dif == 0:
        q.append([l,r,cost,b-1])

print(ans)