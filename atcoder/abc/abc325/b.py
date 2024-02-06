n = int(input())
WX = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(24):
    num = 0
    for w,x in WX:
        if 9 <= (x+i)%24 <= 17:
            num += w
    ans = max(ans,num)
print(ans)