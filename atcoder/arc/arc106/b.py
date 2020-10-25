from collections import deque
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

e = [[] for i in range(n)]
for i in range(m):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    e[c].append(d)
    e[d].append(c)


used = [0]*n

for i in range(n):
    if used[i]:
        continue
    used[i] = 1
    count = a[i]-b[i]
    q = deque([i])
    while q:
        now = q.popleft()
        for nex in e[now]:
            if used[nex]:
                continue
            count += a[nex] - b[nex]
            used[nex] = 1
            q.append(nex)
    if count != 0:
        print("No")
        exit()
print("Yes")