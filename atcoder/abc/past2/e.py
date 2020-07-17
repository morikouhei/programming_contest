n = int(input())
a = [0]+list(map(int,input().split()))
ans = []
for i in range(1,n+1):
    count = 0
    now = i
    while True:
        now = a[now]
        count += 1
        if now == i:
            break
    ans.append(count)
print(*ans)
