w,h,t = map(int,input().split())
sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
ans = 0

dx = abs(sx-tx)
dy = abs(sy-ty)


# #### 1直接向かう
# if dx**2+dy**2 == t**2:
#     ans += 1

M = 3*10**5
for numy in range(-M,M):

    if numy >= 0:
        if numy%2:
            tty = h-ty
        else:
            tty = ty

        if numy != 0:
            tty += numy*h
        dy = abs(sy-tty)

    else:
        if numy%2:
            tty = h-ty
        else:
            tty = ty

        tty += numy*h
        dy = abs(sy-tty)

    if t**2 < dy**2:
        continue

    dx = int((t**2-dy**2)**0.5)
    for i in range(dx-1,dx+2):

        nsx = 0
        
        ttx = sx+i
        ntx = ttx//w
        
        if ntx%2:
            tttx = w-tx
        else:
            tttx = tx
        
        if tttx%w == ttx%w and (t**2 == dy**2+i**2):
            ans += 1
        
        if i == 0:
            continue
        ttx = sx-i
        ntx = ttx//w

        if ntx%2:
            tttx = w-tx
        else:
            tttx = tx
        
        if tttx%w == ttx%w and (t**2 == dy**2+i**2):
            ans += 1


print(ans)
