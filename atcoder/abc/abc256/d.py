n = int(input())
M = 2*10**5+5
count = [0]*M
for i in range(n):
    l,r = map(int,input().split())
    count[l] += 1
    count[r] -= 1

ans = []
l,r = -1,-1
for i in range(M-1):

    count[i+1] += count[i]
    if count[i] and l == -1:
        l = i
    if count[i] and count[i+1] == 0:
        r = i+1
        ans.append([l,r])
        l = -1
        r = -1
for i in ans:
    print(*i)
