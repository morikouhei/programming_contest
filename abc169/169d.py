n = int(input())

d = {}
for i in range(2,int(n**0.5)+1):
    if n%i == 0:
        d[i] = 0
        while n%i == 0:
            d[i] += 1
            n //= i
if n > 1:
    d[n] = 1

ans = 0
for i in d.values():
    x = i
    for j in range(1,10000):
        if x >= j:
            x -= j
            ans += 1
        else:
            break
print(ans)

