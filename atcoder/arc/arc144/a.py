n = int(input())
print(2*n)
left = n
ans = []
while left:
    ans.append(min(left,4))
    left -= min(left,4)
print(*ans[::-1],sep="")