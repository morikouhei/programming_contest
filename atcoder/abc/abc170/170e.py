import heapq
import sys
input = sys.stdin.readline

n,q = map(int,input().split())
l = [[] for i in range(2*10**5+1)]
A = [-1]
B = [-1]
for i in range(n):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
    heapq.heappush(l[b],(-a,i+1))
    
h = []
for i in range(2*10**5+1):
    if l[i]:
        x,y = l[i][0]
        heapq.heappush(h,(-x,i,y))

for _ in range(q):
    c,d = map(int,input().split())
    nc = B[c]
    heapq.heappush(l[d],(-A[c],c))
    B[c] = d
    while True:
        x,y = l[nc][0]
        if B[y] != nc:
            heapq.heappop(l[nc])
        else:
            heapq.heappush(h,(-x,nc,y))
            break
        if len(l[nc]) == 0:
            break
    while True:
        x,y = l[d][0]
        if B[y] != d:
            heapq.heappop(l[d])
        else:
            heapq.heappush(h,(-x,d,y))
            break
        if len(l[d]) == 0:
            break
    
    while True:
        ans,p,i = h[0]
        if B[i] != p:
            heapq.heappop(h)
        elif l[p][0][0] != -ans:
            heapq.heappop(h)
        else:
            print(ans)
            break

