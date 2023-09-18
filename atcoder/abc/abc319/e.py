import sys
sys.stdin.readline

n,x,y = map(int,input().split())
PT = [list(map(int,input().split())) for i in range(n-1)]

q = int(input())
Q = [int(input()) for i in range(q)]

M = 840
dist = [y]*M

for i in range(n-1)[::-1]:
    ndist = [0]*M
    p,t = PT[i]
    for j in range(M):

        times = (p-j%p)%p + t
        ndist[j] = dist[(times+j)%M] + times
    dist = ndist
    # print

ans = []
for q in Q:

    count = q+x

    ans.append(dist[count%M]+count)
print(*ans,sep="\n")
