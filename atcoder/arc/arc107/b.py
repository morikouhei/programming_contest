n,k = map(int,input().split())
k = abs(k)
ans = 0
for i in range(k+2,2*n+1):
    if i <= n+1:
        a = i-1
    else:
        a = n-(i-n)+1
    if i-k <= n+1:
        b = i-k-1
    else:
        b = n-(i-k-n)+1
    ans += a*b
print(ans)