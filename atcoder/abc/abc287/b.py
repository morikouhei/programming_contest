n,m = map(int,input().split())
S = [int(input())%1000 for i in range(n)]
T = [0]*1000
for i in range(m):
    T[int(input())] += 1
ans = 0
for s in S:
    if T[s]:
        ans += 1
print(ans)