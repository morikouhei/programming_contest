a,b,k = map(int,input().split())

tab = [[1]]
for i in range(1,70):
    nex = []
    for j in range(i+1):
        if j == 0 or j == i:
            nex.append(1)
        else:
            nex.append(tab[-1][j-1]+tab[-1][j])
    tab.append(nex)

ans = []
nowa = a
nowb = b
k -= 1
for i in range(a+b):
    if nowa == 0:
        ans.append("b")
        continue
    if nowb == 0:
        ans.append("a")
        continue
    count = tab[a+b-i-1][nowa-1]

    if count <= k:
        ans.append("b")
        nowb -= 1
        k -= count
    else:
        ans.append("a")
        nowa -= 1

print(*ans,sep="")
