n = int(input())
A = list(map(int,input().split()))
p = 0
ans = [0]*4
for a in A:
    ans[0] += 1
    nans = [0]*4
    for i in range(4):
        if ans[i] and i+a < 4:
            nans[i+a] += 1
        elif ans[i] and i+a >= 4:
            p += 1
    ans = nans
print(p)