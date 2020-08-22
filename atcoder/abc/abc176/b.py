ans = 0

for i in input().split():
    ans += int(i)

print("No" if ans%9 else "Yes")