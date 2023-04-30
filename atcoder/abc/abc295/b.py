r,c = map(int,input().split())
B = [list(input()) for i in range(r)]

ans = [["#"]*c for i in range(r)]
for i in range(r):
    for j in range(c):
        ans[i][j] = B[i][j]
for i in range(r):
    for j in range(c):
        if B[i][j] in ".#":
            continue
        p = int(B[i][j])

        for x in range(r):
            for y in range(c):
                if abs(i-x)+abs(j-y) <= p:
                    ans[x][y] = "."


for i in ans:
    print("".join(i))