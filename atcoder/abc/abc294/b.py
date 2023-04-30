h,w = map(int,input().split())
ans = []
A = [list(map(int,input().split())) for i in range(h)]
for i in range(h):
    l = []
    for j in range(w):
        if A[i][j] == 0:
            l.append(".")
        else:
            l.append(chr(ord("A")+A[i][j]-1))
    print("".join(l))