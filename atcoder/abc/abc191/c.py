h,w = map(int,input().split())
S = [input() for i in range(h)]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        c = 0
        for k in range(2):
            for t in range(2):
                c += S[i+k][j+t] == "#"
        if c%2:
            ans += 1
print(ans)
