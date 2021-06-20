from math import gcd
l,r = map(int,input().split())

count = [0]*(r+5)
ans = 0
for i in range(r,1,-1):
    a = (l+i-1)//i
    b = r//i
    dif = max(b-a+1,0)
    count[i] = dif**2
    for j in range(2*i,r+1,i):
        count[i] -= count[j]
    if a > 1:
        ans += count[i]
    else:
        ans += count[i]-b-(b-1)

print(ans)


