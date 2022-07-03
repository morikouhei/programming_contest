n,k = map(int,input().split())

if k > int(str(k)[::-1]):
    print(0)
    exit()
ans = set)0
for i in range(15):
    c = k * 10**i
    if c <= n:
        ans.add(c)

rk = int(str(k)[::-1])

for i in range(15):
    c = rk * 10**i
    if c <= n:
        ans.add(c)
print(len(ans))