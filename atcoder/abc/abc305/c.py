h,w = map(int,input().split())
S = [input() for i in range(h)]
H = []
W = []
for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            H.append(i)
            W.append(j)

for i in range(min(H),max(H)+1):
    for j in range(min(W),max(W)+1):
        if S[i][j] != "#":
            print(i+1,j+1)
            exit()