n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
P = [i-1 for i in map(int,input().split())]
ind = [-1]*n
for i in range(n):
    ind[P[i]] = i
bp = [(B[i],i) for i in range(n)]
bp.sort(reverse=True)
ans = []

for b,i in bp:
    if ind[i] == i:
        continue
    p = ind[i]
    if A[i] <= B[P[i]] or A[p] <= B[P[p]]:
        print(-1)
        exit()
    ans.append((i+1,p+1))
    ind[P[i]],P[p] = p,P[i]
print(len(ans))
for i in ans:
    print(*i)


