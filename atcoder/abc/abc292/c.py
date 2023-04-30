n = int(input())

dic = {}
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j > n:
            break
        if i == j:
            dic[i*j] = dic.get(i*j,0)+1
        else:
            dic[i*j] = dic.get(i*j,0)+2
ans = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        if i*j > n:
            break
        if i == j:
            ans += dic.get(n-i*j,0)
        else:
            ans += dic.get(n-i*j,0)*2

print(ans)