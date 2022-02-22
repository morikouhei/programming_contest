n = int(input())
use = [0]*(361)
use[0] = 1
now = 0
A = list(map(int,input().split()))
for a in A:
    now += a
    now %= 360
    use[now] = 1

ans = 0
l = 0
for i in range(1,360):
    if use[i]:
        ans = max(ans,i-l)
        l = i
ans = max(ans,360-l)
print(ans)