n = int(input())
S = input()

cands = [0]*n

for i,s in enumerate(S):
    if s != "R":
        continue
    l = i-1
    r = i+1
    num = 0
    while 0 <= l and r < n and S[l] == "A" and S[r] == "C":
        num += 1
        l -= 1
        r += 1
    if num:
        cands[num] += 1

ans = 0
l = 1
r = n-1

for i in range(n):

    if i%2 == 0:
        while 0 < r and cands[r] == 0:
            r -= 1
        if r > 0 and cands[r]:
            ans += 1
            cands[r-1] += 1
            cands[r] -= 1
        else:
            break

    else:
        if l > 1 and cands[l-1]:
            l -= 1
        while l < n  and cands[l] == 0:
            l += 1
        if l < n and cands[l]:
            ans += 1
            cands[l] -= 1
        else:
            break
print(ans)
