n = int(input())
LR = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    l,r = LR[i]
    cum = 0
    for j in range(l,r+1):
        for k in range(i+1,n):
            nl,nr = LR[k]
            cum += max(min(nr-nl+1,j-nl),0)/(nr-nl+1)
    ans += cum/(r-l+1)
print(ans)