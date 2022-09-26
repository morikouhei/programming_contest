S = list(input())
t = "atcoder"

ans = 0

for i in range(7):
    ind = S.index(t[i])
    if ind <= i:
        continue
    while ind > i:
        S[ind],S[ind-1] = S[ind-1],S[ind]
        ind -= 1
        ans += 1
print(ans)