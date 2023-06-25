n = int(input())
S = input()
ans = []
q = []
for s in S:
    if s == ")":
        if q and q[-1] == "(":
            q.pop()
            while True:
                x = ans.pop()
                if x == "(":
                    break
        else:
            ans.append(s)
            q.append(s)
    else:
        if s == "(":
            q.append(s)
        ans.append(s)
print(*ans,sep="")