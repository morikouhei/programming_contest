import itertools
n = int(input())
R = input()
C = input()

for la in itertools.permutations(range(n),n):

    for lb in itertools.permutations(range(n),n):

        for lc in itertools.permutations(range(n),n):


            ok = 1
            ans = [["."]*n for i in range(n)]

            for x,y in enumerate(la):
                if ans[x][y] != ".":
                    ok = 0
                ans[x][y] = "A"

            for x,y in enumerate(lb):
                if ans[x][y] != ".":
                    ok = 0
                ans[x][y] = "B"

            for x,y in enumerate(lc):
                if ans[x][y] != ".":
                    ok = 0
                ans[x][y] = "C"

            

            for i in range(n):
                for j in range(n):
                    if ans[i][j] != ".":
                        if ans[i][j] != R[i]:
                            ok = 0
                        break

            for i in range(n):
                for j in range(n):
                    if ans[j][i] != ".":
                        if ans[j][i] != C[i]:
                            ok = 0
                        break
        
                        
            if ok:
                print("Yes")

                for i in ans:
                    print("".join(i))
            
                exit()
print("No")