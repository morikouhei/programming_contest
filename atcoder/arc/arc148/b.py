n = int(input())
S = list(input())
d = {"d":0,"p":1}
rd = {0:"d",1:"p"}
S = [d[s] for s in S]
ans = S[:]

for i in range(n):
    if S[i] == 0:
        continue
    l = i
    for r in range(l,n):
        temp = S[:]
        change = temp[l:r+1]
        change = [x^1 for x in change[::-1]]
        temp[l:r+1] = change
        if ans > temp:
            ans = temp
    break

ans = [rd[s] for s in ans]
print("".join(ans))