n = int(input())
A = list(map(int,input().split()))
num = [0]*n
ans = []
for i,a in enumerate(A):
    a -= 1
    num[a] += 1
    if num[a] == 2:
        ans.append([i,a+1])

ans.sort()
ans = [a for _,a in ans]
print(*ans)