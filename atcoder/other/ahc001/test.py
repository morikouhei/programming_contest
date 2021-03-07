n = int(input())
l = [tuple(map(int,input().split())) for i in range(n)]

ans = [[0]*4 for i in range(n)]
M = 10000
for x,y,r in l:
   ans.append([x,y,x+1,y+1])
for i in ans:
    print(*i)