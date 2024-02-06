from heapq import heappop,heappush
n,m = map(int,input().split())
A = list(map(int,input().split()))


count = [0]*n

h = []
for i in range(n):
    heappush(h,[0,i])

for a in A:
    a -= 1
    count[a] += 1
    heappush(h,[-count[a],a])

    _,ans = h[0]
    print(ans+1)