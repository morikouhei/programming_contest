from heapq import heappush,heappop
n,l = map(int,input().split())
A = list(map(int,input().split()))

h = []
for a in A:
    heappush(h,a)
if l - sum(A):
    heappush(h,l-sum(A))
ans = 0

while len(h) > 1:
    x = heappop(h)
    y = heappop(h)
    ans += x+y
    heappush(h,x+y)
    
print(ans)