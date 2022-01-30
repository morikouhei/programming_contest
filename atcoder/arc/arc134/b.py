n = int(input())
S = list(input())

cums = [[0]*26 for i in range(n+1)]
for i,s in enumerate(S):
    num = ord(s) - ord("a")
    for j in range(26):
        cums[i+1][j] = cums[i][j]
    cums[i+1][num] += 1


r = n-1
for i in range(n):
    s = S[i]
    num = ord(s) - ord("a")
    for j in range(num):
        if cums[r+1][j] - cums[i+1][j] > 0:

            while r >= 0 and ord(S[r])-ord("a") != j:
                r -= 1
            if r >= 0:
                S[i],S[r] = S[r],S[i]
                r -= 1
                break

print(*S,sep="")