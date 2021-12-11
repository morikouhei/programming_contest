S = input()
K = int(input())
ans = 0
now = 0
n = len(S)
nk = K
for i in range(n):  
    while now < n:
        if S[now] == "X":
            now += 1
            continue
        if nk:
            nk -= 1
            now += 1
        else:
            break
    ans = max(ans,now-i)
    if S[i] == ".":
        nk += 1
print(ans)