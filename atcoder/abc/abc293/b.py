n = int(input())
A = list(map(int,input().split()))
used = [0]*n
for i,a in enumerate(A):
    if used[i]:
        continue
    used[a-1] = 1

ans = []
for i in range(n):
    if used[i] == 0:
        ans.append(i+1)
print(len(ans))
print(*ans)