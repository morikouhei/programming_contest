S = input()

ans = 0

count = [0]*(1<<10)
count[0] = 1

now = 0
for s in S:
    x = int(s)
    now ^= 1<<x
    ans += count[now]
    count[now] += 1
print(ans)