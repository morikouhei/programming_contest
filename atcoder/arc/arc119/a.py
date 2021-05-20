n = int(input())
ans = 10**20
for i in range(70):
    a,c = divmod(n,1<<i)
    ans = min(ans,a+i+c)
print(ans)
