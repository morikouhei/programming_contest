import bisect
n,q,x = map(int,input().split())
W = list(map(int,input().split()))

s = sum(W)
p = x//s
x %= s
base = [0]+W+W
for i in range(1,2*n+1):
    base[i] += base[i-1]

doubling = [[-1]*n for i in range(50)]
size = [0]*n
for i in range(n):
    y = base[i]
    ind = bisect.bisect_left(base,y+x)
    doubling[0][i] = ind%n
    size[i] = p*n+ind-i

for i in range(1,50):
    for j in range(n):
        doubling[i][j] = doubling[i-1][doubling[i-1][j]]

for _ in range(q):
    k = int(input())
    k -= 1
    now = 0
    for i in range(50)[::-1]:
        if k >= 1<<i:
            k -= 1<<i
            now = doubling[i][now]
    print(size[now])