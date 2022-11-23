n,m = map(int,input().split())

ok = [[0]*n for i in range(n)]

for i in range(m):
    l = list(map(int,input().split()))
    for j in l[1:]:
        for k in l[1:]:
            ok[j-1][k-1] = 1

ans = 0
for i in ok:
    ans += sum(i)

print("Yes" if ans == n**2 else "No")