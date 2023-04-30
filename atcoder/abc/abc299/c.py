n = int(input())
S = input()
if "o" not in S or "-" not in S:
    print(-1)
    exit()


ans = 0
num = 0
for s in S:
    if s == "o":
        num += 1
        ans = max(ans,num)
    else:
        num = 0
print(ans)