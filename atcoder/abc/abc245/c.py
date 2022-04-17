n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

s = [A[0],B[0]]
for i in range(1,n):
    a,b = A[i],B[i]
    ns = set()
    for x in s:
        for nex in ((a,b)):
            if abs(x-nex) <= k:
                ns.add(nex)
    s = ns
print("Yes" if s else "No")