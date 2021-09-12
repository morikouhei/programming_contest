P = list(map(int,input().split()))
ans = []
for p in P:
    ans.append(chr(ord("a")+p-1))
print(*ans,sep="")