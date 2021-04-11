from heapq import heappop, heappush
n = int(input())
V = list(map(int,input().split()))

ans = sum(V)
h = []
for i in range(n):
    heappush(h, V[n+i])
    heappush(h, V[n-1-i])
    ans -= heappop(h)
print(ans)