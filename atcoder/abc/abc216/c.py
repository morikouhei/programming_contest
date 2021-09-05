n = int(input())
s = bin(n)[2:]
ans = []
for i in s:
    if i == "1":
        ans.append("A")
    ans.append("B")
ans.pop()
print(*ans,sep="")