import bisect
n,q = map(int,input().split())
A = [0]+list(map(int,input().split()))+[10**20]

cum = 0
L = [0]
for a,na in zip(A,A[1:]):
    L.append(L[-1]+(na-a-1))

for _ in range(q):
    k = int(input())
    ind = bisect.bisect_left(L,k)
    print(A[ind]+k-L[ind]-1)