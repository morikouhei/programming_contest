n = int(input())

ans = []
for i in range(n+1):
    ok = 0
    for j in range(1,10):

        if n%j == 0 and i%(n//j) == 0:
            ans.append(str(j))
            ok = 1
            break

    if ok == 0:
        ans.append("-")
print(*ans,sep="") 