n = int(input())

def f(a,b):
    return a**3 + a**2*b + a*b**2 + b**3

ans = 10**20
r = 10**6

for i in range(10**6+5):
    while r and f(i,r) >= n:
        r -= 1
    
    if f(i,r) >= n:
        ans = min(ans,f(i,r))
    else:
        ans = min(ans,f(i,r+1))
    


print(ans)