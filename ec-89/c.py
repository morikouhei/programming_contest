from collections import deque
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    l = [list(map(int,input().split())) for i in range(n)]
    count = [[0]*2 for i in range(n+m-1)]
    q = deque([])
    count[0][l[0][0]] += 1
    q.append((0,0,0))
    while q:
        bx,by,dis = q.popleft()
        if bx+1 < n and l[bx+1][by] >= 0:
            count[dis+1][l[bx+1][by]] += 1
            l[bx+1][by] = -1
            q.append((bx+1,by,dis+1))

        if by+1 < m and l[bx][by+1] >= 0:
            count[dis+1][l[bx][by+1]] += 1
            l[bx][by+1] = -1
            q.append((bx,by+1,dis+1))
    ans = 0
    for i in range(len(count)//2):
        ans += min(count[i][0]+count[-1-i][0],count[i][1]+count[-1-i][1])
    print(ans)