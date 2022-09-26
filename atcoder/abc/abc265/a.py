x,y,n = map(int,input().split())
ans = 100000
for i in range(101):
    if i > n:
        break
    if (n-i)%3 != 0:
        continue
    ans = min(ans,x*i+(n-i)//3*y)
print(ans)