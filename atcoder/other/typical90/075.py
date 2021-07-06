n = int(input())
ans = 0
now = n
for i in range(2,int(n**0.5)+1):
    while now%i == 0:
        now //= i
        ans += 1
if now != 1:
    ans += 1

res = 0
while ans != 1:
    ans = (ans+1)//2
    res += 1
print(res)