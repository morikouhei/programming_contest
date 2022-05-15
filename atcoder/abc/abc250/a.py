h,w = map(int,input().split())
r,c = map(int,input().split())
ans = 0
for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
    x = r+di
    y = c+dj
    if 1 <= x <= h and 1 <= y <= w:
        ans += 1
print(ans)