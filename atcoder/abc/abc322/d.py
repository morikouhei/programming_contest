
P = [[list(input()) for i in range(4)] for j in range(3)]

for a in range(4):

    for b in range(4):

        
        for x1 in range(-3,4):
            for y1 in range(-3,4):

                for x2 in range(-3,4):
                    for y2 in range(-3,4):

                        for x3 in range(-3,4):
                            for y3 in range(-3,4):

                                ans = [[0]*4 for i in range(4)]

                                ok = 1

                                for x in range(4):
                                    for y in range(4):
                                        p = P[0][x][y]
                                        if p == ".":
                                            continue
                                        if x+x1 >= 4 or y+y1 >= 4 or x+x1 < 0 or y+y1 < 0:
                                            ok = 0
                                        else:
                                            ans[x+x1][y+y1] += 1

                                for x in range(4):
                                    for y in range(4):
                                        p = P[1][x][y]
                                        if p == ".":
                                            continue
                                        if x+x2 >= 4 or y+y2 >= 4 or x+x2 < 0 or y+y2 < 0:
                                            ok = 0
                                        else:
                                            ans[x+x2][y+y2] += 1

                                for x in range(4):
                                    for y in range(4):
                                        p = P[2][x][y]
                                        if p == ".":
                                            continue
                                        if x+x3 >= 4 or y+y3 >= 4 or x+x3 < 0 or y+y3 < 0:
                                            ok = 0
                                        else:
                                            ans[x+x3][y+y3] += 1
                        
                                if ok == 0:
                                    continue
                                
                                for i in ans:
                                    for j in i:
                                        if j != 1:
                                            ok = 0
                                
                                if ok:
                                    print("Yes")
                                    exit()
        P[2] = list(zip(*P[2][::-1]))

    P[1] = list(zip(*P[1][::-1]))
print("No")