n,k = map(int,input().split())

pat = []
for i in range(k):
    pat.append("a")
    for j in range(i,0,-1):
        pat.append(chr(j+ord("a")))
        pat.append(chr(i+ord("a")))

ans = []
for i in range(n):
    ans.append(pat[i%(len(pat))])
print(*ans,sep="")