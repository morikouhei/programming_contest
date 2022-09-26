a,b,c,d,e = map(int,input().split())
nums = [0]*14
for i in (a,b,c,d,e):
    nums[i] += 1

two = 0
three = 0
for i in range(14):
    if nums[i] == 2:
        two = 1
    if nums[i] == 3:
        three = 1

print("Yes" if two*three else "No")