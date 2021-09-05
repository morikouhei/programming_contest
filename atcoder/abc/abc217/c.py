n = int(input())
P = list(map(int,input().split()))
ans = [0]*n
for i,p in enumerate(P):
    ans[p-1] = i+1
print(*ans)