n,m = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(m)]

nums = [0]*n
for a,b in AB:
    nums[b-1] += 1


ans = 0
count = 0
for i,num in enumerate(nums,1):
    if num == 0:
        count += 1
        ans = i

if count > 1:
    print(-1)
else:
    print(ans)