n,m,l = map(int,input().split())
A = [[a,i] for i,a in enumerate(list(map(int,input().split())))]
B = [[a,i] for i,a in enumerate(list(map(int,input().split())))]

s = set()
for i in range(l):
    c,d = [int(x)-1 for x in input().split()]
    s.add((c,d))

A.sort()
B.sort()

ans = 0

for a,ia in A:

    for i in range(m)[::-1]:
        b,ib = B[i]
        if (ia,ib) not in s:
            ans = max(ans,a+b)
            break
print(ans)

