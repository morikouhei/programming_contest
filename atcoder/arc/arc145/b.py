n,a,b = map(int,input().split())
if a <= b:
    print(max(n-a+1,0))
    exit()

if n < a:
    print(0)
    exit()

mul,mod = divmod(n,a)
ans = 0
if mul>1:
    ans += (mul-1)*b
ans += min(b,mod+1)

print(ans)