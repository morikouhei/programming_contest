n,k = map(int,input().split())
while k:
    if n%200 == 0:
        n //= 200
    else:
        n = n*1000+200
    k -= 1
print(n)