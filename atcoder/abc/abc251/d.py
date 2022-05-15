W = int(input())
ans = []
M = 10**6
for i in range(1,100):
    ans.append(i)
    ans.append(i*100)
    ans.append(i*10000)
ans.append(M)
ans.sort()
print(len(ans))
print(*ans)