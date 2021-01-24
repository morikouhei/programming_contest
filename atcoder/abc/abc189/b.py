n,x = map(int,input().split())
count = 0
ans = -1
for i in range(n):
    v,p = map(int,input().split())
    count += v*p
    if count > 100*x:
        ans = i+1
        break
print(ans)
