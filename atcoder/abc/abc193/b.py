n = int(input())
l = [tuple(map(int,input().split())) for i in range(n)]

ans = 10**20
for a,p,x in l:
    if x > a:
        ans = min(ans,p)
if ans == 10**20:
    ans = -1
print(ans)
