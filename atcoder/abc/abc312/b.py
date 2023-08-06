n,m = map(int,input().split())
S = [input() for i in range(n)]

for i in range(n-8):
    for j in range(m-8):
        ok = 1
        for x in range(4):
            for y in range(4):
                s =  S[i+x][j+y]
                if x < 3 and y < 3 and s == ".":
                    ok = 0
                if (x == 3 or y == 3) and s == "#":
                    ok = 0
                
                s = S[i+8-x][j+8-y]
                if x < 3 and y < 3 and s == ".":
                    ok = 0
                if (x == 3 or y == 3) and s == "#":
                    ok = 0
        if ok:
            print(i+1,j+1)