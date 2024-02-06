n,s,m,l = map(int,input().split())

ans = 10**10
for i in range(n//6+2):
    for j in range(n//8+2):
        for k in range(n//12+2):

            if i*6 + j*8 + k*12 < n:
                continue
            ans = min(ans,i*s+m*j+l*k)

print(ans)