n,a,b = map(int,input().split())
ans = [["."]*(b*n) for i in range(a*n)]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            continue
        sx = i*a
        sy = j*b
        for k in range(a):
            for t in range(b):
                ans[sx+k][sy+t] = "#"

for i in ans:
    print(*i,sep="")