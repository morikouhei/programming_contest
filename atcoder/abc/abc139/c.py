n = int(input())
l = list(map(int,input().split()))
ans = 0
now = l[0]
count = 0
for i in range(1,n):
    if now >= l[i]:
        now = l[i]
        count += 1
        ans = max(ans,count)
    else:
        count = 0
        now = l[i]
print(max(ans,count))