h,w = map(int,input().split())
S = [list(input()) for i in range(h)]
L = []
for i in range(h):
    for j in range(w):
        if S[i][j] == "o":
            L.append((i,j))

x,y = L[0]
nx,ny = L[1]
print(abs(x-nx)+abs(y-ny))