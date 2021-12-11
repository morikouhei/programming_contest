n = int(input())
ans = 0
for i in range(1,n+1):
    if i**3 > n:
        break
    for j in range(i,n+1):
        k = n//(i*j)
        if k < j:
            break
        ans += (k-j)+1
print(ans)