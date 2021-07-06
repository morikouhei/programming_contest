n,m = map(int,input().split())
small = [0]*n
for _ in range(m):
    a,b = [int(x)-1 for x in input().split()]
    if a > b:
        a,b = b,a
    small[b] += 1
print(small.count(1))
