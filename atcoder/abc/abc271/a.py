n = int(input())
l = "0123456789ABCDEF"

ans = []
for i in range(2):
    ans.append(l[n%16])
    n //= 16
print(*ans[::-1],sep="")