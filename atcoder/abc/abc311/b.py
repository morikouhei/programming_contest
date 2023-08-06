n,d = map(int,input().split())
nums = [0]*d
for i in range(n):
    S = input()
    for j,s in enumerate(S):
        if s == "o":
            nums[j] += 1


ans = 0
num = 0
for x in nums:
    if x == n:
        num += 1
        ans = max(ans,num)
    else:
        num = 0
print(ans)