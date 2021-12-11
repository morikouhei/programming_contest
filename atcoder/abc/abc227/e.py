S = input()
n = len(S)
move = min(int(input()),n**2)
K = S.count("K")
E = S.count("E")
Y = n-K-E
dp = [[[0]*(move+1) for i in range(E+1)] for j in range(K+1)]

dp[0][0][0] = 1
for i in range(n):
    ndp = [[[0]*(move+1) for i in range(E+1)] for j in range(K+1)]
    for k in range(K+1):
        for e in range(E+1):
            for m in range(move+1):
                if dp[k][e][m] == 0:
                    continue
                num = dp[k][e][m]
                left = []
                know = k
                enow = e
                ynow = i-k-e
                for j in range(n):
                    if S[j] == "K":
                        if know:
                            know -= 1
                        else:
                            left.append("K")
                    if S[j] == "E":
                        if enow:
                            enow -= 1
                        else:
                            left.append("E")
                    if S[j] == "Y":
                        if ynow:
                            ynow -= 1
                        else:
                            left.append("Y")
                ## K use
                if k != K:
                    for j,s in enumerate(left):
                        if s == "K":
                            if m+j <= move:
                                ndp[k+1][e][m+j] += num
                            break
                ## E use
                if e != E:
                    for j,s in enumerate(left):
                        if s == "E":
                            if m+j <= move:
                                ndp[k][e+1][m+j] += num
                            break
            
                ## Y use
                if i-k-e != Y:
                    for j,s in enumerate(left):
                        if s == "Y":
                            if m+j <= move:
                                ndp[k][e][m+j] += num
                            break
    dp = ndp

ans = 0
for i in dp:
    for j in i:
        ans += sum(j)
print(ans)


