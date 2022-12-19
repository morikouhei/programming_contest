n = int(input())
S = input()
ans = []
now = 0
for s in S:
    if s == ",":
        if now%2 == 0:
            s = "."

    if s == '"':
        now += 1
    ans.append(s)
print(*ans,sep="")