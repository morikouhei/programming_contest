n = int(input())
A = []
for _ in range(n):
    c = int(input())
    a = list(map(int,input().split()))
    A.append([c,a,_+1])
x = int(input())

ans = []
for a in A:
    if x in a[1]:
        ans.append(a)
ans.sort()

if ans == []:
    print(0)
    print()
else:
    out = []
    mi = ans[0][0]

    for x,_,ind in ans:
        if x == mi:
            out.append(ind)
    print(len(out))
    print(*sorted(out))