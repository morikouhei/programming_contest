n = int(input())
inf = 10**20
A = list(map(int,input().split()))+[-inf,inf]
A.sort()

q = int(input())
B = [[int(input()),i] for i in range(q)]
ans = [0]*q
B.sort()

now = 0
for b,i in B:
    while now < n+2 and b > A[now]:
        now += 1
    ans[i] = min(b-A[now-1],A[now]-b)

for i in ans:
    print(i)