n,m = map(int,input().split())
S = [input() for i in range(n)]
ans = n*(n-1)//2

count = [0]*2
for s in S:
    c = s.count("1")
    ans -= count[c%2]
    count[c%2] += 1
print(ans)