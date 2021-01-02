n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x,y = xy[i]
        a,b = xy[j]
        if abs(x-a) >= abs(y-b):
            ans += 1
print(ans//2)