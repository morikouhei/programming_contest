S = input()
ans = 0
p = 1
for s in S[::-1]:
    num = ord(s)-ord("A")+1
    ans += num*p
    p *= 26
print(ans)