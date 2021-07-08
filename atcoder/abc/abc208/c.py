n,k = map(int,input().split())
A = list(map(int,input().split()))
sA = [[a,i] for i,a in enumerate(A)]
sA.sort()
base = k//n
ans = [base]*n
for i in range(k%n):
    ans[sA[i][1]] += 1
for i in ans:
    print(i)