h,w = map(int,input().split())
S = [list(input()) for i in range(h)]

Dx = [0,1,1,1,0,-1,-1,-1]
Dy = [1,1,0,-1,-1,-1,0,1]

snuke = "snuke"
for i in range(h):
    for j in range(w):

        for dx,dy in zip(Dx,Dy):
            ni = i + dx*4
            nj = j + dy*4

            if 0 <= ni < h and 0 <= nj < w:
                ok = 1
                x,y = i,j
                for k in range(5):
                    if S[x][y] != snuke[k]:
                        ok = 0
                    x += dx
                    y += dy
                
                if not ok:
                    continue

                x,y = i+1,j+1
                for k in range(5):
                    print(x,y)
                    x += dx
                    y += dy
                    
