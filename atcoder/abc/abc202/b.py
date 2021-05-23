S = input()
ans = []
for s in S[::-1]:
    if s == "0" or s == "1" or s == "8":
        ans.append(s)
    elif s == "6":
        ans.append("9")
    else:
        ans.append("6")
print(*ans,sep="")