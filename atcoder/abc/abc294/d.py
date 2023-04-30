from heapq import heappop,heappush
n,q = map(int,input().split())


used = [0]*(n+1)

zero = []
for i in range(n):
    heappush(zero,i+1)

one = []

for _ in range(q):
    t,*l = map(int,input().split())
    if t == 1:
        x = heappop(zero)
        heappush(one,x)
    elif t == 2:
        x = l[0]
        used[x] = 1
    else:
        while used[one[0]] == 1:
            heappop(one)
        print(one[0])