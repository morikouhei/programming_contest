H,W,K = map(int,input().split())
C = [list(input()) for i in range(H)]

ans = 0
for i in range(1<<H):
    for j in range(1<<W):
        count = 0
        for h in range(H):
            for w in range(W):
                if ((i>>h)& 1) or ((j>>w)& 1) or C[h][w] == ".":
                    continue
                count += 1
        if count == K:
            ans += 1
print(ans)