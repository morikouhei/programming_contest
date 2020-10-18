x,y,a,b = map(int,input().split())

ans = 0
while x < y and x*a < x+b:
    ans += 1
    x *= a
ans += (y-x-1)//b
print(ans)