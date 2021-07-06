n = int(input())
S = input()
ans = 0
o = 0
x = 0
for i,s in enumerate(S):
    if s == "o":
        x = max(x,i)
        while x < n and S[x] != "x":
            x += 1
        ans += n-x
    if s == "x":
        o = max(o,i)
        while o < n and S[o] != "o":
            o += 1
        ans += n-o
print(ans)