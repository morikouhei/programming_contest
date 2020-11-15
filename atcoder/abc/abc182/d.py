n = int(input())
a = list(map(int,input().split()))
now = 0
count = 0
ma = 0
ans = now
for i in a:
    count += i
    ma = max(ma,count)
    ans = max(ans,ma+now)
    now += count
print(ans)