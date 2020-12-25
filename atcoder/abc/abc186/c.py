n = int(input())

ans = 0
for i in range(1,n+1):
    if "7" in str(i):
        continue
    l = []
    x = i
    while x:
        l.append(x%8)
        x //= 8
    if 7 in l:
        continue
    ans += 1
print(ans)