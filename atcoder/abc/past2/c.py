n = int(input())
s = [list(input()) for i in range(n)]

for i in range(n-2,-1,-1):
    for j in range(1,2*n-2):
        if s[i][j] == ".":
            continue
        for k in range(-1,2):
            if s[i+1][j+k] == "X":
                s[i][j] = "X"
for i in s:
    print(*i,sep="")