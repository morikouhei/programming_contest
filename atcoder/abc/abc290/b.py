n,k = map(int,input().split())
S = input()
ans = []
for s in S:
    if s == "x":
        ans.append("x")
    else:
        if k > 0:
            ans.append("o")
            k -= 1
        else:
            ans.append("x")

print("".join(ans))