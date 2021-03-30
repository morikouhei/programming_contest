from heapq import heappush,heappop
t = int(input())
for _ in range(t):
    n = int(input())
    q = list(map(int,input().split()))
    def calc(p):
        ans = []
        ma = 0
        h = []
        for i in range(n):
            if q[i] > ma:
                for j in range(ma+1,q[i]):
                    heappush(h,p*j)
                ans.append(q[i])
                ma = q[i]
            else:
                x = p*heappop(h)
                ans.append(x)
        return ans
        
    print(*calc(1))
    print(*calc(-1))

