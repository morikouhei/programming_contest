h,w = map(int,input().split())
C = [input() for i in range(h)]
ans = []
for i in range(w):
    num = 0
    for j in range(h):
        if C[j][i] == "#":
            num += 1
    ans.append(num)
print(*ans)