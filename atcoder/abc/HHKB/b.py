h,w = map(int,input().split())
S = [list(input())+["#"] for i in range(h)]
S.append(["#"]*(w+1))

ans = 0
for i in range(h):
    for j in range(w):
        if S[i][j] == ".":
            if S[i][j+1] == ".":
                ans += 1
            if S[i+1][j] == ".":
                ans += 1
print(ans)