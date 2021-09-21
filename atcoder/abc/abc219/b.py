S = [input() for i in range(3)]
T = list(input())
ans = ""
for t in T:
    t = int(t)
    ans += S[t-1]
print(ans)