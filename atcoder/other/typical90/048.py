n,k = map(int,input().split())
L = []
for i in range(n):
    a,b = map(int,input().split())
    L.append(b)
    L.append(a-b)
print(sum(sorted(L)[-k:]))