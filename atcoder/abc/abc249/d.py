n = int(input())
A = list(map(int,input().split()))
M = 2*10**5+5
count = [0]*M
for a in A:
    count[a] += 1

ans = 0
for i in range(1,M):
    if count[i] == 0:
        continue
    for j in range(i,M,i):
        if count[j] == 0 or count[j//i] == 0:
            continue
        ans += count[i]*count[j]*count[j//i]
print(ans)
