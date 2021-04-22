n = int(input())
a,b,c = map(int,input().split())

ans = 10**20
for i in range(10000):
    for j in range(10001-i):
        if i*a+j*b > n:
            break
        k,m = divmod(n-i*a-j*b, c)
        if m == 0:
            ans = min(ans, i+j+k)
print(ans)