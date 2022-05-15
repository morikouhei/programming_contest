n,w = map(int,input().split())
A = list(map(int,input().split())) + [0,0]
ans = set()
for i in range(n+2):
    for j in range(i):
        for k in range(j):
            if A[i]+A[j]+A[k] <= w:
                ans.add(A[i]+A[j]+A[k])
print(len(ans))
