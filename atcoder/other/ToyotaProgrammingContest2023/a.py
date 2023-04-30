n,m,v = map(int,input().split())

ans = 0

for h in range(1,n+1):
    for w in range(1,m+1):
        
        count = w*(w-1)//2*h + h*(h-1)//2*w*m

        rest = v-count
        if rest < 0 or rest%(h*w):
            continue
        x,y = divmod(rest//(h*w)-1,m)
        if x+h <= n and y+w <= m:
            ans += 1
print(ans)
