import itertools
n, K = map(int,input().split())

ans = 0
t = [list(map(int,input().split())) for i in range(n)]

for i in itertools.permutations(range(1,n)):
    x = [0]+list(i)+[0]
    count = 0
    for k in range(len(x)-1):
        count += t[x[k]][x[k+1]]
    if count == K:
        ans += 1

print(ans)