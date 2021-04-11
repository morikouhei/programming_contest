from heapq import heappop, heappush
n = int(input())
V = list(map(int,input().split()))

L = V[:n]
L = L[::-1]
R = V[n:]
ans = 0
count = []
for i in range(n):
    if R[i] >= L[i]:
        ans += R[i]
        count.append(0)
    else:
        ans += L[i]
        count.append(1)
h = []

for i in range(n)[::-1]:
    if count[i] == 0:
        base = R[i]
    else:
        base = L[i]
        
    if h:
        if -h[0] > base:
            num = -heappop(h)
            ans += num-base
            heappush(h, -base)

    if count[i] == 0:
        base = L[i]
    else:
        base = R[i]
    heappush(h, -base)
print(ans)
