n,d = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(n)]

e = [[] for i in range(n)]

for i in range(n):
  x,y = XY[i]
  for j in range(i):
    nx,ny = XY[j]
    if (x-nx)**2+(y-ny)**2 <= d**2:
      e[i].append(j)
      e[j].append(i)
      
vis = [0]*n
vis[0] = 1
q = [0]
while q:
  now = q.pop()
  for nex in e[now]:
    if vis[nex]:
      continue
    vis[nex] = 1
    q.append(nex)
for i in vis:
  print("Yes" if i else "No")