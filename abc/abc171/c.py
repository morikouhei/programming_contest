n = int(input())

for i in range(1000):
    if n > 26**(i+1):
        n -= 26**(i+1)
    else:
        break
x = i+1

t = 26**i
ans = ""
for i in range(x-1,-1,-1):
    t = 26**i
    for j in range(26):
        if n > t:
            n -= t
        else:
            ans += chr(ord("a")+j)
            break
print(ans)

