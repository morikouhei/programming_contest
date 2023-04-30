S = [input() for i in range(8)]
for i in range(8):
    for j in range(8):
        if S[i][j] == "*":
            ans = "abcdefgh"[j] + str(8-i)
            print(ans)